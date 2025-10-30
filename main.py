import os
# OS is used to clear the terminal for better readibility
from datetime import datetime
# Will be used for time stamps for whenever any files are updated

# Function to clear the terminal screen (works for both Windows and Mac/Linux)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display all student grades from the file
def choice_1(final):
    with open("grades.txt", "r") as file: # open file where grades and names are located

        for line in file:   # Loop through the lines of the file to get each name and grade stored in the file
            parts = line.strip().split(",")
            final += ": ".join(parts) + '\n'    # Take the contents found and put them together

    with open("log.txt", "a") as file:
            file.write(f"Display all students done on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n")

    return final

# Function to add a new student and their grade to the file
def choice_2():

    while True:
        try:
            name = input("Enter the students first name: ")
            grade = int(input("Enter the students grade: "))
            break
        except ValueError:
            clear()
            print("Invalid input, please try again")
    # Get user inputs of what they want to add

    with open("log.txt", "a") as file:
            file.write(f"New student added on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}, Student added: {name}, Students grade: {grade}\n")

    with open("grades.txt", "a") as file:   # Open the file and add the user inputs of the name and grade
        file.write(f"\n{name},{grade}") # \n used to create a new line in the .txt file
        file.write(f"\n\nUpdate at: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")},\nUpdate type: Add a student\nSuccesful: True")

    # Prints out if succesful and shows the updated grades.txt file using the function that would be used for choice 1
    print("Student added succesfully!")
    print("")
    print("Updated grade book: ")
    print(choice_1(final=""))
    input("Press enter to continue")

    clear()
    return

# Function to search for a student's record
def choice_3():
    clear()

    with open("log.txt", "a") as file:
            file.write(f"Student search on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n")

    while True:
        try:
            name = input("Who would you like to search for: ").capitalize()
            break
        except ValueError:
            clear()
            print("Invalid input, please put a valid input")
    # Get user input

    with open("grades.txt", "r") as file: # Open the file and loop through each line
        for line in file:
            check = line.strip().split(",")

            if check[0] == name:
                return ": ".join(check) # If studen found return their name and grade
        

    # If student not, return "Student not found"
    return "Student not found"


# Function to remove a student from the file
def choice_4(final):
    clear()

    found = False # Will be used to determine whether to open the file to edit it
    while True:
        try:
            name = input("Who do you want to remove: ").capitalize() # Get user input of target
            break
        except ValueError:
            clear()
            print("Invalid input, plesae try again")

    with open("grades.txt", "r") as file: # open file and loop through each line
        for line in file:

            current_line = line.strip().split(",")

            if name in current_line: # If the name that is being search for is found, found = True
                with open("log.txt", "a") as f:
                    f.write(f"Student removed on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}, Succesful: True, Student removed: {name}\n")
                found = True

            if name not in current_line: # Else, add the name to a list that will then be used to "recreate" the file without the target
                final.append(line)
            
    if found: # If found, open the file, and use the final list to recreate the grades.txt without the target
        with open("grades.txt", "w") as file: # Opening a file as write ("w") will delete its entire contents
            file.writelines(final) # No need for anything more as each line in the list has the nessecary formatting instructions, e.g. \n for a new line
        
        print(f"{name} removed succesfully!") # Confirm that the target has been removed
        
    else:
        with open("log.txt", "a") as file:
            file.write(f"Student removed on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}, Succesful: False\n")
        print("Student not found in record.") # Else, student was not in the file and could not be removed


    print("")
    input("Press enter to continue")

# Choice for calculating class summary
def choice_5():
    amount = 0
    total = 0
    grade = 0

    with open("grades.txt", "r") as file:
        for lines in file:
            part = lines.strip().split(",")
            try:
                grade = int(part[-1])
            except ValueError:
                pass
            print(grade)
            if grade == 0:
                pass
            else:
                amount += 1
                total += grade
            grade = 0
    
    average = total / amount
    final = round(average, 1)
    print(final)

    with open("summary.txt", "a") as file:
        file.write(f"Class average: {final} (Calculated on the {datetime.now().strftime("%d/%m/%Y %H:%M:%S")})\n")
    
    with open("log.txt", "a") as file:
        file.write(f"Class summary calculated on {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n")


    input("Average calculated succesfully, you can view in summary.txt. Press enter to continue")

# Main program loop
while True:
    clear() # Clear the terminal then display the choices
    print("1: Display records")
    print("2: Add a new record")
    print("3: Search for a student")
    print("4: Update or remove a record")
    print("5: calculate class statistics")


    """
    Each choice will wipe the terminal before printing empty strings for some formatting, then printing any text if needed, then executes
    the related function and prints the output. The input("Press enter to continue") is put in place to allow the user to actually view
    the printed contents otherwise the printed contents would show for a split second before being wiped and shown the choices they can
    choose from.
    """


    # Get user choice
    try:
        choice = int(input("What would you like to do with the grade book? (Select options 1-5): "))
    except ValueError:
        choice = 0
        clear()
        print("")
        print("Invalid input, please enter a valid input (1-5).")
        input("Press enter to continue")

    # Handles inputs that are not possible e.g. option 6 does not exist
    if (choice < 0) or (choice > 5):
        clear()
        print("")
        print(f"option {choice} does not exist, please enter a valid option")
        input("Press enter to continue")


    # Option 1: Display all student records
    if choice == 1:
        clear()
        print("")
        print("Student grades:")
        print(choice_1(final=""))
        input("Press enter to continue")

    # Option 2: Add a new record
    elif choice == 2:
        print("")
        choice_2()
        input("Press enter to continue")

    # Option 3: Search for a student
    elif choice == 3:
        print("")
        print(choice_3())
        input("Press enter to continue")

    # Option 4: Remove a student
    elif choice == 4:
        print("")
        choice_4(final=[])
    
    # Option 5: Class summary
    elif choice == 5:
        clear()
        print("")
        choice_5()

