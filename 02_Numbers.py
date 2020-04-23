# Python numeric operations and functions

#import random library

import random


name = "mandar kulkarni"
age = 35

print(age)

# print fibonacci series of 10 mumbers

n1,n2 = 0,1

series = []   #adding to a list. create empty list

count = 0

while count <= 10:     #simple while loop
    series.append(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count = count+1

print("Fibonacci sequence")

print(series)


# print squares

squares = []    #adding to a list. create empty list

for x in range(1,10):             #simple for loop
    squares.append(x**2)

print("Printing squares of numbers from 1 to 10")

print(squares)


# random number and user input - program feeling lucky

game_start = input("Do you want to play Feeling Lucky! Enter Y to play any other character to exit ")

while game_start == 'Y':   # use == for conditon check
                   user_num = input("Enter a number between 1 to 10! ")

                   print("You have entered - ")
                   print(user_num)
                   
                   random_num = random.randint(1,10)

                   print("Lucky number is - ")
                   print(random_num)

# if else statement
                   if int(user_num) == random_num:
                       print("Its your lucky day today! Go to Vegas!")

                       cont_play = input("Do you want to play again? ")

                       game_start = cont_play
                   else:
                       print("Try again")

                       cont_play = input("Do you want to play again? ")

                       game_start = cont_play


