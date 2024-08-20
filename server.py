from fastapi import FastAPI, Query
from functions import evaluate_candidate
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class JDAnalyzerRequest(BaseModel):
    resume_text: str

@app.post("/suggest-jd")
async def suggest_candidate(jd_reqst: JDAnalyzerRequest):
    resume_text = jd_reqst.resume_text
    response = {'output': evaluate_candidate(resume_text)}
    return response

if __name__ == "__main__":
    uvicorn.run(app, host=8080)