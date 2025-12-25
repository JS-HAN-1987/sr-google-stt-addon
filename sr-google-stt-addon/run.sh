#!/usr/bin/with-contenv bashio

echo "--- SR Google STT 서버 시작 중 ---"

# Flask REST API 서버 백그라운드 실행
python3 /app.py &

# Wyoming Protocol 서버 전면 실행 (HA 음성 어시스턴트용)
exec python3 /wyoming_stt.py