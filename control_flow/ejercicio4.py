"""
Organized Robot

Your program will be used in a robot to categorize items by their color.
Each color corresponds to a box with a specific number.
For simplicity, the program handles 3 colors:
 red goes to box #1
 green goes to box #2
 black goes to box #3
The given program takes the color as input.

Task
Complete the program to output the corresponding box in the given format.
In the case of an unsupported color, the program should output unknown.

Input Example
green

Output Example
box #2
"""
color = input()

#your code goes here
if color == "red":
    print("box #1")
elif color == "green":
    print("box #2")
elif color == "black":
    print("box #3")
else:
    print("unknown")
