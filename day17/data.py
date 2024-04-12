import requests

resp = requests.get("https://opentdb.com/api.php?amount=10&type=boolean").json()
question_data = resp['results']
