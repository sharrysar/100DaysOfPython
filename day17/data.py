import requests

resp = requests.get("https://opentdb.com/api.php?amount=10&category=12&difficulty=easy&type=boolean").json()
question_resp = resp['results']

question_data = []
for question in question_resp:
    data = {
        "question": question['question'],
        "correct_answer": question['correct_answer']
    }
    question_data.append(data)
