FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8000
ENV POSTGRES_DATABASE_URI=postgresql://postgres.ccafmriemaxluvacwokn:fu2hxj6LNEd8Ks4F@aws-0-us-west-1.pooler.supabase.com:6543/postgres
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]