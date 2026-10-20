"""
order-service: a tiny FastAPI service for IT 390 Week 2.

You do not need to modify this file. Your job this week is to write the
Dockerfile that packages it into a container image. See the assignment
handout on D2L for the full instructions.
"""
from fastapi import FastAPI

app = FastAPI(title="order-service")

# A small in-memory list of orders so the service has something to return.
ORDERS = [
    {"id": 1, "item": "widget", "qty": 3},
    {"id": 2, "item": "gadget", "qty": 1},
]


@app.get("/health")
def health():
    """Liveness check. Your container is working if this returns ok."""
    return {"status": "ok"}


@app.get("/orders")
def list_orders():
    """Return all orders."""
    return {"orders": ORDERS}


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    """Return a single order by id, or a 404-style message if missing."""
    for order in ORDERS:
        if order["id"] == order_id:
            return order
    return {"error": "order not found", "id": order_id}
