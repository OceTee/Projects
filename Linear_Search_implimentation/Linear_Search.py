# Perform a linear search for the target in the list.
def linear_search(list, target):
    "Return the index of target in list, or None if not found."
    for i in range (0, len(list)):
        if list[i] == target:
            return i
    return None

# Verify and print the result of the search.
def verify(index):
    if index is not None:
        print(f"Target found at index: {index}.")
    else:
        print("Target not found in the list.")
    

# Initialize an empty list to store user inputs
input_list = []

# Prompt user for the number of elements in the list
input_count = int(input("Input the Total number of elements in the list:"))

# Collect user inputs to populate the list
for i in range(input_count):
    input_value = input("Enter value {}:".format(i + 1))
    input_list.append(input_value)
print("The list given as input by the user is :", input_list)


# Ask user if they want to modify the list
Confirmation = input("Would you like to add or remove elements from this list? (y/n): ")
if Confirmation.lower() == "y": 
    # Ask user what operation they want to perform
    operation = input("Enter the operation (add/remove): ")
    # Add a new element to the list
    if operation.lower() == "add":
        new_element = input("Enter the new element to add: ")
        input_list.append(new_element)
        print("Updated list:", input_list)
    # Remove an existing element from the list if it exist
    elif operation.lower() == "remove":
        element_to_remove = input("Enter the element to remove: ")
        input_list.remove(element_to_remove)
        print("Updated list:", input_list)
    else:
        print("Invalid operation. Please try again.")

# Prompt user for the element they want to search for
target = str(input("Enter the element to search for: "))

# Perform the linear search and Verify and display the search result
result= linear_search(input_list, target)
verify(result)
