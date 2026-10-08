# Pincode Lookup API

A simple **FastAPI-based REST API** for looking up location details using Indian PIN codes. It supports single and bulk PIN code lookups with validation and custom exception handling.

## Features

- Single PIN code lookup
- Bulk PIN code lookup
- Pydantic validation
- Custom exception handling
- Swagger API documentation
- FastAPI REST endpoints

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## API Endpoints

- `GET /pincode/{code}` — Look up a single PIN code
- `POST /pincode/bulk` — Look up multiple PIN codes
- `GET /` — API welcome endpoint

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open the API documentation at:

`http://127.0.0.1:8000/docs`

## Project Structure

```text
pincode-lookup/
├── main.py
├── models.py
├── data.py
├── exceptions.py
└── requirements.txt
```