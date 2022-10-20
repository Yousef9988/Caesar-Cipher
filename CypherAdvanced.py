def cypher(msg, shift):
    cypher_msg = ""
    for char in msg:
        if not char.isalpha():
            cypher_msg += char
        else:
            num_code = ord(char)
            if chr(num_code).isupper():
                if num_code + int(shift) <= 90:
                    new_char = chr(num_code + int(shift))
                else:
                    new_char = chr(64 + int(shift) - (90 - num_code))
            elif chr(num_code).islower():
                if num_code + int(shift) <= 122:
                    new_char = chr(num_code + int(shift))
                else:
                    new_char = chr(96 + int(shift) - (122 - num_code))
            cypher_msg += new_char

    return cypher_msg


message = input("Enter your message: ")
shift_value = 0                                                 # Define value for shift for the while loop
while shift_value == 0:                                         # Keep trying until the user inputs a valid shift value
    try:
        shift_value = input("Enter shift value for encryption: ")
        if int(shift_value) not in range(1, 26):
            raise ValueError
        cyphered_message = cypher(message, shift_value)
        print(cyphered_message)
    except ValueError:
        shift_value = 0
        if shift_value == 0:
            print("Invalid input! Insert a number between 1 and 25")



