from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hola_mundo():
    return {"message":"Hola Equipo"}

@app.get("/")
def root_endpoint():
    return {"message": "Bienvenido a mi API"}

@app.get("/suma")
def sumar(a:int, b:int):
    resultado = a +b
    return { "resultado": resultado}