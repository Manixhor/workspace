from fastapi import FastAPI,HTTPException,Request

app = FastAPI()

req_counter = {}
max_req = 5
@app.get("/data")

def get_data(request:Request):
    client_ip = request.client.host #to get the client ip address
    req_counter[client_ip] = req_counter.get(client_ip,0) + 1 #this add the times we login
    print(req_counter)
    if req_counter[client_ip]>max_req:
        raise HTTPException(status_code=429,detail="Too many req.")
    return {"message":f"request{req_counter[client_ip]} successful"}