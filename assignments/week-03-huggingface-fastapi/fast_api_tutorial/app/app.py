from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import pipeline


app = FastAPI()
pipe = pipeline('translation', './model/t5-small')# complete this line with the code to load the pipeline from the local file

class TextToTranslate(BaseModel):
    input_text: str

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/translation")
def translation(text_to_translate: TextToTranslate):
    return {"translation": pipe(text_to_translate.input_text)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)