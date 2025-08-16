from fastapi import FastAPI

app = FastAPI(title = "Deep and Ben's API")

@app.get("/deep")
def read():
    return {"message": "Hello from Deep!"}

@app.get("/ben")
def read():
    return {"message": "Hello from Ben!"}