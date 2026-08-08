from fastapi import FastAPI

app = FastAPI()

products = [
    {
        "id": 1,
        "name": "Wireless Headphones",
        "category": "electronics",
        "price": 999.0,
        "in_stock": True,
        "tags": ["wireless", "audio", "bluetooth"]
    },
    {
        "id": 2,
        "name": "Python Notebook",
        "category": "books",
        "price": 299.0,
        "in_stock": True,
        "tags": ["python", "programming", "learning"]
    },
    {
        "id": 3,
        "name": "Mechanical Keyboard",
        "category": "electronics",
        "price": 1499.0,
        "in_stock": False,
        "tags": ["keyboard", "gaming", "mechanical"]
    },
    {
        "id": 4,
        "name": "Coffee Mug",
        "category": "home",
        "price": 249.0,
        "in_stock": True,
        "tags": ["coffee", "kitchen", "ceramic"]
    },
    {
        "id": 5,
        "name": "USB-C Cable",
        "category": "electronics",
        "price": 399.0,
        "in_stock": True,
        "tags": ["usb", "charging", "cable"]
    }
]


@app.get("/")
def home():
    return {"message": "Welcome to Lakshmi's Mini Shop!"}

@app.get("/products/")
def get_products(
    category: str | None = None,
    skip: int = 0,
    limit: int = 10
):
    filtered_products = products

    if category:
        filtered_products = [
            product for product in filtered_products
            if product["category"] == category
        ]

    return filtered_products[skip:skip + limit]


@app.get("/search/")
def search_products(q: str):
    results = [
        product for product in products
        if q.lower() in product["name"].lower()
    ]

    return {
        "query": q,
        "results": results
    }
@app.get("/products/{product_id}")
def get_product(product_id: int, details: bool = False):
    for product in products:
        if product["id"] == product_id:
            if details:
                return product

            return {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"]
            }

    return {"message": "Product not found"}