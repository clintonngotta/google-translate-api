# Google Translate API

This is a simple FastAPI-based project that provides a RESTful API for translating text using the Google Translate service. It also includes endpoints for health checks and retrieving supported languages.

## Features

- **Health Check**: Verify the API is running.
- **Translate Text**: Translate text to a specified target language.
- **Supported Languages**: Retrieve a list of supported languages for translation.

## Dependencies

This project uses the following Python libraries:

- fastapi
- uvicorn
- googletrans
- pydantic
- And others listed in requirements.txt.

## Endpoints

### Health Check

- **GET** `/health`
  - Returns the status of the API.

### Root

- **GET** `/`
  - Returns a welcome message.

### Translate Text

- **POST** `/translate`
  - Request Body:
    ```json
    {
    	"text": "Hello, world!",
    	"target_lang": "fr"
    }
    ```
  - Response:
    ```json
    {
    	"translated_text": "Bonjour, le monde!",
    	"detected_source_language": "en",
    	"target_language": "fr"
    }
    ```

### Supported Languages

- **GET** `/languages`
  - Returns a list of supported languages.

## Installation & Project Setup

1.  Clone the repository:

    ```bash
    git clone <repository-url>
    cd google-translate-api

    ```

2.  Create and activate a virtual environment:

    ```bash
    python -m venv venv
        source venv/bin/activate

    ```

3.  Install Dependencies:

    ```bash
    pip install -r requirements.txt

    ```

4.  Run the App

    ```bash
    uvicorn main:app --reload
    ```

    option two:

    ```bash
    fastapi dev
    ```
