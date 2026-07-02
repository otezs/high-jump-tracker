# High jump tracker v1.0 by Maxim Szeto
import json

# holds all of the high jump logs
highJumpLog = {
    
    "height": [],
    "date": []
    
}

# when we open the file for the first time we have to load the previous jumps
with open("high-jump-log.json", "r") as file:
    highJumpLog = json.load(file)




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
    while userInput != "4":
        with open("high-jump-log.json", "w") as file:
            json.dump(highJumpLog, file)

        userInput = input("""Here is what you can do in the app:\n1. Add or delete a jump in your training log (in meters)
        \n2. View your training log
        \n3. View your average jump height and your personal best and when it was achieved
        \n4. Leave app
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



main()