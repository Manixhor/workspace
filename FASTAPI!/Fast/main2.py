from fastapi import FastAPI,Form,File,UploadFile
from typing import List
app = FastAPI()

# @app.post("/feedback")

# def feed(name:str = Form(...),email:str=Form(...),
#          rating:int = Form(le=5,ge=1)):
#     return {
#         "status": "feedback received",
#         "name" : name,
#         "rating": rating
#     }

#file upload 

@app.post("/file_upload")

async def file_upload(files:List[UploadFile]=File(...)):
    result = []
    for file in files:

        content = await file.read()
        try:
            text_p = content.decode("utf-8")[:200]
        except UnicodeDecodeError:
            text_p = "cannot be preview the text"

    result.append ({
        "File Name" : file.filename,
        "content_type": file.content_type,
        "file size in bytes": len(content),
        "text":text_p

        })
    return result 
















