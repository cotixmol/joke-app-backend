FROM python:3.10

COPY . /joke_app
WORKDIR /joke_app

RUN pip install fastapi uvicorn

CMD ["uvicorn", "main:joke_app", "--host", "0.0.0.0", "--port", "80"]
