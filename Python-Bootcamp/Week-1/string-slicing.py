encrypted_message = 'bmaunmdbraai'

# Split the encrypted message into two parts based on the position of the comma
comma_index = encrypted_message.index(',')
first_part = encrypted_message[:comma_index]
second_part = encrypted_message[comma_index + 1:]

# Decrypt the first word
decrypted_first = first_part[::2]

# Decrypt the second word
decrypted_second = second_part[::2]

# Check if the length of the decrypted words match the original lengths
# If not, append '#' to the smaller word until they match
difference = len(decrypted_first) - len(decrypted_second)
if difference > 0:
    decrypted_second += '#' * difference
elif difference < 0:
    decrypted_first += '#' * abs(difference)

# Join the decrypted words with a comma and print the result
print(decrypted_first + ',' + decrypted_second)
