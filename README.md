# DEACERO 

## Description
A FastAPI-based microservice architecture designed for handling REST APIs, with PostgreSQL integration and OAuth2.0 authentication. This project emphasizes scalability, security, and performance through asynchronous programming.

## Technical Stack
- FastAPI for API development
- PostgreSQL for database
- Alembic for migrations
- Docker for containerization
- OAuth2.0 for authentication


## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/IvanLugo1631/inventory_manager_api
    ```

2. Navigate to the project directory:
    ```bash
    cd inventory_manager_api
    ```

3. Create and activate virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Linux/macOS
    # or
    .venv\Scripts\activate     # For Windows
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Option 1: Docker Compose Setup
To set up the project using Docker Compose, follow these steps:

1. Change to the `docker-compose` branch:
    ```bash
    git checkout docker-compose
    ```

2. Build and start the containers:
    ```bash
    docker-compose up --build
    ```

3. Stop the containers:
    ```bash
    docker-compose down
    ```

## Option 2: Run the app
To set up the project, follow these steps:

1. Change to the `main` branch:
    ```bash
    git checkout main
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Start the app:
    ```bash
    uvicorn app.main:app --reload
    ```

4. Access the app at [http://localhost:8000](http://localhost:8000)

## Database Migrations

- Create new migration:
  ```bash
  alembic revision --autogenerate -m "Your migration message"
  ```

- Apply migrations:
  ```bash
  alembic upgrade head
  ```



## Key Features
- Asynchronous Operations: Leveraging FastAPI's async capabilities for improved performance
- Secure Authentication: OAuth2.0 implementation for robust security
- Database Integration: PostgreSQL configured as a microservice
- Docker Support: Containerized deployment for consistency across environments
- Migration Management: Database versioning with Alembic
- Unitest: pytest to run it create every edge case 
- Stress test: 
    - Locust: Open-source load testing tool that allows to define user behavior with Python code and simulate multiple users.


## Infrastructure Components
- FastAPI Application Server
- PostgreSQL Database
- OAuth2.0 Authentication Service
- Docker Containers
- Alembic Migration System
  
  Full System

  
![image](https://github.com/user-attachments/assets/9b547b23-1eae-47e2-b153-3325fea45944)

Data Model


![image](https://github.com/user-attachments/assets/ab09b49d-44a7-4f72-afc3-38b2f7c6bca3)

## API Documentation
Once running, access the API documentation at:

Local 

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

Remote 
- Swagger UI: [https://inventory-manager-api-237050277063.us-south1.run.app/docs](remote/docs)
- ReDoc: [https://inventory-manager-api-237050277063.us-south1.run.app/redoc](remote/redoc)

## Environment Variables
Create a `.env` file in the root directory with:
