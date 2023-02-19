"""
Going Once, Going Twice, Sold

You are writing a program for an auction where the maximum bid is set. The number of bids is variable.
Task
Complete the program to take all bids from auction participants until the maximum bid is met.
The program should output a message with the winning bid.

Input Example
1600
800
1300
1700

Output Example
Sold: 1700
"""
maxBid = int(input()) # recibe una entrada y la convierte en un int

while(True):  #  realiza un condicion
    bid = int(input())   # recibe una entrada y la convierte en un int
    if bid>maxBid:  #  realiza una condicion
        break   # termina el bucle si la condicion anterior es verdadera
print("Sold:", bid)  #  imprime una texto y una variable

