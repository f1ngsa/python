print("You wake up on a spaceship, you dont remember anything. \nYour actions?\nOption 1 you contact Earth.\nOption 2 you look around the space ship,\nOr option 3, try to learn to control the space ship.")
enter = input("Which option are you choosing? option 1 or option 2?: ")
if enter == "option 1" or enter == "Option 1" or enter == "1":
    print("Earth isnt answering.")
    print("Enter 1 if you want to send a SOS signal.\nEnter 2 if you want to press the big red button on the remote.")
    hm = input("Which option are you choosing?: ")
    if hm == "Option 1" or hm == "option 1" or hm == "1":
        print("After a long time of waiting your signal has been heard, and they sent a rescue team after you.")
    elif hm == "option 2" or hm == "Option 2" or hm == "2":
        print("After pressing the big red button a bomb has been thrown on Earth, you accidently destroyed your home planet.")
elif enter == "option 2" or enter == "Option 2" or enter =="2":
    print("All of the cabins are empty, you are the only one on the ship and don't know how to control it.\nOption 1, try to turn on the autopilot.\nPress the SOS button.")
    hmmm = input("What option do you pick?: ")
    if hmmm == "Option 1" or hmmm == "option 1" or hmmm =="1":
        print("After you turned on the autopilot, the ship started going into an unknown direction, you died of hunger later, with failing to find anything to eat on the ship.")
    elif hmmm == "Option 2" or hmmm == "option 2" or hmmm == "2":
        print("Your signal has been heard, and a rescue team has been sent to you.")
elif enter == "Option 3" or enter == "option 3" or enter == "3":
    print("You succesfully learn to control the space ship and go back to Earth.")