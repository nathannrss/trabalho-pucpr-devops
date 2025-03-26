from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
async def root():
    return {"massage": "Hello Word"} 


@app.get("/funcaoteste1")
async def funcaoteste():
    return {"teste": "deu certo"}

