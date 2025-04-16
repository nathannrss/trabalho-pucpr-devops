from fastapi import FastAPI
import random


app = FastAPI()


@app.get("/")
async def root():
    return {"massage": "Hello Word"} 


@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num-aleator": random.randint(0, 1000)}




#teste erro


# test_main.py

def test_erro_simulado():
    assert False, "Erro simulado para testar falha no pipeline"


