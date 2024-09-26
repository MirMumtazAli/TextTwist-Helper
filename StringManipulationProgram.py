# Step 1: Take string input from the user
a = input("Enter a string : ")

# Display the menu of operations for string manipulation
print('''
    1. UPPER        6. index
    2. lower        7. reverse
    3. Capitalize   8. startswith
    4. islower      9. endswith
    5. isUpper      10. swapcase''')

# Step 2: Get the user's choice for the operation code
b = int(input("Enter the operation Code (between 1 and 10): "))

# Step 3: Ensure the operation code is valid (between 1 and 10)
while b<1 or b>10:
    print("-"*30)
    print("Please enter valid operation code (between 1 and 10): ")
    print("-"*30)
    
# Display the menu again for the user to pick a valid operation
    print('''
    1. UPPER        6. index
    2. lower        7. reverse
    3. Capitalize   8. startswith
    4. islower      9. endswith
    5. isUpper      10. swapcase''')
    b = int(input("Enter the operation Code (between 1 and 10): "))

# Step 4: Match the user's choice with the corresponding string operation
match b:
        case 1:
            # Convert the string to uppercase and print
            print(f"Upper of {a} is :", a.upper())
        case 2:
            # Convert the string to lowercase and print
            print(f"Lower of {a} is :", a.lower())
        case 3:
            # Capitalize the first letter of the string and print
            print(f"Capitalize of {a} is : ", a.capitalize())
        case 4:
            # Check if the string is in lowercase
            checklows = a.islower()
            if checklows == True:
                print("Given string is in lower case.")
            else:
                print("Given string is not in lower case.")
        case 5:
            # Check if the string is in uppercase
            checkupps = a.isupper()
            if checkupps == True:
                print("Given string is in UPPER case.")
            else:
                print("Given string is not in UPPER case.")
        case 6:
            # Get the index of a specific letter in the string
            try:
                letter = input(f"Enter the letter from \'{a}\' to get index number :")
                print(f"Index number of {letter} in {a} is :" , a.index(letter))
            except ValueError:
                # Handle the case where the letter is not in the string
                print("Given letter not in the given string.")
        case 7:
            # Reverse the string and print
            print(f"Reverse of {a} is :", a[::-1])
        case 8:
            # Check if the string starts with a specific letter
            letter = input(f"Enter the letter to check (starts with) : ")
            checkstart  = a.startswith(letter)
            if letter in a:
                if checkstart == True:
                    print(f"Given String starts with {letter}")
                else:
                    print(f"Given String does not starts with {letter}")
            else:
                print("Given letter not in the given string.")
        
        case 9:
            # Check if the string ends with a specific letter
            letter = input(f"Enter the letter to check (ends with) : ")
            checkend  = a.endswith(letter)
            if letter in a:
                if checkend == True:
                        print(f"Given String ends with {letter}")
                else:
                    print(f"Given String does not ends with {letter}")
            else:
                print("Given letter not in the given string.")
        case 10:
            # Swap the case of each letter in the string (upper to lower, lower to upper)
            swapcs = a.swapcase()
            print(f"After swapping case : {swapcs}")
        case _:
            # If an invalid operation code is somehow entered, display an error message
            print("Please enter valid Operation Code (between 1 and 10).")
        