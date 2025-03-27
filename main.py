from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"massage": "Hello Word"} 

#teste para ver se está ok. obrigado
@app.get("/teste31")
async def funcaoteste():
    return {"teste": "deu certo"}

'''teste para ver se está tudo certo '''