import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_key = os.environ.get("GROQ_API_KEY")
if not groq_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Add it to your .env.")

client = Groq(api_key=groq_key)

def generate_itinerary(source, destination, start_date, end_date, no_of_days):
    system_prompt = (
        "You are an expert travel planner specializing in Indian and international trips. "
        "Always give detailed, practical, budget-friendly itineraries. "
        "Tone: friendly, informative, concise. Use INR for costs; include real attractions and dining options."
    )
    user_prompt = (
        f"Generate a personalized {no_of_days}-day trip itinerary "
        f"from {source} to {destination} between {start_date} and {end_date}. "
        f"Include sightseeing, food recommendations, transport suggestions, "
        f"and an optimum budget per day in INR."
    )

    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # or a lighter model like "llama-3.2-11b-text"
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
        max_tokens=800,
    )
    return resp.choices[0].message.content