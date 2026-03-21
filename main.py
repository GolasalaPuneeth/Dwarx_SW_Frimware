from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from Routes import Payments
import time
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--------------> On Pull up")
    yield
    print("--------------> On Pull down")


app = FastAPI(root_path="/",
              title="HYDROPAY VENDX BACKEND",
              lifespan=lifespan)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    response.headers["X-Response-Time"] = f"{execution_time:.2f} ms"
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://www.tapmytalent.com"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Payments,prefix="/v1")


# @app.get("/")
# async def read_root():
#     return {"Hello": "World"}





if __name__=="__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=3001)