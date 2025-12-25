#!/usr/bin/with-contenv bashio

echo "--- SR Google STT 서버 시작 중 ---"

# 디버깅: Python과 패키지 확인
echo "[DEBUG] Python 버전:"
python3 --version

echo "[DEBUG] 설치된 패키지:"
pip3 list | grep -i wyoming

echo "[DEBUG] 파일 확인:"
ls -la /wyoming_stt.py
ls -la /app.py

# Flask REST API 서버 백그라운드 실행
echo "[INFO] Flask 서버 시작..."
python3 /app.py &
FLASK_PID=$!
echo "[INFO] Flask PID: $FLASK_PID"

# 잠깐 대기
sleep 2

# Wyoming Protocol 서버 실행 (에러 캡처)
echo "[INFO] Wyoming 서버 시작..."
python3 /wyoming_stt.py 2>&1 || {
    echo "[ERROR] Wyoming 서버 시작 실패! 에러 코드: $?"
    echo "[ERROR] Flask만 실행된 상태로 유지합니다"
    wait $FLASK_PID
    exit 1
}