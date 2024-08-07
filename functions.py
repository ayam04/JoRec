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
    {"role": "user", "content": f"Please evaluate and improve the following job description based on the given criteria: Clarity, Inclusivity, Relevance, Structure, Company Branding, Performance Indicators, and Engagement. Additionally, provide a detailed breakdown of key components for an ideal job description:\n\n{jd_text}\n\nThe detailed breakdown includes Job Title, Job Summary, Key Responsibilities, Required Qualifications, Preferred Qualifications, Work Environment and Physical Demands, Company Overview, Compensation and Benefits, Location, and Application Process."}
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
    job_text = "A data scienctist from bangalore with 5 years of experience in machine learning and deep learning."
    feedback = evaluate_candidate(job_text)
    print(feedback)
