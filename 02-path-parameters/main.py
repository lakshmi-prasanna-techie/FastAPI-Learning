from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to Lakshmi's Mini Shop! "
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": f"Product #{product_id}",
        "available": True
    }
@app.get("/users/{username}")
def  get_name(username:str):
    return{"username": username,
    "message": f"Welcome back, {username}!"
    }

@app.get("/users/{username}/orders/{order_id}")
def get_order(username: str, order_id: int):
    return {
        "username": username,
        "order_id": order_id,
        "status": "Processing"
    }

@app.get("/prices/{price}")
def get_price(price: float):
    return {
        "price": price,
        "currency": "USD"
    }