def check_string(input_string):
    if 's' in input_string or 'S' in input_string:
        print("The string is containing the letter 's'")
    else:
        print("The string doesn't contain the letter 's'")

# Get input from the user
user_input = input("Enter a string: ")
check_string(user_input)