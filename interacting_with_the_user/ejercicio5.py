"""
Bank Account Balance

Imagine you need to build a program for ATMs to calculate and display the balance remaining after a withdrawal.
The given takes the balance and the withdrawal as input.

Task
Complete the program to calculate and output the remaining balance after the withdrawal in the given format

Input Example
100
30

Output Example
Your balance: 70
"""
balance = int(input())  #  guarda la entrada que realiza el usuario en una variable y la convierte en un int
withdraw = int(input())  #  guarda la entrada que realiza el usuario en una variable y la convierte en un int
print("Your balance:", (balance-withdraw))  #  Imprime una cadena de texto junto a unas varbales las cuales estan realizando una resta
