"""
Countdown
Create a timer program that will take the number of seconds as input, and countdown to 0.

Input Example
3
Output Example
3
2
1
0
"""

number = int(input())  #  solicita un numero al usuario lo convierte en int y lo guarda en una varible  
while number>=0:  #  realiza una conficion
    print(number)  #  imprime una variable
    number -=1  #  resta 1 a un variable
