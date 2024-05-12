# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()
# EXERCISEDB_API_KEY= os.environ.get('EXERCISEDB_API_KEY')
# EXERCISEDB_ENDPOINT = 'https://exercisedb.p.rapidapi.com/exercises'

# def get_metrics(height, weight):
#     bmi = (weight / ((height / 100) ** 2))
#     return {"bmi": bmi}

# def fetch_exercise(limit = 10):
#     headers = {"X-RapidAPI-Key": EXERCISEDB_API_KEY,
#             "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"}
#     params = {"limit":limit}
#     response = requests.get(EXERCISEDB_ENDPOINT, headers=headers, params=params)
#     return response.json()


# exercises = fetch_exercise()
# print(exercises)

