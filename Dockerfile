FROM python:3.10-alpine

WORKDIR /usr/src/app

RUN pip install --no-cache-dir requests-html
COPY utlista.py .

CMD ["python", "utlista.py"]
