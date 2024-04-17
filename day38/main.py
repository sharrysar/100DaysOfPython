import requests
from datetime import datetime

def find_workout(query):
    APP_ID = 'a2fcce48'
    APP_KEY = '8ca0277910c27e2f2dd77ba0f64f3010'
    headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
    }    
    query = {'query': query}
    url = f'https://trackapi.nutritionix.com/v2/natural/exercise'

    try:
        resp = requests.post(url=url, headers=headers, json=query)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error looking up exercise: {e}")
    else:
        return resp.json()

def update_sheet(name, duration, calories):
    day = datetime.now().strftime("%d/%M/%Y")
    time = datetime.now().strftime("%X")
    url = 'https://api.sheety.co/frostytest/workoutTracking/workouts'
    data = {
        "workout": {
            "date": day,
            "time": time,
            "exercise": name,
            "duration": duration,
            "calories": calories
        }
    }

    resp = requests.post(url=url, json=data)
    return resp.status_code


exercise = input("What exercises did you do today?: ")
nutritionix_response = find_workout(exercise)

if nutritionix_response:
    duration = nutritionix_response['exercises'][0]['duration_min']
    name = nutritionix_response['exercises'][0]['name']
    calories = nutritionix_response['exercises'][0]['nf_calories']
    
    sheety_resp = update_sheet(name,duration,calories)

    if sheety_resp == 200:
        print("Sheet updated successfully!")
    else:
        print("Something went wrong.")
else:
    print("An error occured")
