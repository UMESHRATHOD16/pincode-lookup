from pydantic import BaseModel, field_validator

class pinCodeValidator(BaseModel):
    pincode:str

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("pincode is not valid")
        return value

class LocationResponse(BaseModel):
    pincode :str
    city :str
    state :str
    district :str

class BulkRequest(BaseModel):
    pincodes : list[str]

    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls,values):
        if len(values) == 0:
            raise ValueError("At least one pincode is required!")
        if len(values) > 20:
            raise ValueError("Maximum of 20 pincodes allowed per request")

        for code in values:
            if len(code) != 6 or not code.isdigit():
                        raise ValueError("Each pincode must be exactly of 6 digit")
        return values

class BulkLocationResponse(BaseModel):
    status :str = "success"
    found :int
    not_found :int
    results :list[LocationResponse]
    missings :list[str]