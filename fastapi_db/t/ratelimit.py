from fastapi import FastAPI,HTTPException,Request
app = FastAPI()

req_counter = {}

max_req = 5

@app.get("/date")
def get_data(request:Request):
    client_ip = request.client.host
    req_counter[client_ip] = req_counter.get(client_ip)    

