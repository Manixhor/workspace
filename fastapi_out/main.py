from fastapi import FastAPI,HTTPException,Cookie,Response
import uuid
from datetime import datetime,timedelta
app = FastAPI()
from typing import Optional
#cookies -> small piece of information

coruname = "admin"
corpass = "admin"

sessions = {}
time = 10
@app.post("/login")
def login(uname:str,pa:str,res:Response):
    if coruname == uname and corpass == pa:
        sid = str(uuid.uuid4())
        cur_time = datetime.now()
        exp_time = cur_time +timedelta(seconds=time)
        print("current time",cur_time)
        print("exp time",exp_time)
        sessions[sid] = {"username":uname,"exp_time":exp_time}
        res.set_cookie(key="sid",value=sid,httponly=True,max_age=time)
        return {"Message":"Login Success"}

    else:
        raise HTTPException(status_code = 401,detail
                            ="Invalid credential")
      
    

@app.get("/home")
def home(sid:Optional[str]=Cookie(None)):
    if sid is None or sid not in sessions:
         raise HTTPException(status_code = 401,detail
                            ="Not autheticated")
    session_data = sessions[sid]
    if session_data["exp_time"]< datetime.now():
        sessions.pop(sid)
    return {"data":sessions}  

