# Gunnar Dougherty first Group 61 git addition

def menu():
    print('Menu')
    print('-' * 13)
    print('1. Encode\n2. Decode\n3. Quit')
    print('')  # instructions pdf shows double space between menu and input
    choice = int(input('Please enter an option: '))
    while True:
        if choice in (1, 2, 3):
            break
        else:
            choice = int(input('Invalid! Please enter an option: '))
    return choice  # menu option choice


def encode():
    password = input('Please enter your password to encode: ')
    encoded_password = '' # initialize new string
    for digit in password:  # iterate through each digit in string
        encoded_digit = (int(digit) + 3) % 10  # encoding is add 3, keep one digit, hence modulus 
        encoded_password += str(encoded_digit)  # add incoded digit to new string
    print('Your password has been encoded and stored!')
    print('')  # instructions pdf shows double space between confirmation output and menu
    return encoded_password


def main():
    while True:
        choice = menu()
        if choice == 1:
            encoded_password = encode() # stores encoded password as variable
        elif choice == 2:
            pass
        elif choice == 3:
            break


if __name__ == '__main__':
    main()
