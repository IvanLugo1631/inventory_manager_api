# DEACERO - FastAPI Microservice

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

## Docker Setup
- Build and start containers:
  ```bash
  docker-compose up --build
  ```

- Stop containers:
  ```bash
  docker-compose down
  ```

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

## Infrastructure Components
- FastAPI Application Server
- PostgreSQL Database
- OAuth2.0 Authentication Service
- Docker Containers
- Alembic Migration System

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
