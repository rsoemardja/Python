#if you want to implement/use random numbers YOU SHOULD write on top of the program is import
# use sin and cosine(cos) 
# a common error is that people save this file as a random.py DON't do that as a reference for the future
import random

# This picks a random number from 0 to 49
# If you have a function like randrange you NEED to do something

# This is a common error
#random is the the library 
# randrange is the function 
#and the () is the parameters that you assign onto the function
ramdom.randrange(50)

# now How do you store a function

my_number = random.randrange(50)

# This picks a random number from 100 to 200
my_number = random.randrange(100,201)

# This will select the random idem out of the my_list
my_list = ["rock", "paper", "scissors"]
random_index = random.randrange(3)
print(my_list[random_index])

# It will get a random floating point number from 0 to 1
my_number = random.random()

# it will pick a random floating point number between 10 to 15
my_number = random.random() * 5 + 10