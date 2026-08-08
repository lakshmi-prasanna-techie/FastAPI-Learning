from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "My First FastAPI Project"
    }


@app.get("/about")
async def about():
    return {
        "name": "Lakshmii",
        "skill": "Learning FastAPI",
        "project": "Building APIs"
    }