import requests

URL = "https://opentdb.com/api.php"

params = {
    "amount": 10,
    "category": 9,
    "difficulty": "easy",
    "type": "boolean",
}
response = requests.get(url=URL, params=params)
response.raise_for_status()
data = response.json()

question_data = data["results"]

# question_data_formatted = [{
#     "category": q["category"],
#     "type": q["type"],
#     "difficulty": q["difficulty"],
#     "question": q["question"],
#     "correct_answer": q["correct_answer"],
#     "incorrect_answers": q["incorrect_answers"]
# }
#     for q in data["results"]]
