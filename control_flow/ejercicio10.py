"""
BMI Calculator

Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²
The resulting number indicates one of the following categories:
Underweight = less than 18.5
Normal = more or equal to 18.5 and less than 25
Overweight = more or equal to 25 and less than 30
Obesity = 30 or more

Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

Sample Input
85
1.9
Sample Output
Normal
"""
#tu código va aquí
peso = int(input())  #  pide una entrada de texto y la convierte en un int
altura = float(input())  #  pide una entrada de texto y la convierte en un float
IMC = peso/(altura*altura)  #  realiza una operacion y la guarda en una variable
if IMC < 18.5:  #  realiza una condicion
    print("Underweight")  #  realiza un impresion si la condicion anterior es verdadera
elif IMC > 18.5 and IMC < 25:  #  realiza una condicion si la condicion anterior no se cumple
    print("Normal")  #  realiza un impresion si la condicion anterior es verdadera
elif IMC > 25 and IMC < 29.9:  #  realiza una condicion si la condicion anterior no se cumple
    print("Overweight")  #  realiza un impresion si la condicion anterior es verdadera
elif IMC > 30:  #  realiza una condicion si la condicion anterior no se cumple
    print("Obesity")  #  realiza un impresion si la condicion anterior es verdadera
    
