"""
Take your kindle!

Airlines are running a special promotion for teenagers that offer them kindles to use during the flight.

Task
Write a program to take the passengers' age as input and output 'Take your kindle!' if the age is under or equal to 19.

Sample Input
14

Sample Output
Take your kindle!
"""
edad = int(input())  #  guarda la entrada que realiza el usuario en una variable y la convierte en un int
if edad <= 19 :  #  realiza la condicion si es verdadera o no
    print("Take your kindle!")  #  imprime una cadena de texto la cual sera imprimida solo si la condicion de arriba es verdadera
