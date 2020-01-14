#This is about while loop

#This is a for loop here
for i in range(10):
    print (i)

# If you want to code a faster loop process you would use for loop
#While loop is more flexible

# i =0 is the init counter condition(initialisaion counter)
# and we have got a increment i += 1
i=0
while i<10:
    print (i)
    i += 1
# And we get the same output as the for loop
#It will repeat the 0 all the time
i=0
while i <= 2*32:
    print (i)
    i *= 2
#with i=1  it will root the value then it will power the value up to 32
# This is an example of a while loop
i=1
while i <= 2*32:
    print (i)
    i *= 2

#Another Example of a while loop is this
#
quit="n"
while quit == "n":
    quit = input("Do you want to quit?")

#done = False    
#while done == False:
#This key word not and make it the opposite
#done = False
#while not(done):

done=False
while not (done):
    quit = input("Do you want to quit? ")
    if quit == "y":
        done - True

    attack = input("Does your elf attach the dragon? ")
    if attack == "y":
        print = True

value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)

# Common problems with while loops

#The programmer wants to count down from 10
# What is wrong and how to fix it?
i = 10
while i == 0:
    print(i)
    i -= 1


#What is wrong with this loop that tries to count to 10? Whap will happen it is run?
#
i = 1
while i < 10:
    print(i)