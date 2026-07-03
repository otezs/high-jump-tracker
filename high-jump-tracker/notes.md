Notes for main.py

Improvements:
- Add major actions to be functions
- Delete 


Issues:
#1 main function doesnt register 0 or -2 as out of range and still tells me that I did good
#2 When you put a negative number in the log it tells you both you cant jump negative feet and that thats not an option meaning that I think I need to exit the loop before it can register down there in the else statement
#3 numbers average jump height is not rounded to the hundreths place if the decimal ends earlier
like (3+2)/ 2 = 2.5 but should be shown as 2.50

Fixed:
#1 fixed: had to specify that the log had to be less than 0.0 since input is asking
for a float number
#2 fixed: use elif instead of if