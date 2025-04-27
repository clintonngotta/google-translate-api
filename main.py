from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request


app = FastAPI()
@app.get("/")
def read_root():
    return "Welcome to the Google Translate API"


@app.post("/translate")
async def translate_text(
    text: str,
    target_lang: str,
    request: Request
):
    
    translated_text = f"Translated '{text}' to {target_lang}"
    return JSONResponse(content={"translated_text": translated_text})
