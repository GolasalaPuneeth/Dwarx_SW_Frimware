from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from Routes import Payments
from DatabaseLayer import engine,SQLModel
import time
import uvicorn



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("--------------> On Pull up")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    print("--------------> On Pull down")
    await engine.dispose()


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
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Payments,prefix="/v1")


if __name__=="__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=3000)