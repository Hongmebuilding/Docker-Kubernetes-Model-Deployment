FROM python:3.9
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY train_model.py .
COPY generate_data.py .
COPY model /model/

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
