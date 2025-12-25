# 라즈베리 파이 5(64비트) 및 기타 아키텍처 지원
ARG BUILD_FROM
FROM $BUILD_FROM

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# 시스템 의존성 설치 (STT용 FLAC 및 파이썬)
RUN apk add --no-cache \
    python3 \
    py3-pip \
    flac

# 파일 복사
COPY run.sh /
COPY app.py /
COPY wyoming_stt.py /
COPY requirements.txt /

# 의존성 설치
RUN pip3 install --no-cache-dir --break-system-packages -r /requirements.txt

# 실행 권한 부여
RUN chmod a+x /run.sh

# 실행
CMD [ "/run.sh" ]