import sqlite3
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel 


app = FastAPI()

conn= sqlite3.connect("test.db",check_same_thread=False)

cursor = conn.cursor()
# cursor.execute('''
#     create table if not exists items(
#             item_id integer primary key autoincrement,
#             name text not null, 
#             des text   
               
#                )


#             ''')
# conn.commit()

class item(BaseModel):
    name : str 
    des : str 

@app.post("/items/adding")
def create_item(i:item):
    try:
        cursor.execute("Insert into items(name,des) values(?,?)",(i.name,i.des))
        conn.commit()
        return {"message":"Items stored successfuly.."}
    except Exception as e:
        return HTTPException(status_code=400,detail=
                             f"unable to store {e}")

@app.get("/items/read")

def read():
    try:
        cursor.execute("Select * from items")
        rows = cursor.fetchall()
        return [{"id":r[0],"name":r[1],"des":r[2]} for r in rows]
    except Exception as e:
        return HTTPException(status_code = 400,detail = f"unable to Read {e}")
    
