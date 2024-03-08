import os
import time
from contextlib import asynccontextmanager

import fastapi
import uvicorn
from loguru import logger

import genfile
import routers


@asynccontextmanager
async def init_server(app: fastapi.FastAPI):
    logger.info("Checking if test file exists...")
    if not os.path.exists("./media/1gb.txt") or not os.path.exists("./media/500mb.txt"):
        logger.info("Missing test files, generating them...")
        genfile.generate_files()
    logger.info("Everything is ready!")
    yield


app = fastapi.FastAPI(
    title="Web Server for CS4296 Cloud Computing Project",
    lifespan=init_server,
)

app.include_router(routers.router, prefix="/api/test")


# Reference: https://fastapi.tiangolo.com/tutorial/middleware/


@app.middleware("http")
async def monitor_process_time(request: fastapi.Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    process_time_in_ms = process_time * 1000
    response.headers["X-Process-Time"] = f"{process_time_in_ms}ms"
    return response


@app.get("/")
def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
