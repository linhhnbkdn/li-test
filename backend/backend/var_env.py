import os

# Load environment variables
# DB configurations
DB_USER: str = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Redis configurations
REDIS_URL = os.getenv("REDIS_URL")

# Celery configurations
BROKER_URL = os.getenv("BROKER_URL")
