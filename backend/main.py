from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/get_openai_summary/")
async def root(topic: str):
    print(topic)
    return {"data": f"{topic} back"}