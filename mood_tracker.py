print ("Hello and Welcome to the Mood Tracker App!")

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
       
def get_user_choice():
    while True:
        print("\nWhat would you like to do?")
        print("1. Log a mood")
        print("2. View mood history")
        print("3. Exit app")

        choice = input("Enter your choice (1-3): ").strip()

        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid input. Please choose 1,2 or 3.")