def network():
    while True:
        print("\nNetwork Support:")
        print("1. No Internet Connection")
        print("2. Slow Internet")
        print("3. WiFi Not Showing")
        print("4. Limited Connection")
        print("5. Network Keeps Disconnecting")
        print("6. Return to Main Menu")

        choice = input("Select a network issue (1-6): ")

        if not choice.isdigit():
            print("Please enter a number.")
            continue

        choice = int(choice)

        # RETURN TO MAIN MENU
        if choice == 6:
            return

        # OPTION 1
        if choice == 1:
            while True:
                print("\nNo Internet Connection:")
                print("1. Check cables/router")
                print("2. Restart devices")
                print("3. Return")

                sub = input("Choose an option: ")

                if not sub.isdigit():
                    print("Please enter a number.")
                    continue

                sub = int(sub)

                if sub == 1:
                    print("Ensure Ethernet cables are plugged in and router lights are on.")
                elif sub == 2:
                    print("Restart your router and computer, then try reconnecting.")
                elif sub == 3:
                    break
                else:
                    print("Invalid option.")

        # OPTION 2
        if choice == 2:
            while True:
                print("\nSlow Internet:")
                print("1. Too many devices connected")
                print("2. Weak signal strength")
                print("3. Return")

                sub = input("Choose an option: ")

                if not sub.isdigit():
                    print("Please enter a number.")
                    continue

                sub = int(sub)

                if sub == 1:
                    print("Disconnect unused devices to free up bandwidth.")
                elif sub == 2:
                    print("Move closer to the router or use a wired connection.")
                elif sub == 3:
                    break
                else:
                    print("Invalid option.")

        # OPTION 3
        if choice == 3:
            while True:
                print("\nWiFi Not Showing:")
                print("1. WiFi turned off")
                print("2. Router issue")
                print("3. Return")

                sub = input("Choose an option: ")

                if not sub.isdigit():
                    print("Please enter a number.")
                    continue

                sub = int(sub)

                if sub == 1:
                    print("Make sure WiFi is enabled on your device.")
                elif sub == 2:
                    print("Restart your router and check if SSID is broadcasting.")
                elif sub == 3:
                    break
                else:
                    print("Invalid option.")

        # OPTION 4
        if choice == 4:
            while True:
                print("\nLimited Connection:")
                print("1. IP address issue")
                print("2. Router configuration")
                print("3. Return")

                sub = input("Choose an option: ")

                if not sub.isdigit():
                    print("Please enter a number.")
                    continue

                sub = int(sub)

                if sub == 1:
                    print("Try renewing your IP address using network settings.")
                elif sub == 2:
                    print("Reset router settings or contact your ISP.")
                elif sub == 3:
                    break
                else:
                    print("Invalid option.")

        # OPTION 5
        if choice == 5:
            while True:
                print("\nNetwork Keeps Disconnecting:")
                print("1. Interference")
                print("2. Outdated drivers")
                print("3. Return")

                sub = input("Choose an option: ")

                if not sub.isdigit():
                    print("Please enter a number.")
                    continue

                sub = int(sub)

                if sub == 1:
                    print("Keep router away from other electronics to reduce interference.")
                elif sub == 2:
                    print("Update your network drivers in device manager.")
                elif sub == 3:
                    break
                else:
                    print("Invalid option.")

        if choice < 1 or choice > 6:
            print("Please select a valid option (1-6).")