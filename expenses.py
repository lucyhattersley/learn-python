# Initialize a dictionary to store expenses by category
expenses = {}

# Continue adding expenses until the user decides to stop
adding = True
while adding:
    # Ask for the category
    category = input("Enter the category (Food, Transport, Entertainment): ").capitalize()

    # Validate category input
    if category not in ['Food', 'Transport', 'Entertainment']:
        print("Invalid category. Please enter a valid category.")
        continue

    # Ask for the expense amount
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Please enter a valid amount in numbers.")
        continue

    # If the category already exists in the dictionary, add to it
    if category in expenses:
        expenses[category].append(amount)
    else:
        # Otherwise, create a new list in the dictionary for this category
        expenses[category] = [amount]

    # Ask if the user wants to continue
    continue_input = input("Do you want to add another expense? (yes/no): ").lower()
    if continue_input != 'yes':
        adding = False

# Calculate total expenses by category and overall
print("\nExpenses Summary:")
total_expenses = 0
for category, amounts in expenses.items():
    category_total = sum(amounts)
    print(f"{category}: ${category_total:.2f}")
    total_expenses += category_total

print(f"Total Spent: ${total_expenses:.2f}")

