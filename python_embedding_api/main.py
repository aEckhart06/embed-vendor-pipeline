from fastapi import FastAPI
from routes import items

app = FastAPI(title="My API", version="1.0.0")


# include routers
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to My API!"}

if __name__ == 'main':
    app.run(host='0.0.0.0', port=8080)