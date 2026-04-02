#Imports
import os
import hashlib

#Defining file where user information is stored
user_file = 'users.txt'

#Defining password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#Defining username
def user_exists(username):
    if not os.path.exists(user_file):
        return False
    with open(user_file, 'r') as f:
        return any(line.startswith(f"{username}:") for line in f)

#Defining Register function
def register():
    username = input("Enter your username: ")
    #If statement that doesnt allow multiple accounts with same name
    if user_exists(username):
        print("User already exists")
        return
    password = input("Enter a password: ")
    with open(user_file, 'a') as f:
        f.write(f"{username}:{hash_password(password)}\n")
    print("Registration successful")

#Defining Login function
def login():
    if not os.path.exists(user_file):
        #Checks if user entered has been registered
        print("No users registered yet")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")
    hashed = hash_password(password)

    with open(user_file, 'r') as f:
        for line in f:
            if line.strip() == f"{username}:{hashed}":
                print("Login successful")
                return
    #If password incorrect prints login failed
    print("Login failed")

#Defining menu function
def main():
    options = {'1': register, '2': login, '3': reset_password, '4': exit}
    while True:
        print("\n1. Register\n2. Login\n3. Reset Password\n4. Exit")
        choice = input("Choose an option: ")
        action = options.get(choice)
        if action:
            action()
        else:
            print("Invalid choice")


#Defining reset password function
def reset_password():
    if not os.path.exists(user_file):
        print("No users registered yet")
        return

    username = input("Enter your username: ")

    if not user_exists(username):
        print("User does not exist")
        return

    #2 factor authentication to protect users
    old_password = input("Enter your old password: ")
    old_hashed = hash_password(old_password)

    with open(user_file, 'r') as f:
        lines = f.readlines()

    updated = False

    with open(user_file, 'w') as f:
        for line in lines:
            stored_username, stored_hash = line.strip().split(":")
            #If username and password match allows user to change password
            if stored_username == username:
                if stored_hash == old_hashed:
                    new_password = input("Enter your new password: ")
                    new_hashed = hash_password(new_password)
                    f.write(f"{username}:{new_hashed}\n")
                    updated = True
                else:
                    print("Incorrect old password")
                    f.write(line)
            else:
                f.write(line)

    if updated:
        print("Password reset successful")

if __name__ == "__main__":
    main()

