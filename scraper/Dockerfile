FROM python:3.7

RUN apt-get update && apt-get install -y parallel

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./check.sh"]
# ENTRYPOINT [ "python" ]
