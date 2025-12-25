# SR Google STT Add-on

Home Assistant용 Google Speech Recognition STT 애드온입니다.

## 특징

- Google Web Speech API를 사용한 음성 인식
- 한국어 및 다국어 지원
- 사용자 정의 포트 설정
- REST API 엔드포인트 제공

## 설치 방법

1. Home Assistant → 설정 → 추가 기능
2. 우측 상단 ⋮ → Repositories
3. 저장소 URL 추가:
   ```
   https://github.com/JS-HAN-1987/sr-google-stt-addon
   ```
4. "SR Google STT" 설치
5. 설정에서 포트와 언어 조정 (선택사항)
6. Start 클릭

## 설정

### 옵션

- **port** (기본값: 5005): STT 서버 포트
- **language** (기본값: ko-KR): 인식할 언어 코드
  - 한국어: ko-KR
  - 영어(미국): en-US
  - 일본어: ja-JP
  - 중국어: zh-CN

### 예제 설정
```yaml
port: 5005
language: ko-KR
```

## API 사용법

### STT 엔드포인트

**POST** `/stt`

음성 파일을 전송하여 텍스트로 변환합니다.

```bash
curl -X POST \
  http://homeassistant.local:5005/stt \
  -F "file=@audio.wav"
```

**응답:**
```json
{
  "result": "안녕하세요"
}
```

### 헬스체크

**GET** `/health`

```bash
curl http://homeassistant.local:5005/health
```

**응답:**
```json
{
  "status": "healthy"
}
```

### 정보 확인

**GET** `/info`

```bash
curl http://homeassistant.local:5005/info
```

**응답:**
```json
{
  "name": "SR Google STT",
  "version": "1.0.0",
  "port": 5005,
  "language": "ko-KR"
}
```

## 지원 아키텍처

- aarch64 (Raspberry Pi 4/5 64-bit)
- amd64 (Intel/AMD 64-bit)
- armv7 (Raspberry Pi 3/4 32-bit)
- armhf (ARM 32-bit)

## 문제 해결

### 애드온이 시작되지 않을 때
1. 로그 확인
2. 포트 충돌 확인 (다른 포트로 변경)
3. 애드온 재시작

### 음성 인식이 안 될 때
- 오디오 파일이 WAV 형식인지 확인
- 인터넷 연결 확인 (Google API 사용)
- language 설정이 올바른지 확인

## 라이센스

MIT License

## 유지보수자

JS-HAN-1987