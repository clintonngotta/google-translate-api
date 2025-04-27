from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi import HTTPException


from models import TranslationModel


app = FastAPI()
@app.get("/")
def read_root():
    return "Welcome to the Google Translate API"


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

@app.post("/translate")
async def translate_text(
    data: TranslationModel
):    
    
    translated_text = f"Translated '{data.text}' to {data.target_lang}"
    return JSONResponse(content={"translated_text": translated_text})
