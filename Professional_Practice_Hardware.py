
def hardware():
    print("You have selected Option 1: Hardware support.")
    print("which category dop you need help with:\n"
              "1.Computer system\n"
              "2.Peripherals")
  
    Choice = input("please select one of the options")
    Choice = int(Choice)

    if Choice ==1:
        print("You have selected Computer system support")
        computerSystem()

    elif Choice ==2:
        print("You have selected Peripheral support")
        peripheral()
    else:
        print("please select either 1 or 2:")

def computerSystem():
    print("Please specify the problem with the system:\n" 
    "1.Overheating\n" \
    "2.No Power\n" \
    "3.Display Issues\n"
    "4.Storage Issues")

    Choice1=input("Please select an option:")
    Choice1=int(Choice1)

    if Choice1 ==1:
        print("You have selected overheating problems\n"
              "Here is some information that may be useful\n")
        print(" If your system is overheating, There may be issues with the external fans in the case\n" \
        "Make sure they are working correctly by ensuring they are connected to the motherboard in the correct port and\n" \
        "dust them regularly to ensure maximum performance. ")

    elif Choice1==2:
        print("You have selected Power problems\n"
              "Here is some information that may be useful\n")
        print("Make sure the power supply is switched on and connected correctly to the system\n"
        "The system may need a stronger power supply or a new one if it has failed \n"
        "Additionally make sure that the Outlet the shstem is plugged into is fully working \n")

    elif Choice1==3:
        print("You have selected Display problems\n"
              "Here is some information that may be useful\n")
        print("Make sure the display and system are connected porperly with the correct cable \n"
              "Ensure that the display is connected to correct port on the I/O shield or graphics card of the system\n" \
              "MAke sure the Display has sufficient power to it")

def peripheral():
    print("You have selected Option 2: Perihperal support.\n"
          "Here is some tips and information that may be helpful for keyboards, mice, printers, etc.\n")
    print("Make sure that the peripheral is connected correctly to the system using the correct port, wires or connection type needed.\n"
          "Make sure that any necessary drivers for the peripheral are downloaded onto your system. \n"
          "Make sure that your system supports the specific peripheral that you are wishing to use.")


if __name__=="__main__":
    hardware()
