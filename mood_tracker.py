from rich import print

def validate_rating(rating):
    return 1 <= rating <= 5

from datetime import datetime

def log_mood():
    print("[bold cyan]How are you feeling today? (1–5):[/bold cyan]")
    rating = int(input(">> "))

    print("[bold magenta]Why do you feel this way?[/bold magenta]")
    note = input(">> ")

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
        print("-----[bold cyan] What would you like to do?[/bold cyan]-----")
        print("[bold blue]1.[/bold blue] [green]Log a mood[/green]")
        print("[bold blue]2.[/bold blue] [purple]View mood history[/purple]")
        print("[bold blue]3.[/bold blue] [orange1]View mood summary[/orange1]")
        print("[bold blue]4.[/bold blue] [red]Exit app[/red]")

        print("[bold yellow]Enter your choice (1–4):[/bold yellow]")
        choice = input(">> ").strip()

        if choice in ["1", "2", "3", "4"]:
            return choice
        else:
            print("[bold red] Invalid input. Please choose 1,2,3 or 4.[/bold red]")

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
        }   
    
    ratings = [entry.get("rating", 0) for entry in moods]
    average = sum(ratings) / len(ratings)  

    print("\n[bold cyan]Mood Summary:[/bold cyan]")
    print(f"[green]Total entries:[/green] {len(ratings)}")
    print(f"[orange1]Average rating:[/orange1] {average:.1f}")

    return {
        "total": len(ratings),
        "average": average,
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