from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.bookings.router import router as booking_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(booking_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
