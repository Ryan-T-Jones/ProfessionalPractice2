import Professional_Practice_Hardware
import Professional_Practice_Network 
import Professional_Practice_Software 
import Professional_Practice_Login 
import os
import hashlib

def main():

    while True:
        print("what problem do you have today?")
        print("1. Hardware Support")
        print("2. Software Support")
        print("3. Network Support")
        print("4. Account Support")
        print("5. Exit")
    
    
        userChoice = input("Please select an option:")
        userChoice = int(userChoice)
    
        if userChoice == 1:
            print("you have selected option 1")
            Professional_Practice_Hardware.hardware()
    
        elif userChoice == 2:
            print("you have selected option 2")
            Professional_Practice_Software.software()
    
        elif userChoice == 3:
            print("you have selected option 3")
            Professional_Practice_Network.network()
    
        elif userChoice == 4:
            print("you have selected option 4")
            Professional_Practice_Login.main()
        
        elif userChoice ==5:
            return
    
        else:
            print("Please select an option from the above list 1-5")
Professional_Practice_Login.login()
main()
