# John Cooper
def encode(decoded_password):
    # Encodes the password adding 3 to each digit.
    # Uses modulo operator to make sure the result is from 0-9
    encoded_password = ""
    for digit in decoded_password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = int(digit)+7
        decoded_password += (str(decoded_digit))[-1]
    return decoded_password


def main():
    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        menu_selection = int(input('Please enter an option: '))

        if menu_selection == 1:
            passcode = input('Please enter your password to encode: ')
            encoded_password = encode(passcode)
            print('Your password has been encoded and stored!\n')

        if menu_selection == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')

        if menu_selection == 3:
            quit()


if __name__ == "__main__":
    main()

