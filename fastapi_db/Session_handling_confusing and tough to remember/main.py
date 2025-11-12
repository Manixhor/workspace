from fastapi import FastAPI, UploadFile,File
import pandas as pd
from PyPDF2 import PdfReader
import io 
app = FastAPI()

@app.post("/read")

async def read(file: UploadFile = File(...)):
    content = await file.read()
    name = file.filename.lower()

    if name.endswith((".xls",".xlsx")):
        df = pd.read_excel(io.BytesIO(content))
        return {"type ": "Excel","preview":df.head(3).to_dict()}
    

    




