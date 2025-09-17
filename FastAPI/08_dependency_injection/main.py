from fastapi import FastAPI, Depends

app = FastAPI()

def token:
    return "my secrettoken"



@app.get("/protected")
def protected(token: str = Depends(get_token)):
    return {"token": token}