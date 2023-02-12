"""
Open or Closed

The store is open every day from 10 to 21, except on Saturday and Sunday.
The given program takes the day and the hour as input.

Task
Complete the program to output whether a store is Open or Closed, based on the day of the week and the hour.
The day of the week is represented as an integer (1 for Monday, 2 for Tuesday, etc.)

Input Example
4
15

Output Example
Open

"""
day = int(input())  #  pide una entrada y la convierte esta cadena en un int
hour = int(input())  #  pide una entrada y la convierte esta cadena en un int

if 6 > day and hour > 10 and 21 > hour:  #  realiza una comparacion triple
    print("Open")  #  en caso de que las 3 comparaciones sean verdaderas realiza una impresion
else:  #  en caso de que no se cumpla la condicion
    print("Closed")  #  raliza esta impresion
