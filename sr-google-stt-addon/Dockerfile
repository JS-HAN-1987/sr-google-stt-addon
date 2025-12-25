# 라즈베리 파이 5(64비트) 전용 베이스 이미지 사용
FROM ghcr.io/home-assistant/aarch64-base:latest

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# 시스템 의존성 설치 (STT용 FLAC 및 파이썬)
RUN apk add --no-cache \
    python3 \
    py3-pip \
    flac

# Python 라이브러리 설치 (강제 설치 옵션 추가)
RUN pip3 install --no-cache-dir --break-system-packages \
    flask \
    SpeechRecognition

# 파일 복사
COPY run.sh /
COPY app.py /

# 실행 권한 부여
RUN chmod a+x /run.sh

# S6-overlay 호환을 위한 실행 방식
CMD [ "/run.sh" ]