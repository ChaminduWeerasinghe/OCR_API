#run server - uvicorn main:app --port 8000

from fastapi.responses import FileResponse
from fastapi import FastAPI,UploadFile,File
from service import recognizer


app = FastAPI()

@app.post('/convert/')
async def converter(file: UploadFile = File(...)):

    filepath,filename = recognizer(file=file)
    return FileResponse(filepath,media_type='application/octet-stream',filename=filename)




        


    # try:
    #     return_result = "<html><body><p>\n"
    #     reader = easyocr.Reader(['en'],gpu=True)
    #     result = reader.readtext(filepath)
    #     for line in result:
    #         return_result += line[1]+'\n'

    #     return_result += '</p></html></body>'

    # except:
    #     pass

    
    

