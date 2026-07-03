# High jump tracker v1.0 by Maxim Szeto
import os
import json

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


averageHeight = 0
index = 0
userInput = 0
pb = 0


askUserName = input("Welcome to Maxim's High jump App! Please enter your name: ")
if askUserName.lower() == "maxim":
    print("Developer mode activated! Welcome, Maxim!")
else:
    print(f"Hello, {askUserName}! Thanks for using my High Jump App.")
print("--------------------------------------------------------------")


# main function controls the major functionings of the app
def main():
    averageHeight = 0
    index = 0
    userInput = 0
    
    # this input will keep showing up until the user desides to leave the app
    while userInput != "5":
        with open(file_path, "w") as file:
            json.dump(highJumpLog, file)

        userInput = input("""\nHere is what you can do in the app:\n1. Add or delete a jump in your training log (in meters)
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
            addOrDelte = input("\n1. Add a jump\n2. Delete a jump\nWould you like to: ")
            if addOrDelte == "1":
                try:
                    newlog = float(input("\nIn meters what height did you achieve? "))
                    # newlog = f"{newlog:.2f}

                    if newlog <= 0.00:
                        print("\nYou cant jump negative meters dude.")

                    elif newlog <= 1.00:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"Good start. {newlog} meters is good but you can do better\n")
                    elif newlog <= 1.50:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"that is pretty solid. {newlog} meters is solid\n")
                    elif newlog <= 2.00:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"dang you jumping. {newlog} meters is good\n")
                    elif newlog >= 2.00:
                        highJumpLog["height"].append(newlog)
                        print("\nAdded to log")
                        print(f"Wowza. {newlog} meters is amazing\n")
                    
                except ValueError:
                    print("Please input a number.\n")

                '''
                When we first ask them to delete a jump we first have to show them
                there training log. Then we ask them which jump they want to delete
                and then turn it into a integer so we can manipulate it. Then we look
                at each jump in the log and if the jump is equal to the number of jump
                they wanted gone minus one we delete it from the log
                '''

            elif addOrDelte == "2":
                index = 1
                print("Here is your training log:\n")
                for jump in highJumpLog["height"]:
                    print(f"Jump #{index}: {jump}m\n")
                    index += 1   
                deleteWhichJump = int(input("Which Jump would you like to delete?: "))
                for jump in highJumpLog["height"]:
                    if jump == highJumpLog["height"][deleteWhichJump - 1]:
                        highJumpLog["height"].pop(deleteWhichJump - 1)
                print(f"\nJump {deleteWhichJump} ({jump}m) has been deleted.\n")


            else:
                print("Choose 1 or 2 dude")
       
            '''
            if the user inputs two we will print their training log by using an f string
            to show the jumps in a human readable manner. for each of the jumps in the highjump
            log we will print what number jump it was and then the actual height of the jump
            '''

        elif userInput == "2":
            if highJumpLog["height"] != []:
                index = 1
                print("Here is your training log:\n")
                for jump in highJumpLog["height"]:
                    print(f"Jump #{index}: {jump}m\n")
                    index += 1
            else:
                print("\nYou have nothing in your training log\n")
            
            
            
            '''
            If the user presses 3 we first check if they have any jumps logged. if they do
            no we tell them so. If they do we calculate the average jump height by adding all the
            jumps together and each time adding 1 to the index so we can divide the total height of
            all the jumps by the amount of jumps taken. Then we find the highest jump by saying for 
            each jump in the log if the jump is greater than the current pb of = then that is the new pb
            we print both the average and the pb at the same time.
            '''

        elif userInput == "3":
            if highJumpLog["height"] != []:
                calcAvgHJ()
                calcPB()
            else:
                print("\nYou do not have any jumps logged\n")
                


        elif userInput == "4":
            pb = 0
            for jump in highJumpLog["height"]:
                if jump > pb:
                    pb = jump
            try:    
                userGoal = float(input("\nWhat is your high jump height goal?: "))
                if userGoal <= 0.00:
                    print("\nYou cant jump negative meters dude.")
                elif userGoal <= pb:
                    print("\nYou have already achieved that high of a jump\n")
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
        
        elif userInput == "5":
            print("\nThanks for using my app! Bye!\n")
            exit()
        

        else:
            print("\nThats not an option gurt\n")
                



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
    print(f"Goal: {goal}m")
    print(f"Progress: {userProgress}%")

main()