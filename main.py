from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{
        "message":"Pincode api LookUp project"
    }