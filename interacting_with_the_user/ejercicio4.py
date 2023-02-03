"""
Chess Tournament
You are making a program that needs to calculate the points earned by a player in a chess tournament.
A win is worth 1 point, while a tie is worth 0.5 points.
The given program declares two variables: wins and ties.

Task
Complete the program to convert the inputted values into numbers, then calculate and output the points earned by the player.

Hint
Multiply the ties value by 0.5, to get the points earned for ties.
"""
wins = int(input())  #  guarda la entrada que realiza el usuario en una variable
ties = int(input())  #  guarda la entrada que realiza el usuario en una variable
print(wins+(ties*.5))  #  imprime las variables son sumadas y una de ellas se multiplica