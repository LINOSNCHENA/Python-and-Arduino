from fastapi import FastAPI
from typing import Union
from fastapi.middleware.cors import CORSMiddleware
import requests
from fastapi.responses import StreamingResponse
import subprocess
from fastapi import FastAPI, Response, Request
import asyncio

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.get("/")
async def root():
    return ("hello world")
    


# @app.get("/facts")
# async def read_item():
#     response = requests.get("https://cat-fact.herokuapp.com/facts")
#     array1 = response.json()[0]
#     print("---------------------|111|-----------------")
#     print(response)
#     print(array1)
#     return (array1)
    
async def generate_digits():
    for digit in range(10):
        yield f"data: {digit}\n\n"
        print("---------------------|22|-----------------")
        print(digit)
        await asyncio.sleep(1)

@app.get("/stream")
async def stream_digits():
    async def generate():
        async for digit in generate_digits():
            print("---------------------|33|-----------------")
            print(digit)
            yield digit

    return StreamingResponse(generate(), media_type="text/event-stream")

