
FROM python:3.12-slim
 

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=5500
EXPOSE 5500


CMD ["python", "app.py"]


