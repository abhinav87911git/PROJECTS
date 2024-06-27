
#  script for password generator


import random
import string

def password_generator(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input('Enter the length of password you want : '))
    print(f'The generated password is : {password_generator(length)}')
