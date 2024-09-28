import random

#function of password generator
def Password_Generater(length):
    #for shorter length 
    if length < 5 :
        print('Length of password is too short!')
        return None
    
    #initiallize all the characters using to make password
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '1234567890'
    special_characters = '`~!@#$%^&*()-_=+[]{}\|;:,.></?'
    
    #creationg password list to store the characters of password
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
        ]
    
    #storing all characters in a variable   
    all_string = lowercase_letters + uppercase_letters + digits + special_characters
    #selecting random password for every time 
    password += random.choices(all_string,k = length-4)
    #shuffle our generated password
    random.shuffle(password)
    
    #join list to make a password
    return ''.join(password)

#taking length of password from user   
def taking_input():
    length = int(input('Enter length of password : '))
    return length
    
try :
    #function call   
    length = taking_input()
    password = Password_Generater(length)
    #printing generated password
    if password:
        print('Generated Password is : ', password)
    
except ValueError :
    print('Please enter a valid number .')
    