from fastapi import FastAPI

app = FastAPI()

@app.post("/interact_with_agent")
def interact_with_agent():
    pass