import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from core import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    default_response_class=ORJSONResponse
)

@app.get("/")
async def hello_world():
    return "hello world"

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)