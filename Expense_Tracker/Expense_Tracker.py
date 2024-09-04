from Expense_Class import Expense

# Initializing the main function

def main():
    print(f"Running Expense Tracker!")
    expense_file_path = "./Expense_Tracker/Expense.csv"
    
    # Get user input for expense
    expense = get_user_expense()
    # Write their expense to file
    write_expense_to_file(expense, expense_file_path)
    # Read and summarize expenses
    read_and_summarize_expenses(expense_file_path)

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
    print(f"Saving User expense: {expense} to {expense_file_path}")

    # Implementing file writing logic
    
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")



def read_and_summarize_expenses(expense_file_path):
    print(f"Summarizing User Expenses")

    # Expense list to store the results
    expenses = []
    # Implementing file reading logic

    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            # for removing the white spaces in the string
            stripped_line = line.strip()
            line_elements = line.split(",")
            expense_name = line_elements[0]
            expense_category = line_elements[1]
            expense_amount = float(line_elements[2])
            print(expense_name, expense_amount, expense_category)


# function will only be run if called

if __name__ == "__main__":
    main()