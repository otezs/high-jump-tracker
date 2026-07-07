# High jump tracker v1.0 by Maxim Szeto
import os
import json
import time

# holds all of the high jump logs
highJumpLog = {
    
    "height": [],
    "date": []
    
}


# 1. Finds the folder where main.py lives
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Glues the folder path and the filename together
file_path = os.path.join(script_dir, "high-jump-log.json")

 
# 3. We use 'file_path' instead of just the filename.
try:
    with open(file_path, "r") as file:
        highJumpLog = json.load(file)

except FileNotFoundError:
    pass


os.system("clear")
askUserName = input("Welcome to Maxim's High jump App! Please enter your name: ")
if askUserName.lower() == "maxim":
    print("Developer mode activated! Welcome, Maxim!")
else:
    print(f"Hello, {askUserName}! Thanks for using my High Jump App.")

time.sleep(3)


# main function controls the major functionings of the app
def main():
    averageHeight = 0
    index = 0
    userInput = 0
    
    # this input will keep showing up until the user desides to leave the app
    while userInput != "5":
        os.system("clear")
        userInput = input("""Here is what you can do in the app:\n1. Add or delete a jump in your training log (in meters)
        \n2. View your training log
        \n3. View your average jump height and your personal best and when it was achieved
        \n4. Add new goal and see progress
        \n5. Leave
        \nPlease input the number corresponding with what action you want to do: """)

        '''
        If the user inputs 1 we will ask them how high they jumped. If the user inputs anything but
        number we have a except block of code so no error message is created. When the user inputs a 
        log we will append the new log into the list that has all of the logs.
        '''
        if userInput == "1":
            os.system("clear")
            addOrDelete = input("\n1. Add a jump\n2. Delete a jump\nWhat would you like to do?: ")
            if addOrDelete == "1":
                try:
                    newlog = float(input("\nIn meters what height did you achieve? "))
                    newlog = round(newlog, 2)

                    if newlog <= 0.00:
                        print("\nYou cant jump negative meters.")

                    elif newlog <= 1.00:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"Good start. {newlog:.2f} meters is good but you can do better\n")
                    elif newlog <= 1.50:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"that is pretty solid. {newlog:.2f} meters is solid\n")
                    elif newlog <= 2.00:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"dang you jumping. {newlog:.2f} meters is good\n")
                    elif newlog >= 2.00:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"Wowza. {newlog:.2f} meters is amazing\n")
                    
                except ValueError:
                    print("Please input a number.\n")
                
                time.sleep(2)
                '''
                When we first ask them to delete a jump we first have to show them
                there training log. Then we ask them which jump they want to delete
                and then turn it into a integer so we can manipulate it. Then we look
                at each jump in the log and if the jump is equal to the number of jump
                they wanted gone minus one we delete it from the log
                '''

            elif addOrDelete == "2":
                
                
                if highJumpLog["height"] != []:
                    os.system("clear")
                    try:
                        index = 1
                        print("Here is your training log:\n")
                        for jump in highJumpLog["height"]:
                            print(f"Jump #{index}: {jump}m\n")
                            index += 1   
                        deleteWhichJump = int(input("Which Jump would you like to delete?: "))
                        for jump in highJumpLog["height"]:
                            if jump == highJumpLog["height"][deleteWhichJump - 1]:
                                del highJumpLog["height"][deleteWhichJump - 1]
                        os.system("clear")
                        print(f"\nJump {deleteWhichJump} ({jump}m) has been deleted.\n")
                        time.sleep(2)
                    except IndexError:
                        print(f"\nThere is no jump #{deleteWhichJump}")

                else:
                    os.system("clear")
                    print("You have nothing in your high jump log")
                    
                    while True:
                        userExit = input("\nclick e to exit: ")
                        if userExit == "e":
                            break

            else:
                print("Choose 1 or 2 dude")

            with open(file_path, "w") as file:
                json.dump(highJumpLog, file)

            '''
            if the user inputs two we will print their training log by using an f string
            to show the jumps in a human readable manner. for each of the jumps in the highjump
            log we will print what number jump it was and then the actual height of the jump
            '''

        elif userInput == "2":
            os.system("clear")
            if highJumpLog["height"] != []:
                index = 1
                print("Here is your training log:\n")
                for jump in highJumpLog["height"]:
                    print(f"Jump #{index}: {jump:.2f}m\n")
                    index += 1
            else:
                print("\nThere is nothing in your training log\n")
                time.sleep(3)
            
            while True:
                userExit = input("click e to exit: ")
                if userExit == "e":
                    break
                
            
            '''
            If the user presses 3 we first check if they have any jumps logged. if they do
            no we tell them so. If they do we calculate the average jump height by adding all the
            jumps together and each time adding 1 to the index so we can divide the total height of
            all the jumps by the amount of jumps taken. Then we find the highest jump by saying for 
            each jump in the log if the jump is greater than the current pb of = then that is the new pb
            we print both the average and the pb at the same time.
            '''

        elif userInput == "3":
            os.system("clear")
            if highJumpLog["height"] != []:
                calcAvgHJ()
                calcPB()

            else:
                print("\nYou do not have any jumps logged\n")
            
            while True:
                userExit = input("click e to exit: ")
                if userExit == "e":
                    break
            
                

        elif userInput == "4":
            os.system("clear")
            if highJumpLog["height"] != []:    
                pb = 0
                for jump in highJumpLog["height"]:
                    if jump > pb:
                        pb = jump
                
                try:    
                    userGoal = float(input("\nWhat is your high jump height goal?: "))
                    if userGoal <= 0.00:
                        print("\nYou cant jump negative meters dude.")
                        time.sleep(3)
                        continue
                    elif userGoal <= pb:
                        print("\nYou have already achieved that high of a jump\n")
                        time.sleep(3)
                        continue
                    elif pb / userGoal >= 0.95:
                        calcGoal(pb, userGoal)
                        print("This goal is within reach")
                    elif pb / userGoal >= 0.90:
                        calcGoal(pb, userGoal)
                        print("This goal is will be hard but you can do it!")
                    elif pb / userGoal >= 0.85:
                        calcGoal(pb, userGoal)
                        print("This goal is going to be challenging")
                    elif pb / userGoal >= 0.80:
                        calcGoal(pb, userGoal)
                        print("This goal is going to be pretty hard")
                    else:
                        print("This goal is basically impossible")
                                
                except ValueError:
                    print("Please input a number.\n")
                userExit = input("\nclick e to exit: ")

            else:
                print("You have nothing in you high jump log\n")            
            

                while True:
                    userExit = input("click e to exit: ")
                    if userExit == "e":
                        break
                    
            
        
        elif userInput == "5":
            print("\nThanks for using my app! Bye!\n")
            return 
        

        else:
            print("\nThats not an option\n")
                



def calcAvgHJ():
    index = 0
    averageHeight = 0
    for jump in highJumpLog["height"]: 
        averageHeight += jump
        index += 1
    averageHeight = averageHeight/index
    print("Your average jump height is... " + str(round(averageHeight, 2)) + " meters!\n")


def calcPB():
    pb = 0
    for jump in highJumpLog["height"]:
        if jump > pb:
            pb = jump
    print(f"Your Personal Best jump is {pb}m\n")

def calcGoal(userPB, goal):
    userProgress = round(userPB/goal, 2) * 100
    print(f"\nCurrent PB: {userPB}m")
    print(f"Goal: {goal:.2f}m")
    print(f"Progress: {userProgress}%")
    

main()

if __name__ == "__main__":
    main()