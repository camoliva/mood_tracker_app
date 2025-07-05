print ("Hello and Welcome to the Mood Tracker App!")

def validate_rating(rating):
    return 1 <= rating <= 5

from datetime import datetime

def log_mood():
    rating = int(input("How are you feeling today? (1-5): "))
    note = input("Any comments? ") or ""
    date = datetime.now().strftime("%Y-%m-%d")

    return {
        "rating": rating,
        "note": note,
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
    except (FileNotFoundError, json.JSONDecodeError):

        moods = []

    for entry in moods:
        print(f"{entry.get('date', 'N/A')}: Rating {entry.get('rating', 'N/A')} - {entry.get('note', '')}")
    return moods
       
def get_user_choice():
    while True:
        print("\nWhat would you like to do?")
        print("1. Log a mood")
        print("2. View mood history")
        print("3. Show mood summary")
        print("4. Exit app")

        choice = input("Enter your choice (1-4): ").strip()

        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("Invalid input. Please choose 1,2,3 or 4.")

def show_mood_summary(filename="moods.json"):
    try:
        with open(filename, "r") as file:
            moods = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        moods = []

    if not moods:
        return {
            "total": 0,
            "average": 0,
            "highest": None,
            "lowest": None
        }   
    
    ratings = [entry.get("rating", 0) for entry in moods]
    average = sum(ratings) / len(ratings)
    highest = max(ratings)
    lowest = min(ratings)   

    print("\nMood Summary:")
    print(f"Total entries: {len(ratings)}")
    print(f"Average rating: {average:.1f}")
    print(f"Best day: {highest}")
    print(f"Worst day: {lowest}")

    return {
        "total": len(ratings),
        "average": average,
        "highest": highest,
        "lowest": lowest
    }

def get_user_name(filename="user.json"):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f).get("name", "user")
    else:
        name = input( "Hello! What is your name? ")
        with open(filename, "w") as f:
            json.dump({"name": name}, f)
        return name