#Python string operations and functions

#1 - Variables

first_name = "mandar"
last_name = "kulkarni"

#2 - print variables with a string

print("First Name :" + first_name)
print("Last Name :" + last_name)

#3 - concatenate strings

full_name = first_name + ' ' + last_name

print("Full name :" + full_name)

#4 - list of hobbies

hobbies = ['movies', 'tennis', 'cricket', 'reading' ]

#5 print first hobby

print(first_name + "'s hobby " + hobbies[0])

#6 print all hobbies

for hobby in hobbies:
    print(full_name + "'s hobbies " + hobby)


#7 add a new hobby

hobbies.append('trekking')

#8 print hobbies

print(hobbies)
