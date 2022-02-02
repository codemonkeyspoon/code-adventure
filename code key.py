import string
import random
import os.path

## characters that help generate the password
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    ## Specify website
    website = str(input("What website? "))

    ## length of password from the user
    length = int(input("Enter password length: "))

    ##Number of character types
    alphabets_count = int(input("How many letters: "))
    digits_count = int(input("How many numbers: "))
    special_characters_count = int(input("How many special characters"))

    characters_count = alphabets_count + digits_count + special_characters_count

    ## Confirm total length
    ## will print if sum is greater than length
    if characters_count > length:
        print("Characters total amount is greater than the password length")
        return

    ## initialize the password
    password = []

    ## Picks random letters
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    ## Picks random digits
    for i in range(digits_count):
        password.append(random.choice(digits))

    ## picks random special charaters
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    ## if the total count is less than entered length
    ## add characters to equal total length
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    ## shuffle the characters
    random.shuffle(characters)

    ## shuffle result password
    random.shuffle(password)

    ## convert the list into string
    ## then print list
    print("This password was created for " + website + "\n")
    print("".join(password))
    password += "\n"

    file = open("passlist.txt", "a")
    file.write(website + ": ")
    file.write("".join(password))
    file.close()



## invoke function
generate_random_password()
