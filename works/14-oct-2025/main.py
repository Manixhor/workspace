from fastapi import FastAPI

app = FastAPI()

# Step 1: When user logs in, give them a token (like a ticket)
@app.post("/login")
def login(username: str, password: str):
    if username == "admin" and password == "123":
        return {"token": "ABC123"}  
    else:
        return {"message": "Wrong username or password"}

# Step 2: User shows token to enter secret room
@app.get("/secret-room")
def secret_room(token: str):
    if token == "ABC123":  
        return {"message": "Welcome to the secret room!"}
    else:
        return {"message": "Access denied! No valid token."}
