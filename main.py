from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi import HTTPException

from googletrans import Translator

from models import TranslationModel


app = FastAPI()
@app.get("/")
def read_root():
    return "Welcome to the Google Translate API"


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Custom exception handler for HTTP exceptions.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )
@app.exception_handler(Exception)

async def general_exception_handler(request: Request, exc: Exception):
    """
    Custom exception handler for general exceptions.
    """
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )

@app.post("/translate")
async def translate_text(
    data: TranslationModel
):    
    """
    Translate text to a target language.
    """
    
    translator = Translator(service_urls=['translate.googleapis.com'])
    try:
        translated_text = await  translator.translate(data.text, dest=data.target_lang)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if not translated_text:
        raise HTTPException(status_code=500, detail="Translation failed")
    print("translated_text:", translated_text)
    return JSONResponse(content={"translated_text": translated_text.text, "detected_source_language": translated_text.src, "target_language": translated_text.dest})
