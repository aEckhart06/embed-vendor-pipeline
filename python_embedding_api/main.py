from fastapi import FastAPI
from app.routes import items

app = FastAPI(title="My API", version="1.0.0")

# include routers
app.include_router(items.router)

# Middleware
# CORS
# Authentication
# Rate Limiting
# Logging
# Error Handling
# Performance
# Security
# Monitoring

@app.get("/")
def root():
    return {"message": "Welcome to My API!"}