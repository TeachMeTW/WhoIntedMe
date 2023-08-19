FROM python:3.11.4

WORKDIR /whointedme

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . ./app

CMD ["python", "./app/app.py"]
