import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

def evaluate_candidate(jd_text):
    if not jd_text:
        return "Job description text cannot be empty."

    messages = [
        {"role": "system", "content": "You are a career advisor."},
        {"role": "user", "content": f"Please evaluate the following Candidate for clarity, completeness, and quality:\n\n{jd_text}\n\nProvide feedback and suggestions for improvement. Also, suggest a suitable career path, summarize their weaknesses, and recommend improvements along with the recommended career path."}
    ]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=1
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    resume_text = "A data scienctist from bangalore with 5 years of experience in machine learning and deep learning."
    feedback = evaluate_candidate(resume_text)
    print(feedback)
