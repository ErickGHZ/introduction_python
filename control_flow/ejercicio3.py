"""
else Statement

Write a program to control entrance to a club.
Only people who are 18 or older are allowed to enter the club.
Your program takes the age of the person who tries to enter, and outputs "Allowed"  if they are allowed to enter the club, and "Sorry" if they are younger than the allowed age.

Sample Input
24

Sample Output
Allowed
"""
age = int(input())  #  guarda la entrada que realiza el usuario en una variable y la convierte en un int
if age > 18:  #  realiza la condicion si es verdadera o no
    print("Allowed")  #  imprime una cadena de texto la cual sera imprimida solo si la condicion de arriba es verdadera
else:  #  realiza la condicion si es ni verdadera 
    print("Sorry")  #  imprime una cadena de texto la cual sera imprimida solo si la condicion de arriba es falsa
