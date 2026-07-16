# calculation functions that happen in the main file
import time

def addNewLog(jump, log):

        if jump <= 0.00:
            print("\nYou cant jump negative meters.")
            time.sleep(2)
            #continue

            # append each log into the height category of the high jump log
        elif jump <= 1.00:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"Good start. {jump:.2f} meters is good but you can do better\n")
        elif jump <= 1.50:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"that is pretty solid. {jump:.2f} meters is solid\n")
        elif jump <= 2.00:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"dang you jumping. {jump:.2f} meters is good\n")
        elif jump >= 2.00:
            log["height"].append(jump)
            print("\nAdded to log")
            print(f"Wowza. {jump:.2f} meters is amazing\n")
                        
        # at the very end of the adding section we will add a date no matter what the jump was
        log["date"].append(time.strftime("%Y-%m-%d - %I:%M %p", time.localtime()))


def calcPB(log):
    pb = 0
    pbDate = ""
    # since we zip the height and date lists together when we find the pb we use the same index 
    # and assign it to be the date of the pb
    for jump, date in zip(log["height"], log["date"]):
        if jump > pb:
            pb = jump
            pbDate = date
    print(f"Your Personal Best jump is {pb:.2f}m and it was logged on {pbDate}\n")


def calcAvgHJ(log):
    index = 0
    averageHeight = 0
    for jump in log["height"]: 
        averageHeight += jump
        index += 1
    averageHeight = averageHeight/index
    print("Your average jump height is... " + str(round(averageHeight, 2)) + " meters!\n")