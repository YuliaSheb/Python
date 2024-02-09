import requests
from datetime import *


tablepoint = "https://api.sheety.co/d260081a1e3d731dca6b2543ac095ee7/копияMyWorkouts/workouts"
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": "63cfa564",
    "x-app-key": "3b0a2d931fe050b679dc28269c549405"
}


exerc = input("Tell me which exercises you did: ")


exercise_conf = {
 "query": exerc,
 "gender": "female",
 "weight_kg": 54.5,
 "height_cm": 155,
 "age": 20
}


response = requests.post(url=endpoint, json=exercise_conf, headers=headers)
data = response.json()
data_list = [value for (key, value) in data.items()]
data_list = data_list[0][0]
exercises = data_list["name"].title()
duration = data_list["duration_min"]
calories = data_list["nf_calories"]


today = datetime.now()
day = today.date()
day = day.strftime("%d/%m/%Y")
times = today.time()
times = times.strftime("%H:%M:%S")


parametr = {
    "workout": {
        "Date": day,
        "Time": times,
        "Exercise": exercises,
        "Duration": duration,
        "Calories": calories
        }
}


response_table = requests.post(url=tablepoint, json=parametr, auth=("Yulia", "Osd2016-2019"))


headers = {
    "Authorization": "Basic WXVsaWE6T3NkMjAxNi0yMDE5"
}
response_table = requests.post(
        url=tablepoint, json=parametr,
        headers=headers
    )
print(response_table.text)