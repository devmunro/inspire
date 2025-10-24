from fastapi import FastAPI
from routes import quotes
import random

app = FastAPI(
    title="Inspire API",
    description="A simple API for inspirational quotes.",
    version="1.0.0"
)

app.include_router(quotes.router, prefix="/quotes", tags=["Quotes"])

@app.get("/")
def root():
    messages = [
        "Welcome to Inspire API — fuel your mind with motivation! 🚀",
        "Your daily dose of inspiration starts here ✨",
        "Dream big. Code harder. Inspire always 💪"
    ]

    return {
        "message": random.choice(messages),
        "docs_url": "/docs",
    }
