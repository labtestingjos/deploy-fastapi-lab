from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hola_mundo():
    return {"message":"Hola Equipo"}