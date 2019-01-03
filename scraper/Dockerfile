FROM python:3.7

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./check.sh"]
# ENTRYPOINT [ "python" ]
