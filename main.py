from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"massage": "Hello Word"} 


@app.get("/teste")
async def funcaoteste():
    return {"teste": "deu certo"}

'''teste para ver se está tudo certo '''