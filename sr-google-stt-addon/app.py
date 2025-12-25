from flask import Flask, request, Response
import speech_recognition as sr
import os
import json

app = Flask(__name__)

recognizer = sr.Recognizer()

def json_response(data, status=200):
    """한글이 제대로 표시되는 JSON 응답"""
    return Response(
        json.dumps(data, ensure_ascii=False),
        status=status,
        mimetype='application/json; charset=utf-8'
    )

def load_options():
    """애드온 옵션 로드"""
    options_file = "/data/options.json"
    if os.path.exists(options_file):
        try:
            with open(options_file, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"옵션 로드 실패: {e}", flush=True)
    # 기본값
    return {"port": 5005, "language": "ko-KR"}

@app.route('/stt', methods=['POST'])
def speech_to_text():
    """음성을 텍스트로 변환"""
    if 'file' not in request.files:
        return json_response({"error": "파일이 없습니다"}, 400)
    
    audio_file = request.files['file']
    options = load_options()
    language = options.get('language', 'ko-KR')
    
    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language=language)
            return json_response({"result": text})
    except sr.UnknownValueError:
        return json_response({"error": "음성을 인식할 수 없습니다"}, 422)
    except sr.RequestError as e:
        return json_response({"error": f"Google 서비스 에러: {e}"}, 500)
    except Exception as e:
        return json_response({"error": f"서버 오류: {str(e)}"}, 500)

@app.route('/health', methods=['GET'])
def health_check():
    """상태 확인"""
    return json_response({"status": "healthy"})

@app.route('/info', methods=['GET'])
def info():
    """애드온 정보"""
    options = load_options()
    return json_response({
        "name": "SR Google STT",
        "version": "1.0.0",
        "port": options.get('port', 5005),
        "language": options.get('language', 'ko-KR')
    })

if __name__ == '__main__':
    options = load_options()
    port = options.get('port', 5005)
    
    print("=" * 50, flush=True)
    print(f"SR Google STT 서버 시작", flush=True)
    print(f"포트: {port}", flush=True)
    print(f"언어: {options.get('language', 'ko-KR')}", flush=True)
    print("=" * 50, flush=True)
    
    app.run(host='0.0.0.0', port=port, debug=False)