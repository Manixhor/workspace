from fastapi import FastAPI


app = FastAPI()


@app.get('/home')

def hello():
	return "hello world"
	
@app.get()