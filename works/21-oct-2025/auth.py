from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

fake_user = {"username": "mani", "password": "1234"}


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == fake_user["username"] and form_data.password == fake_user["password"]:
        data = {"sub": form_data.username, "exp": datetime.utcnow() + timedelta(minutes=30)}
        token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": f"Hello {data['sub']}! Token works ✅"}
    except:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
