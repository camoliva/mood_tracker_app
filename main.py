from rich import print
from mood_tracker import (
    get_user_name,
    log_mood,
    save_mood_to_file,
    view_moods,
    get_user_choice,
    show_mood_summary,
)

def main():
    name = get_user_name()
    print(f"Hello and Welcome {name}!")
    print("This is your personal mood tracker.\n")

    while True:
        choice = get_user_choice()

        if choice == "1":
            print("\n Lets start")
            entry = log_mood()
            save_mood_to_file(entry)
            print("[bold green]Mood logged successfully![/bold green]")

        elif choice == "2":
            print("\nMood History:")
            moods = view_moods()
            if not moods:
                print("No mood history found, please try logging one first.")

        elif choice == "3":
            print("Heres how you have been feeling lately.")
            show_mood_summary()

        elif choice == "4":
            print(f"[bold purple]Thanks for using the Mood Tracker App, {name}! Have a great day![/bold purple]")
            break

if __name__ == "__main__":
    main()
            