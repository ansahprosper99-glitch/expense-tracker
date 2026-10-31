# expense_tracker.py

import csv
from datetime import datetime

FILE = "expenses.csv"

def add_expense():
    amount = float(input("Amount (GHS): "))
    category = input("Category (food, transport, data, etc): ")
    note = input("Note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, amount, category, note])
    print("Saved!")

def view_expenses():
    try:
        with open(FILE, "r") as f:
            reader = csv.reader(f)
            total = 0
            for row in reader:
                print(f"{row[0]} | {row[1]} GHS | {row[2]} - {row[3]}")
                total += float(row[1])
            print(f"\nTotal spent: {total} GHS")
    except FileNotFoundError:
        print("No expenses yet.")

# Main loop
while True:
    print("\n1. Add expense\n2. View all\n3. Exit")
    choice = input("> ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
