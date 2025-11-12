from fastapi import FastAPI,HTTPException,Cookie,Response
import uuid
from typing import Optional
from datetime import datetime,timedelta
app = FastAPI()


couname = "admin"
copass = "admin"
sessions = {}
time= 10


@app.post("/login")

def login(uname:str,pa:str,res:Response):
    if couname == uname and pa == copass:
        sid = str(uuid.uuid4())
        cur_time = datetime.now() 
        exp_time = cur_time + timedelta(seconds=time)
        print(cur_time)
        print(exp_time)
        sessions[sid] = {"username": uname,"exp_time":exp_time}
        res.set_cookie(key="sid",value=sid,httponly=True,max_age=time)
        return {"msg":"Login Success !"}

    
    else:
        raise HTTPException(status_code=401,detail="Invalid Credentials")

@app.get("/home")

def home(sid:Optional[str]=Cookie(None)):
    if sid is None or sid not in sessions:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    session_data = sessions[sid]
    if session_data["exp_time"]<datetime.now():
        sessions.pop(sid)

    return {"data":sessions}