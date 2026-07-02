import json


myList = [2, 3, 4, 5, 3, 1, 0.5, 9]
greatestNum = 0

for i in myList:
    if i > greatestNum:
        greatestNum = i

print(greatestNum)



myList = [2,3,4,5]

print(myList)

for i in myList:
    if i < i+1:
        print(i)
'''
highJumpLog = {
    
    "height": [],
    "date": []
    
}
highJumpLog["height"].append(30)
print(highJumpLog["height"][0])


with open("high-jump-log.json", "w") as file:
    json_text = json.dumps(highJumpLog)
    file.write(json_text) 
    print(json_text)
'''

try:
    john = input("enter your name")
except KeyboardInterrupt:
    print("\nbruh")
