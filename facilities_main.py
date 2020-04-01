from fastapi import FastAPI

myFirstapp = FastAPI()

@myFirstapp.get("/")
async def root():
    return {"message": "Hello trisejasfdsfnksdgfnjdfngdfg"}
