from fastapi import FastAPI
from pydantic import BaseModel
import redis
import os

app = FastAPI()

try:
    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = int(os.getenv("REDIS_PORT", 6379))

    r = redis.Redis(host=redis_host,port=redis_port, db=0, decode_responses=True)
except Exception as e:
    print(f"Exception in redis {str(e)}")

class CounterResponse(BaseModel):
    counter: str
    count: int

@app.get("/", response_model=CounterResponse)
def read_root():
    key = "page_views"
    count = r.incr(key) # increment page views by 1
    return CounterResponse(counter= key, count=count)