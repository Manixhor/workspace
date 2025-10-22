from fastapi import FastAPI, Depends

app = FastAPI()

# This is a helper (dependency)
def give_cookie():
    return " Here’s your cookie!"

# This is the main function (endpoint)
@app.get("/get-cookie")
def get_cookie(cookie: str = Depends(give_cookie)):
    return {"message": cookie}

@app.get("/get-cookie")
def get_cookie1(cookie: str = Depends(give_cookie)):
    return {"message": cookie}
