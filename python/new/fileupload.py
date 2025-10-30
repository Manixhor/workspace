from fastapi import FastAPI,File,UploadFile
from typing import List 


app = FastAPI()


@app.post("/singlefile")
async def file_upload(files:List[UploadFile]=File(...)):
    result = []
    for file in files:

        content = await file.read()

        try:
            text_p=content.decode("utf-8") [:200]
        except UnicodeDecodeError :
            text_p = "cannot be previewed as text"
        result.append ( {
            "File name":  file.filename,
            "content_type": file.content_type,
            "size of the file" : len(content),
            "content in the file ":  text_p
        })
    return result 



