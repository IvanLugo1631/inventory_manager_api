FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
ENV POSTGRES_DATABASE_URI=postgresql://fastapi_user:strongpassword123@db:5432/fastapi_db
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]