import csv
from datetime import date
from pathlib import Path

# Go from src/ back to project folder, then into data/
DATA_FILE = Path(__file__).parent.parent / "data" / "workouts.csv"

# Make sure data folder exists
DATA_FILE.parent.mkdir(exist_ok=True)

# Create CSV with headers if it doesn't exist yet
if not DATA_FILE.exists():
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "exercise", "set", "reps", "weight"])

exercise = input("Exercise name: ")
weight = input("Weight used: ")
sets = int(input("How many sets?: "))

rows = []

for set_number in range(1, sets + 1):
    reps = input(f"Reps for set {set_number}: ")

    rows.append([
        date.today(),
        exercise,
        set_number,
        reps,
        weight
    ])

with open(DATA_FILE, "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)

print("Workout saved.")
