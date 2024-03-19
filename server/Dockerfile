FROM python:3.9

COPY . /app
WORKDIR /app

RUN pip install grpcio grpcio-tools

EXPOSE 50051

CMD ["python", "server.py"]
