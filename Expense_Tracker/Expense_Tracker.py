from Expense_Class import Expense

# Initializing the main function

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "./Expense_Tracker/Expense.csv"
    Budget = 3000
    
    # Get user input for expense
    expense = get_user_expense()
    # Write their expense to file
    write_expense_to_file(expense, expense_file_path)
    # Read and summarize expenses
    read_and_summarize_expenses(expense_file_path, Budget)

# Function for the user input
def get_user_expense():
    expense_name = input("Enter expense: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"Expense: {expense_name}, Amount: ${expense_amount}")
    print(f"Getting User Expense")

    # Defining a tuple for categories

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

    # while loop for Category selection

    while True:
        print("select a category: ")
        for i, category in enumerate(expense_categories, start=1):
            print(f"{i}.{category}")

        # range and input type declaration

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Select the category number {value_range}: ")) - 1

        # range checker

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
                )
            return new_expense
        else:
            print("Invalid selection. Please try again.")

# Saving user input to file
    
def write_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User expense: {expense} to Expenses")

    # Implementing file writing logic
    
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")



def read_and_summarize_expenses(expense_file_path, Budget):
    print(f"Summarizing User Expenses")

    # Expense list to store the results
    expenses:list[Expense] = []
    # Implementing file reading logic

    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
           
            expense_name,  expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name, category=expense_category, amount=float(expense_amount)
            )
            # print(line_expense)
            expenses.append(line_expense)
        # print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
        
        # Summing up the total

    print("Expenses By Category:")
    for key, amount in amount_by_category.items():
        print(f"{key}: ${amount:.2f}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"You've Spent ${total_spent} this month")

    remaining_budget = Budget - total_spent 

    print(f"Your Remaining Budget is ${remaining_budget}")

    # print (amount_by_category)


# function will only be run if called

if __name__ == "__main__":
    main()