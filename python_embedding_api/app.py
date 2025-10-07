from fastapi import FastAPI, Request
import uvicorn


app = FastAPI(title="My API", version="1.0.0")

# include routers
# app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "Welcome to My API!"}

@app.post("/transformAndEmbedData")
async def transformAndEmbedData(request: Request):
    data = await request.json()
    return {
        "message": "The api has received the data!",
        "data": data
        }


if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8080, reload=True)