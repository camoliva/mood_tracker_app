from mood_tracker import log_mood, save_mood_to_file, view_moods, get_user_choice

def main():
    while True:
        choice = get_user_choice()

        if choice == "1":
            entry = log_mood()
            save_mood_to_file(entry)
            print("Mood logged successfully!")
        elif choice == "2":
            print("\nMood History:")
            view_moods()
        elif choice == "3":
            print("Thanks for using the Mood tracker App, have a great day!")
            break
if __name__ == "__main__":
    main()
            