import json
import os

def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def add_income(data):
    income = float(input("Enter your total monthly income: "))
    data['income'] = income
    return data

def add_expense(data):
    if 'expenses' not in data:
        data['expenses'] = {}
    
    category = input("Enter the expense category (Housing, Utilities, Groceries, Transportation, Entertainment, Other): ")
    amount = float(input("Enter the expense amount: "))
    description = input("Enter a brief description of the expense: ")
    
    if category in data['expenses']:
        data['expenses'][category].append({'amount': amount, 'description': description})
    else:
        data['expenses'][category] = [{'amount': amount, 'description': description}]
    
    return data

def monthly_summary(data):
    total_expenses = 0
    income = data.get('income', 0)
    expenses = data.get('expenses', {})

    print("\nMonthly Summary:")
    print(f"Total Income: ${income:.2f}")
    
    for category, entries in expenses.items():
        category_total = sum(item['amount'] for item in entries)
        total_expenses += category_total
        print(f"{category}: ${category_total:.2f} ({(category_total / income * 100):.2f}%)")

    net_savings = income - total_expenses
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Savings: ${net_savings:.2f}")

def main():
    data_file = 'budget_data.json'
    budget_data = load_data(data_file)

    while True:
        print("\n--- Home Budget Tracker Menu ---")
        print("1. Add Monthly Income")
        print("2. Add Expense")
        print("3. Show Monthly Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            budget_data = add_income(budget_data)
        elif choice == '2':
            budget_data = add_expense(budget_data)
        elif choice == '3':
            monthly_summary(budget_data)
        elif choice == '4':
            save_data(budget_data, data_file)
            print("Data saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
