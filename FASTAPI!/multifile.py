from fastapi import FastAPI, UploadFile,File
import pandas as pd
from PyPDF2 import PdfReader 
import io 
app = FastAPI()

@app.post("/read-file")

async def read(file:UploadFile = File(...)):
    content = await file.read()
    name = file.filename.lower()
    if name.endswith((".xls",".xlsx")):
        df=pd.read_excel(io.BytesIO(content))
        return {"type":"Excel",
                "preview":df.head(3).to_dict()}
    elif name.endswith((".pdf")):
        reader = PdfReader(io.BytesIO(content))
        text  = "".join([p.extract_text() or "" for p in reader.pages[:2]])
        return {"type": "PDF","preview":text.strip()[:500]}
    return {"error": "Hey you ellumudra crct ga file"
    "upload cheyi"}

