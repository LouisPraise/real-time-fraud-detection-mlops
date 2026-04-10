FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY FraudDetection.py .
COPY My_Fd_Model.pkl .

RUN pip install -r requirements.txt

CMD ["uvicorn", "FraudDetection:app", "--host", "0.0.0.0", "--port", "8000"]
