import string
import hashlib

def password_strength(password):
    suggestion=[]
    length=len(password)
    uppercasec=sum(1 for char in password if char in string.ascii_uppercase)
    lowercasec=sum(1 for char in password if char in string.ascii_lowercase)
    numberc=sum(1 for char in password if char in string.digits)
    specialc=sum(1 for char in password if char in string.punctuation)
    if length<12:
        suggestion.append("Password should be at least 12 characters long.")
    if uppercasec<1:
        suggestion.append("Password should contain at least one uppercase letter")
    if lowercasec<1:
        suggestion.append("Password should contain at least one lowercase letter")
    if numberc<1:
        suggestion.append("Password should contain at least one number")
    if specialc<1:
        suggestion.append("Password should contain at least one special character")
    for i in range(len(suggestion)):
        print(suggestion[i])
    if not suggestion:
        print("Password is strong")
        return "Password is strong"

result=password_strength("password")

def hash_password(password):
    password.encode('utf-8')
    hashed_password=hashlib.sha256(password.encode())
    return hashed_password

while True:
    password=input("Enter your password: ")
    result=password_strength(password)
    if result=="Password is strong":
        hashed_password=hash_password(password)
        print("Your password has been hashed using SHA-256:", hashed_password.hexdigest())
    choice=input("Do you want to check another password? (y/n): ")
    if choice.lower() != 'y':
        print("Exiting the program.")
        break
