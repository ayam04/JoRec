import openai
import os
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_KEY")
)

def evaluate_candidate(jd_text):
    if not jd_text:
        return "Job description text cannot be empty."

    messages = [
        {"role": "system", "content": "You are a friendly and professional career advisor."},
        {"role": "user", "content": (
            f"Please review the following job description and provide feedback, including a score out of 10 for each of the following criteria: Clarity, Inclusivity, Relevance, Structure, Company Branding, Performance Indicators, and Engagement. For each criterion, generate a two-line summary to justify the score.\n Additionally, offer friendly suggestions for improvement where needed. Job Description: {jd_text}"
        )}
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    job_text = "A data scientist from Bangalore with 5 years of experience in machine learning and deep learning."
    feedback = evaluate_candidate(job_text)
    print(feedback)
