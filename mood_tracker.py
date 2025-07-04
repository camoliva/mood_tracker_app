print ("Welcome to the Mood Tracker!")

def validate_rating(rating):
    return 1 <= rating <= 5

from datetime import datetime

def log_mood():
    rating = int(input("How are you feeling today? (1-5): "))
    note = input("Any comments? ")
    date = datetime.now().strftime("%Y-%m-%d")

    return {
        "rating": rating,
        "comment": note,
        "date": date   
    }

import json
import os

def save_mood_to_file(entry, filename="moods.json"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    data.append(entry)

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def view_moods(filename="moods.json"):
    try:
        with open(filename, "r") as file:
            moods = json.load(file)
    except (FileNotFoundError, json.JSONDecoderError):
        moods = []

    for entry in moods:
        print(f"{entry[ ' date' ]}: Rating {entry[ 'rating' ]} - {entry[ ' note ' ]}")
    return moods
       