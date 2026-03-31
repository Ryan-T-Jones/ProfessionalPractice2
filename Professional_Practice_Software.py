def software():
    print("You have selected software issue")
    while True:
        print("Which catagory would you like to select:\n" 
        "1:Performance\n" 
        "2:Settings\n" 
        "3:Application\n" 
        "4:File\n" 
        "5:Return")
        try:
            Response=input(": ")
            Response=Response.strip().lower()
            match Response:
                case "1"|"performance":
                    print("performance")
                    Performance()
                case "2"|"Settings":
                    print("")
                    Settings()
                case "3"|"Application":
                    print("")
                    Application()
                case "4"|"File":
                    print("")
                    File()
                case "5"|"Return":
                    #Return()
                    return
        except:
            print("")

def Performance():
    print("You have selected performance issue")
    while True:
        try:
            print("Low performance can be caused by multiple factors:\n" 
            "1:High CPU usage.\n" 
            "2:High RAM usage.\n" 
            "3:High memory usage.\n" 
            "4:Malware.\n" 
            "5:High network bandwidth.\n" 
            "6:Hardware issues.")
            print("To Solve your problem more information is required.\n" 
            "Please select from the list above of the potential issues to find how to diagnose the issue and a solution")
            #To imporve, user would enter specific symptoms and the program would able to detect issue
            Response=input(":").strip().lower()
            print("Enter 1 for help diagnosing the problem. Enter 2 for help resolving the problem")
            Response_Type=input(": ").strip().lower()
            match Response:
                #CPU
                case "1"|"High CPU usage" if Response_Type=="1":
                    print("To diagnose CPU usage open the task manager application. A percentage of CPU usage is available at the top of the screen. This menu will also reveal which applications are causing high CPU usage.")

                #RAM
                case "2"|"High RAM usage" if Response_Type=="1":
                    print("To diagnose RAM usage open the task manager application. A percentage of RAM usage is available at the top of the screen. This menu will also reveal which applications are causing high RAM usage.")

                #Memory
                case "3"|"High memory usage" if Response_Type=="1":
                    print("To diagnose memory usage open settings. Within settings search for storage. This menu will display total storage and how it is used and by what")

                #Malware
                case "4"|"Malware" if Response_Type=="1":
                    print("To diagnose malware open a malware detetion program and run a scan. For computers running windows this can be windows security")
                    Alternative_Response=input("For more accurate information to diagnose or resolve please select security option")
                    #check
                    if Alternative_Response=="yes":
                        return
                    else:
                        pass

                #Network
                case "5"|"High network bandwidth" if Response_Type=="1":
                    print("To diagnose check network connectivity within network and internet in settings. To check performance of network run an online interent speed test")
                    Alternative_Response=input("For more accurate information to diagnose or resolve please select network option")
                    #check
                    if Alternative_Response=="yes":
                        return()
                    else:
                        pass

                #Hardware
                case "6"|"Hardware issues" if Response_Type=="1":
                    print("To diagnose hardware issues check if device is overheating or loud fan sounds. It may also be useful to check component's compatability and componets age and specifications")
                    Alternative_Response=input("For more accurate information to diagnose or resolve please select hardware option")
                    #check
                    if Alternative_Response=="yes":
                        return()
                    else:
                        pass
                case "1"|"High CPU usage" if Response_Type=="2":
                    print("There are multiple solutions it is best to try each one until the problem is resolved.\n"
                    "1:Close specific applications that have high CPU usage that are not being used.Ensure not to close nessecary application, if unsure search online first before closing.\n"
                    "2:If the application being activly used has high CPU usage then check applications settings for optimaisation options or for potential updates. If the options are unavailable eithier switch application or follow other methods to reduce CPU usage.\n" 
                    "3:Check the system for updates, the operating system might be runing an older version or drivers could be outdated. Updating can resolve bugs and introduce new methods to improve performance.\n"
                    "4:Disable unnecessary services, some services are allows active. Check settings and then startup and turn off unwanted services or check task manager for constant services.Ensure not to end nessecary application, if unsure search online first before ending services.\n"
                    "5:Reboot the device, a reboot can remove old programs, fix memory leaks and stop unnecessary services providing a standard environment at regual performance.\n"
                    )
                case "2"|"High RAM usage" if Response_Type=="2":
                    print("There are multiple solutions it is best to try each one until the problem is resolved.\n"
                    "1:Close specific applications that have high RAM usage that are not being used.Ensure not to close nessecary application, if unsure search online first before closing.\n"
                    "2:If the application being activly used has high RAM usage then check applications settings for optimaisation options or for potential updates. If the options are unavailable eithier switch application or follow other methods to reduce RAM usage.\n" 
                    "3:Clear Cache in both the browser and the computer. In a bowser this option will be located in the browser setting usually under privacy and security option. To clear a computers cache go to settings then storage and the option should appear.\n"
                    "4:Check for malware or suspicious applications that have high resource usage.\n"
                    "5:Reboot the device, a reboot can remove old programs, fix memory leaks and stop unnecessary services providing a standard environment at regual performance.\n"
                    )

                case "3"|"High memory usage" if Response_Type=="2":
                    print("There are multiple solutions it is best to try each one until the problem is resolved.\n"
                          "1:Clear the recylce bin located on the desktop or in the file explorer under home, it stores deleted data but still takes up space.\n"
                          "2:Run windows file cleanup, enter setting and select storage, an option to cleanup files should appear.This removes files from downloads and delete unused system files.\n"
                          "3:Manually check and remove unused data or duplicate files that take up additional storage.\n"
                          "4:Unistall application through the correct methods by entering settings and select apps, then select installed apps and unistall unwanted application. Manual deletion can cause some files to remain if not careful.\n"
                          "5:Create backups of old but wanted data on external drives to save space on the main device.\n")
        except:
            print("")
        return

def Settings():
    print("You have selected Settings issue")
    while True:
        print("Below is a list of setting options available to select from:\n" 
        "1:Audio.\n" 
        "2:Accessibility.\n" 
        "3:Display.\n" 
        "4:Maintenance.\n"
        "5:Return.")
        print("Please select from the list above of the Settings related issue you need help with")
        #To imporve, user would enter specific setting or describe a change and the program would give a setting
        try:
            Response=input(": ")
            Response=Response.strip().lower()
            match Response:
                case "1"|"Audio":
                    print("1.no sound playing from computer\n"
                    "2.no sound playing from headset\n"
                    "3.no audio detected")
                case "2"|"Accessibility":
                    print("1.Alter text size\n"
                    "2.Enable text to speech\n"
                    "3.Control perhipherals\n")
                case "3"|"Display":
                    print("1.Change screen brightness\n"
                    "2.Change Display projection\n"
                    "3.Advanced display changes\n")
                case "4"|"Maintenance":
                    print("1.Check for updates\n"
                    "2.power settings\n"
                    "3.Manage storage\n")
                case "5"|"Return":
                    break
            
            while True:
                Response_Number=input(": ")
                match Response:
                    case "1"|"Audio" if Response_Number=="1":
                        print("Ensure monitor or computer has built in speakers, ensure volume option is turned up. Enter settings and select sound, select output option and click on the chosen device to output sound. Ensure sound is enable for application within volume mixer option.")
                    case "1"|"Audio" if Response_Number=="2":
                        print("Ensure headset is connected correctly and plugged into the correct port, ensure volume option is turned up. Enter settings and select sound, select output option and click on the chosen device to output sound.")
                    case "1"|"Audio" if Response_Number=="3":
                        print("Ensure microphone is connected correctly and plugged into the correct port, ensure volume option is turned up. Enter settings and select sound, select input option and click on the chosen device to input sound. Ensure sound is enable for application within volume mixer option.")
                    case "2"|"Accessibility" if Response_Number=="1":
                        print("Enter settings and select accessibility, select the option text size and change it. Other oprions to change text appearance are available. To change font size in browser open broswer setting and select appearance then select fonts.")
                    case "2"|"Accessibility" if Response_Number=="2":
                        print("Enter settings and select accessibility, select the option narrator and choose the perfered settings. Some browser might have a built in text to speech option.")
                    case "2"|"Accessibility" if Response_Number=="3":
                        print("The keyboard and mouse and be changed for personal prefrences. For the keyboard, an option for an on screen keyboard is available. For the mouse, the speed and size of the cursor and be changed. To access enter setting then select accessibility.")
                    case "3"|"Display" if Response_Number=="1":
                        print("The screen brightness can be controlled by the physical monitor with certain buttons. The brightness can also be controlled within settings in display. Alternative options are also availble for specific situations.")
                    case "3"|"Display" if Response_Number=="2":
                        print("To change display projection enable a connection to the desired device. Once a connection is established hold the windows button then press the 'p' button and then select on option.")
                    case "3"|"Display" if Response_Number=="3":
                        print("Within settings there are options to change display resolution and refresh rate. These options aloow for a better experience but can depend on the monitor capabilities and do effect performance.")
                    case "4"|"Maintenance" if Response_Number=="1":
                        print("If an update is available it might apear in the bottom right corner of the screen. Enter settings then select update to check for any updates. It is also importnat to check browser and applications for updates as well.")
                    case "4"|"Maintenance" if Response_Number=="2":
                       print("Enter settings then select power, there are options to reduce the energy consumption. One option is energy saver mode which reduce power consumption and increases battery life. Other options are also available.")
                    case "4"|"Maintenance" if Response_Number=="3":
                        print("Enter settings then select storage, this will display availble storage locations and storage allocation of software. If storage is full eitier increase physical storage or delete unused files. Do not delete neccessary files.")
                if Response_Number=="1" or Response_Number=="2" or Response_Number=="3":
                    break
                else:
                    pass
        except:
            print("")
    return
    
def Application():
    print("You have selected file issue")
    while True:
        print("Below is a list of Application options available to select from:\n"  
        "1:Email issue.\n" 
        "2:Software compatability.\n" 
        "3:Return.")
        print("Please select from the list above of the potential issues to find how to diagnose the issue and a solution")
        try:
            Response=input(": ")
            Response=Response.strip().lower()
            match Response:
                case "1"|"email issue":
                    print("1.Unable to send emails\n"
                    "2.unable to receive email\n"
                    "3.Attachment issues\n")
                case "2"|"software compatability issue":
                    print("1.Software not installing\n"
                    "2.Application error\n")
                case "3"|"return":
                    break
            #
            while True:
                Response_Number=input(": ")
                match Response:
                    case "1"|"email issue" if Response_Number=="1":
                        print("1:Check internet connection, no internet or a weak signal can result in emails not loading or aperaring.\n"
                        "2:Check different email folders, emails might get catagorised as spam or other.\n" 
                        "3:Check sender is not block or contains blocked content, check that the sender is not blocked by you or the administration.\n")
                    case "1"|"email issue" if Response_Number=="2":
                        print("1:Check internet connection, no internet or a weak signal can result in emails not sending.\n"
                        "2:Check that the recipient's address has been entered correctly, a typing error can lead to the email being send to an invalid account.\n" 
                        "3:Check recipient is not block or email does not contain blocked content, check that the recipient is not blocked by you or the administration.")
                    case "1"|"email issue" if Response_Number=="3":
                        print("1:If attachment is too large the email will not be able to be sent, eithier send content seperatly or compress file.\n"
                        "2:Blocked file type, some file types are block and will result in the email not sending or being block, send the content seperatly or zip the file.")
                    case "2"|"software compatability issue" if Response_Number=="1":
                        print("1:Not enough storage space, if there is not enough space in storage available the application will not install, check storage and create space before installing.\n"
                              "2:Software secuirty risk, the application might get flagged as malware or other security risk by the administration or operating system, check application is safe and authorised and eithier run as administrator or check security settings.\n"
                              "3:Software is incompatable, check that the software is for the correct operating system and the device meets the software requirements.")
                    case "2"|"software compatability issue" if Response_Number=="2":
                        print("1:Check software was installed correctly and is a compatable version, check that no files have corrupted or other software is needed.\n"
                              "2:Close and restart the software or the device, temporary issues can be fixed by restarting the software.\n"
                              "3:Check for available updates, the issue could be caused by running an older version of the software so an update can fix potential issues.")
                if Response_Number=="1" or Response_Number=="2":
                    break
                else:
                    pass
        except:
            print("")
    return

def File():
    print("You have selected file issue")
    while True:
        print("Below is a list of File options available to select from:\n"  
        "1:File management.\n" 
        "2:File storage.\n" 
        "3:Data loss and backup failures.\n" 
        "4:Download and transfer.\n"
        "5:Return.")
        print("Please select from the list above of the potential issues to find how to diagnose the issue and a solution")
        #To imporve,
        try:
            Response=input(": ")
            Response=Response.strip().lower()
            match Response:
                case "1"|"File management":
                    print(""
                    "1.File permissions\n"
                    "2.File type\n")
                case "2"|"File storage":
                    print(""
                    "1.Access cloud storage.\n"
                    "2.Access Shared drives\n"
                    "3.Access One drive\n")
                case "3"|"Data loss and backup failures":
                    print(""
                    "1.File corruption\n"
                    "2.Create backup\n"
                    "3.Recover data\n")
                case "4"|"Download and transfer":
                    print(""
                    "1.Download data\n"
                    "2.Transfer methods\n")
                case "5"|"Return":
                    break
            #
            while True:
                Response_Number=input(": ")
                Response_Number=Response.strip().lower()
                match Response:
                    case "1"|"File management" if Response_Number=="1":
                        print("Some drives may require different permission's to access or save too, if you are unable to access or use a drive check if the location being access is correct and the inform IT to update account permissions.")
                    case "1"|"File management" if Response_Number=="2":
                        print("Saving or using a file as the incorrect file type can cause the file to be unusable or corrupted due to incompatibility. To check the file type it will usually apear next to the file name")
                    case "2"|"File storage" if Response_Number=="1":
                        print("Cloud storage can be access by any device connected to the internet, the data saved is available on any device connected to the account. If unavailable check internet connection.")
                    case "2"|"File storage" if Response_Number=="2":
                        print("Shared drives can only be access by devices part of the network with accounts having different levels of permission to use,availble from file explorer. If unavailable check if device is part of the network and if account has permission to use the drive")
                    case "2"|"File storage" if Response_Number=="3":
                       print("One drive is connected the windows account, available from file explorer, the data saved is available on any device connected to the account. If unavailable check internet connection or check if your signed in from the system tray.")
                    case "3"|"Data loss and backup failures" if Response_Number=="1":
                        print("If a file is corrupted attempt to find a past version of the file from backups to use instead, some files may have alternate ways to access and recover some data. If system files are corrupted windows has a system file checker tool, to use it search online for the exact steps to use it.")
                    case "3"|"Data loss and backup failures" if Response_Number=="2":
                        print("Winodws has a built in backup system with one drive, enable one drive backup to upload file to one drive. External methods can be used by connecting an external drive and saving data to it through control panel then select file history to backup all files.")
                    case "3"|"Data loss and backup failures" if Response_Number=="3":
                        print("Windows has a built in backup system with one drive, open one drive and redownload any data lost. If data was deleteted it will be located in the recycle bin located on the desktop.")
                    case "4"|"Download and transfer" if Response_Number=="1":
                        print("When downloading software make sure it is compatable with the correct operating system version. When downloading data ensure it is the correct file type for use and is safe to download.")
                    case "4"|"Download and transfer" if Response_Number=="2":
                       print("Data can be transfered by shared storage software such as: drives, cloud storage, one drive or email. External hardware: USB, external hard drive or wired connection. File size can affect how data is sent file.")
                if Response_Number=="1" or Response_Number=="2" or Response_Number=="3":
                    break
                else:
                    pass
        except:
            print("")
    return


if __name__=="__main__":
    software()
