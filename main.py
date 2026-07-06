from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def read_items():
    return {"message": "List items for: build me a test app"}
