from fastapi import FastAPI, HTTPException

app = FastAPI()

items_db = {}

@app.get("/items")
def get_items():
    return items_db

@app.post("/items")
def create_item(item: dict):
    item_id = max(items_db.keys(), default=0) + 1
    items_db[item_id] = item
    return {"created": {"item_id": item_id, "item": item}}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item
    return {"updated": {"item_id": item_id, "item": item}}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]
    return {"deleted": item_id}
