import requests
import os
from dotenv import load_dotenv

load_dotenv()
EXERCISEDB_API_KEY = os.environ.get('EXERCISEDB_API_KEY')
EXERCISEDB_ENDPOINT = 'https://exercisedb.p.rapidapi.com/exercises/target'

def get_metrics(height, weight):
    bmi = (weight / ((height / 100) ** 2))
    return {"bmi": bmi}

def fetch_exercises_by_target(target, limit=5):
    url = f"{EXERCISEDB_ENDPOINT}/{target}"  
    headers = {
        "X-RapidAPI-Key": EXERCISEDB_API_KEY,
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    params = {"limit": str(limit)}  
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return []  

def format_exercise_data(exercises):
    formatted_text = ""
    for exercise in exercises:
        formatted_text += f"• **Name**: {exercise['name']}\n  - **Equipment**: {exercise['equipment']}\n  - **Target**: {exercise['target']}\n - {exercise['gifUrl']}\n\n"
    return formatted_text

# Example usage
exercises_for_abs = fetch_exercises_by_target('quads')
# formatted_exercises = format_exercise_data(exercises_for_abs)
print(exercises_for_abs)
