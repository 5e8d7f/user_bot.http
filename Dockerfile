FROM python:alpine

RUN apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apk del .build-deps

COPY . .

CMD ["python", "-u", "main.py"]
