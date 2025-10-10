import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def choice_1(final):
    with open("grades.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            final += ": ".join(parts) + '\n'
    return final


def choice_2():
    name = input("Enter the students first name: ")
    grade = int(input("Enter the students grade: "))
    with open("grades.txt", "a") as file:
        file.write(f"\n{name},{grade}")
    print("Student added succesfully!")
    print("")
    print("Updated grade book: ")
    print(choice_1(final=""))
    input("Press enter to continue")
    clear()
    return

def choice_3():
    clear()
    name = input("Who would you like to search for: ")
    name = name.capitalize()
    with open("grades.txt", "r") as file:
        for line in file:
            check = line.strip().split(",")
            if check[0] == name:
                return ": ".join(check)
    return "Student not found"

while True:
    clear()
    print("1: Display records")
    print("2: Add a new record")
    print("3: Search for a student")

    choice = int(input("What would you like to do with the grade book? (Select options 1-4): "))

    if choice == 1:
        clear()
        print("")
        print("Student grades:")
        print(choice_1(final=""))
        input("Press enter to continue")


    elif choice == 2:
        print("")
        choice_2()
        input("Press enter to continue")


    elif choice == 3:
        print("")
        print(choice_3())
        input("Press enter to continue")
