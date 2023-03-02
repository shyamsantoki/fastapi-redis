from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Database configuration
HOST = getenv("FASTAPI_HOST")
PORT = getenv("FASTAPI_PORT")
