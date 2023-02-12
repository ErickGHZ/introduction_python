"""
Boolean Logic

Given the age of a person as an input, output their age group.
Here are the age groups you need to handle:

Child: 0 to 11
Teen: 12 to 17
Adult: 18 to 64

Sample Input
42

Sample Output
Adult
"""

age = int(input())  #  pide una entrada y la convierte esta cadena en un int
if age > 0 and age < 11:  #  realiza una comparacion doble
    print("Child")  #  en caso de que las 2 comparaciones sean verdaderas realiza una impresion
elif age > 12 and age <17:  #  si la primera comparacion doble es falsa realiza otra comparacion doble
    print("Teen")  #  en caso de que las 2 comparaciones sean verdaderas realiza una impresion
elif age > 18 and age < 64:  #  si la primera comparacion doble es falsa realiza otra comparacion doble
    print("Adult")  #  en caso de que las 2 comparaciones sean verdaderas realiza una impresion
    
