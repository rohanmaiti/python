"""
1. What is Async in Python?
Normally, Python runs code line-by-line.
If one line is slow (e.g., API request, file read, DB query), the whole program waits before moving on.
This is called blocking.

Async (asynchronous programming) lets Python start a task, then move on to other tasks while waiting for the first one to finish.
This is non-blocking.

2. Core Keywords
async — defines an asynchronous function (a coroutine).
await — pauses the coroutine until an awaited task finishes.
"""

#* Example: Synchronous vs Async
# Synchronous (Blocking)
import time 

# def task(name:int):
#     time.sleep(name)
#     print(f"Task {name} done !!")

# def main():
#     task(20) # will block the code here, untill this complets, code will not move forward
#     task(1)
#     task(3)

# main() # Takes ~24 seconds



#* Asyncronus (non-blocking)
import asyncio
async def task(name:int):
    await asyncio.sleep(name)  # Non-blocking wait
    print(f"Task {name} done")

async def main():
    await asyncio.gather(task(10), task(2), task(3))

asyncio.run(main()) # (runs in parallel)



#* Example of reallife code 
"""
from fastapi import FastAPI
import httpx

app = FastAPI()
client: httpx.AsyncClient = None


@app.on_event("startup")
async def startup_event():
    global client
    client = httpx.AsyncClient()


@app.on_event("shutdown")
async def shutdown_event():
    await client.aclose()


@app.get("/data")
async def get_data():
    response = await client.get("https://httpbin.org/get")
    return response.json()


@app.post("/send")
async def send_data():
    response = await client.post("https://httpbin.org/post", json={"msg": "hello"})
    return response.json()

"""