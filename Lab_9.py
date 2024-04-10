def encoder(password):
    encoded_pass=("")
    for digit in password:
        new_digit=str((int(digit)+3)%10)
        encoded_pass+=new_digit
    return encoded_pass
    
def decoder(numbers):
    decoded_password = ''
    for digit in numbers:
        encoded_digit = str((int(digit) - 3) % 10)
        encoded_password += encoded_digit
    return encoded_password
    "hello"
def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option=input("Please enter an option: ")
        if option =="1":
            password=(input("Please enter your password to encode: "))
            encoded_password=encoder(password)
            print("Your password has been encoded and stored!\n")
        if option=="2":
            print(f"The encoded password is {encoded_password}, and the original password is {decoder('password')}.\n")
        if option=="3":
            break


if __name__ == "__main__":
    main()
