import csv
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Function to add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
    if date == "":
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    # Append expense to CSV
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    print("\nAll Expenses:")
    print("Date       | Category   | Amount | Description")
    print("-"*50)
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()

# Function to view summary by category
def view_summary():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.")
        return

    summary = {}
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category = row[1]
            amount = float(row[2])
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    print("\nExpense Summary by Category:")
    print("-"*30)
    total = 0
    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")
        total += amount
    print(f"Total Expenses: ₹{total}\n")

# Main menu
def main():
    # If CSV file doesn't exist, create with headers
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

    while True:
        print("===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
