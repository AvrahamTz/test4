from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    text: str
    offset: int | None = None
    mode: str
    

app = FastAPI()

@app.get("/test/")
def thetest():
    return { "msg": "hi from test" }

@app.get("/test/:name")
def savedname(name):
    with open("names.txt" "a") as f:
        f.write(name)
        return {"msg":"saved user"}

