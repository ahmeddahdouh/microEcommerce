from itertools import product

from fastapi import FastAPI, APIRouter

from src.endpoints.client_endpoint import client_router
from src.endpoints.commande_endpoint import commande_router
from src.endpoints.product_endpoint import product_router

app = FastAPI()
app.include_router(product_router)
app.include_router(client_router)

app.include_router(commande_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

