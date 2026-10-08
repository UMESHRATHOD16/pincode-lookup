from fastapi import FastAPI
from exceptions import (
    pincode_not_found_handler,
    PincodeNotFoundError,
    invalid_pincode_handler,
    InvalidPinCodeError
)

from data import pincode_db

from models import(
    LocationResponse,
    BulkLocationResponse,
    BulkRequest
)

app = FastAPI(
    title="pincode lookup API",
    description="autofill city info with pincode during checkout"
)


# register custom exception handler
app.add_exception_handler(InvalidPinCodeError,invalid_pincode_handler)
app.add_exception_handler(PincodeNotFoundError,pincode_not_found_handler)

@app.get("/")
def root():
    return{
        "message":"Pincode api LookUp project"
    }

@app.get("/pincode/{code}",response_model=LocationResponse)
def lookup_pincode(code:str):
    if len(code) !=6 or not code.isdigit():
        raise InvalidPinCodeError(code, "Must be exactly 6 digits")

    if code not in pincode_db:
        raise PincodeNotFoundError(code)

    return pincode_db[code]

@app.post("/pincode/bulk",response_model=BulkLocationResponse)
def bulk_lookup(request: BulkRequest):
    result = []
    missing = []

    for code in request.pincodes:
        if code in pincode_db:
            result.append(pincode_db[code])
        else:
            missing.append(code)

    return BulkLocationResponse(
        found=len(result),
        not_found=len(missing),
        results=result,
        missings=missing
    )