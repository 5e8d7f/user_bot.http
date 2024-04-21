FROM python:3.12-alpine3.19 

WORKDIR /app

COPY requirements.txt /app

RUN apk add --no-cache --virtual .build-deps gcc=~13.2.1_git20231014-r0 musl-dev=~1.2.4_git20230717-r4 linux-headers~=6.5-r0 && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

COPY . /app

CMD ["python", "-u", "main.py"]
