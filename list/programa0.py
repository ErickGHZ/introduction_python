"""
List Functions

You are working on a queue management program.
The queue is represented by a list. 
Write a program to take an input, add it to the end of the queue, and output the resulting list.
"""
queue = ['John', 'Amy', 'Bob', 'Adam']  #  crea una list
x= input()   #  guarda una entrada en una variable
queue.insert(x)  #  inserta en la list la varibale
print(queue)  #  impreme las list
