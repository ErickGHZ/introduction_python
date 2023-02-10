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
color = input()  #  pide una entrada de una cadena de texto
if color == "red":  #  realiza una comparacion
    print("box #1")  #  si la comparacaion anteior es correcta imprime una cadena de texto
elif color == "green":  #  si la comparacion anterior no fue cierta realiza esta comparacion
    print("box #2")  #  si la comparacaion anteior es correcta imprime una cadena de texto
elif color == "black":  #  si la comparacion anterior no fue cierta realiza esta comparacion
    print("box #3")  #  si la comparacaion anteior es correcta imprime una cadena de texto
else:  #  si la comparacion anterior no fue cierta realiza esta accion
    print("unknown")  #  imprime una cadena de texto
