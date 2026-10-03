from fastapi.responses import JSONResponse
from fastapi import Request

class PincodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode


class InvalidPinCodeError(Exception):
    def __init__(self, pincode: str, reason: str = "Invalid Pincode" ):
        self.pincode = pincode
        self.reason = reason

# above just created the class and initilaized variables, now its time to handle them by creating handlers

#handlers

async def pincode_not_found_handler(request:Request, exc:PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error" : "pincode_not_found",
            "message": f"No location exists for pincode {exc.pincode}",
            "pincode":exc.pincode
        }
    )

async def invalid_pincode_handler(request:Request, exc:InvalidPinCodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error" : "Invalid_Pincode",
            "message": f"pincode '{exc.pincode}' is invalid: {exc.reason}",
            "pincode":exc.pincode
        }
    )