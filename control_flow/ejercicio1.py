"""
if Statements

Write a program that checks if the water is boiling.
Take the integer temperature in Celsius as input and output "Boiling" if the temperature is above or equal to 100.

Sample Input
105

Sample Output
Boiling
"""
temp = int(input())  #  guarda la entrada que realiza el usuario en una variable y la convierte en un int
if temp >= 100:  #  realiza la condicion si es verdadera o no
   print("Boiling")  #  imprime una cadena de texto la cual sera imprimida solo si la condicion de arriba es verdadera
    