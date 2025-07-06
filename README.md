# WELCOME TO THE MOOD TRACKER APP

A terminal based mood tracking app built in Python. 

This project began as a way to practice version control and test driven development, but it quickly grew into something more meaningful. I wanted to create a simple tool that encourages daily reflection and mental check ins without the complexity of larger apps. Logging your mood even in a small way can offer surprising insight over time and building this app reminded me how powerful even the simplest software can be.

## Features

- Log your mood with a rating from 1-5
- Optional personal note for each entry
- Date added automatically
- View full mood history
- Summary of average mood
- Personalised welcome message (saved across sessions)
- Styled CLI using the `rich` library
- Error handling for empty files or bad inputs
- Built using a Test-Driven Development
- Includes unit tests


## Technologies Used

- Python 3.12
- `unittest` (Python’s built-in test module)
- `rich` (for terminal formatting and colored output)


## Getting Started

## Clone the repository:

git clone https://github.com/camoliva/mood_tracker_app.git
cd mood_tracker_app

## Create and activate a virtual environment 

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
### OR
venv\Scripts\activate  # Windows

## Install required packages:

pip install -r requirements.txt

## Run the app

python main.py

## Security & Dependencies

This app uses only one third party dependency:

rich - License: MIT
https://github.com/Textualize/rich

Security impact:
The rich library is used solely for formatting terminal output. It does not process user data, run external scripts, or affect system-level operations. Its use presents minimal risk in the context of this CLI tool.

## License

This project is licensed under the MIT License see the LICENSE file for details: 

## Author

Cameron Oliva
Built for: ISK1001 Industry Skills I
Assessment 2: Version Control & Software Testing Reflection