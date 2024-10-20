from fastapi import FastAPI
# UH WHAT THE SIGMA !!!???
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/hi")
async def hi():
    return {"message": f"hi there"}
