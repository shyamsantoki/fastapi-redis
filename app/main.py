from fastapi import FastAPI
from routes import health, user

app = FastAPI()

app.include_router(health.router)
app.include_router(user.router)


@app.get("/")
def root():
    return {"message": "Root route"}
