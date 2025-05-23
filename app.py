from fastapi import FastAPI, Query
import uvicorn

app = FastAPI()

@app.get("/calc/")
def calculate(action: str = Query("+"), num1: int = Query(1), num2: int = Query(1)):
    if action == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    elif action == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    else:
        return "An error occured"
    

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
