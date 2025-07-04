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