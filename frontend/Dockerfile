FROM python:3.13-slim

WORKDIR /frontend

COPY frontend/server.py .
COPY frontend/index.html .

EXPOSE 3000

CMD ["python", "server.py"]
