def shutdown():
    print("Select y/n.")
    sdConfirm = input("Do you want to shutdown your computer?: ")

    if sdConfirm == "y":
        apps = input("Are all applications closed?: ")
        if apps == "y":
            confirm = input("Do you Really want to shut down your computer?: ")
            if confirm == "y":
                print("Shutting down.....")
            elif confirm == "n":
                print("Cancelling Shut down...")
        elif apps == "n":
            print("Please turn off all applications before turning off your computer.")
    elif sdConfirm == "n":
        print("Cancelled Shut down.")

shutdown()