from fastapi import FastAPI, Query
from functions import evaluate_candidate
import uvicorn

app = FastAPI()

@app.post("/suggest-candidate")
async def suggest_candidate(resume_text: str = Query(...)):
    return evaluate_candidate(resume_text)

if __name__ == "__main__":
    uvicorn.run(app, host=8080)