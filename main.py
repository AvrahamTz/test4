from fastapi import FastAPI
from pydantic import BaseModel
import func
import uvicorn


class Item(BaseModel):
    text: str
    offset: int | None = None
    mode: str

class Text(BaseModel):
    text:str
    

app = FastAPI()

@app.get("/test/")
def thetest():
    return { "msg": "hi from test" }

@app.get("/test/:name")
def savedname(name):
    with open("names.txt" "a") as f:
        f.write(name)
        return {"msg":"saved user"}
    
@app.post("/caesar/{Item}")
def caesar(Item):
    if Item["mode"] == "encrypt":
        encrypted_text =func.caesar_cipher(Item["text",Item["offset"]])
        return {"encrypted_text":encrypted_text}
    elif Item["mode"] == "decrypt":
        decrypted_text =func.reverse_caesar_cipher(Item["text",Item["offset"]])
        return {"decrypted_text":decrypted_text}

@app.get( "/fence/encryp/")
def get_text(text:str):
    encrypted_text = func.fence_cipher(text)
    return {"encrypted_text":encrypted_text}

@app.post("/fence/decrypt/{Text}")
def encypted(Text):
    decrypted = func.reverse_fence_cipher(Text["text"])
    return {"decrypted":decrypted}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000) 
    


