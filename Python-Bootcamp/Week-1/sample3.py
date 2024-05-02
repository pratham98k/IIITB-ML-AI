# Input from the user
input_string = input("Enter a string: ")

# Remove numbers and special characters
cleaned_string = ''.join(char for char in input_string if char.isalpha())

# Convert uppercase letters to lowercase and vice versa
converted_string = ''.join(char.lower() if char.isupper() else char.upper() for char in cleaned_string)

# Output
print("Processed string:", converted_string)
