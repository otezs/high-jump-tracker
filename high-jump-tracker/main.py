# High jump tracker v1.0 by Maxim Szeto
import os
import json
import time
import calculations

# holds all of the high jump logs
highJumpLog = {
    
    "height": [],
    "date": []
    
}

clearScreen = ""
if os.name == "nt":
    clearScreen = "cls"
else:
    clearScreen = "clear"

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

# clears screen for visibility
os.system(clearScreen)


while True:
    askUserName = input("Welcome to Maxim's High jump App! Please enter your name: ").strip()
    if not askUserName:
        print("Please input a valid username")
        time.sleep(2)
        os.system(clearScreen)
        continue
    else:
        print(f"Hello, {askUserName}! Thanks for using my High Jump App.")
        break




time.sleep(2)

# main function controls the major functionings of the app
def main():
    averageHeight = 0
    index = 0
    userInput = ""
    
    
    while userInput != "5": 
        os.system(clearScreen)
        # holds user input for navigating the app
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
            os.system(clearScreen)
            addOrDelete = input("\n1. Add a jump\n2. Delete a jump\nWhat would you like to do?: ")
            if addOrDelete == "1":
                try:
                    # turns input to float to be able to add to list as a float right away
                    newlog = float(input("\nIn meters what height did you achieve? "))
                    newlog = round(newlog, 2)

                    calculations.addNewLog(newlog, highJumpLog)
                    
                except ValueError:
                    print("Please input a number.\n")
                    time.sleep(2)
                    continue
                
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
                    os.system(clearScreen)
                    try:
                        calculations.showHJLog(highJumpLog)
                        try:
                            deleteWhichJump = input("To delete a jump input the number or if you want to delete all jump type ALL: ")
                            # instead of looping through the list since we already have the index needed for deletion
                            # we just delete it right then and there
                            if deleteWhichJump == "ALL":
                                calculations.deleteAllLogs(highJumpLog)
                                os.system(clearScreen) 
                                    
                            else:
                                calculations.deleteLog(highJumpLog, deleteWhichJump)
                                os.system(clearScreen)
                        except ValueError:
                            print("\nNumbers only")
                            time.sleep(2)
                    
                    except IndexError:
                        print(f"\nThere is no jump #{deleteWhichJump}")
                        time.sleep(2)

                else:
                    os.system(clearScreen)
                    print("You have nothing in your high jump log")
                    time.sleep(2)

                    calculations.exitToMainMenu()

            else:
                print("Choose 1 or 2 dude")
                time.sleep(2)

            # any time we add or delete a log we write to the high jump log file the changes we made
            with open(file_path, "w") as file:
                json.dump(highJumpLog, file)

            '''
            if the user inputs two we will print their training log by using an f string
            to show the jumps in a human readable manner. for each of the jumps in the highjump
            log we will print what number jump it was and then the actual height of the jump
            '''

        elif userInput == "2":
            os.system(clearScreen)
            if highJumpLog["height"] != []:
                calculations.showHJLog(highJumpLog)
            else:
                print("\nThere is nothing in your training log\n")
                time.sleep(2)
                continue
            
            calculations.exitToMainMenu()
                
            
            '''
            If the user presses 3 we first check if they have any jumps logged. if they do
            no we tell them so. If they do we calculate the average jump height by adding all the
            jumps together and each time adding 1 to the index so we can divide the total height of
            all the jumps by the amount of jumps taken. Then we find the highest jump by saying for 
            each jump in the log if the jump is greater than the current pb of = then that is the new pb
            we print both the average and the pb at the same time.
            '''

        elif userInput == "3":
            os.system(clearScreen)
            if highJumpLog["height"] != []:
                calculations.calcAvgHJ(highJumpLog)
                calculations.calcPB(highJumpLog)

            else:
                print("\nYou do not have any jumps logged\n")
            
            calculations.exitToMainMenu()
            
                

        elif userInput == "4":
            os.system(clearScreen)
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
                        calculations.calcGoal(pb, userGoal)
                        print("This goal is within reach")
                    elif pb / userGoal >= 0.90:
                        calculations.calcGoal(pb, userGoal)
                        print("This goal is will be hard but you can do it!")
                    elif pb / userGoal >= 0.85:
                        calculations.calcGoal(pb, userGoal)
                        print("This goal is going to be challenging")
                    elif pb / userGoal >= 0.80:
                        calculations.calcGoal(pb, userGoal)
                        print("This goal is going to be pretty hard")
                    else:
                        print("This goal is basically impossible")
                                
                except ValueError:
                    print("Please input a number.\n")
                userExit = input("\nclick e to exit: ")

            else:
                print("You have nothing in you high jump log\n")            
            

                calculations.exitToMainMenu()
                    

        elif userInput == "5":
            os.system(clearScreen)
            print("\nThanks for using my app! Bye!\n")
            time.sleep(2)
            os.system(clearScreen)
            exit()
        

        else:
            print("\nThats not an option\n")
            time.sleep(2)


if __name__ == "__main__":
    main()