from ProfPractice_OptionOne import optionOne
from network
def main():
    print("what problem do you have today?")
    print("1. Hardware Support")
    print("2. Software Support")
    print("3. Network Support")
    print("4. Security Support")
    print("5. Other")

    userChoice = input("Please select an option:")
    userChoice = int(userChoice)

    if userChoice == 1:
        print("you have selected option 1")
        optionOne()

    elif userChoice == 2:
        print("you have selected option 2")
        #optionTwo()

    elif userChoice == 3:
        print("you have selected option 3")
        #optionThree()

    elif userChoice == 4:
        print("you have selected option 4")
        #optionFour()

    elif userChoice == 5:
        print("you have selected option 5")
        #optionFive()

    else:
        print("Please select an option from the above list 1-5")
main()
