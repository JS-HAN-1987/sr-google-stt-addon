ARG BUILD_FROM
FROM $BUILD_FROM

ENV PIP_BREAK_SYSTEM_PACKAGES=1

WORKDIR /app

RUN apk add --no-cache python3 py3-pip flac

COPY requirements.txt run.py ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "/app/run.py"]
