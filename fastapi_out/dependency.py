from fastapi import FastAPI, Depends
from datetime import datetime

app = FastAPI()
"""Functional"""
# def db():
#     return {"db connected"}
# @app.get("/display")
# async def dis(a=Depends(db)):
#     return {"message":"This is from display endpoint","db_staus":a}
"""Class level dependency"""
# class User:
#     def __init__(self):
#         self.name = "Mani"
#         self.age = "22"

# def getuser():
#     return User()

# @app.get("/user_data")
# async def dis(a:User=Depends(getuser)):
#     return {"name":a.name,"age":a.age}

"""Global level"""
# def veriy(token:str="123"):
#     if token != "123":
#         raise Exception("Invalid TOken")
#     return True
# @app.get("/display")
# async def dis():
#     return {"message":"Hello"}
"""sub level dependency"""
# def grand():
#     return {"Message": "grand accessed"}
# def parent(a=Depends(grand)):
#     return {f"Message:From Parent {a}"}
# @app.get("/display")
# def child(b:str=Depends(parent)):
#     return {"Message":b}

"""Yeild level dependency """
def lib():
    print("Book taken from library",datetime.now())

    book = "Fastapi book"
    yield book 

    print("book returned to library",datetime.now())

@app.get("/yield")
def access(a:str=Depends(lib)):
    return {f"message{datetime.now()}":f"reading {a}"}