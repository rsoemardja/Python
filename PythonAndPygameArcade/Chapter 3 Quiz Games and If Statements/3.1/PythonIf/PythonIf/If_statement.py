# I will write a standard  input function
input("What is the temperature? ")


# i want to print the answer to the input but the problem is that it is not recorded
# by doing temperature = i am assigning temperature to a variable 
temperature=input("What is the temperature? ")
print (temperature)

# if i write it like this the computer doesn't know if it is a int (number)  
temperature=input("What is the temperature? ")
print (temperature+1)

# If i put double quotes onto the number it will simply add a the number 1 to the number you inputted
# If i do it like this i am simply tacking the number on to the question but it is NOT a integer
# I could put a string in this question i.e Jim70
temperature=input("What is the temperature? ")
print (temperature+"1")

# now i am going to converts this to a int(number) variable
# so that when i am going input a number it won't just tack on the number it will act as a int
temperature=input("What is the temperature? ")
temperature=int(temperature)
print (temperature+"1")

# So now i am going to apply an if statement 
temperature=input("What is the temperature? ")
temperature=int(temperature)
# All if statements MUST end with a colon :
# Only The print statements with if iare ALWAYS indented automatically 
if temperature > 90:
    print("It is hot outside.")
    # This one is not indented
    # Note that if i write the value of 90 it WILL not output the print statement because it is not greater than itself
print ("Done")

# With this i will i have put the >= greater than or equal to so that i input my value 90 and it print the message
temperature=input("What is the temperature? ")
temperature=int(temperature)

if temperature >= 90:
    print("It is hot outside.")

print ("Done")

# i could do  < (less than) or <= (less than or equal to)
temperature=input("What is the temperature? ")
temperature=int(temperature)

if temperature <= 90:
    print("It is hot outside.")

print ("Done")

# This is a common error as this is a syntax error (typing/input error)
# and the reason is that = is that of an assignment
temperature=input("What is the temperature? ")
temperature=int(temperature)

if temperature = 90:
    print("It is hot outside.")

print ("Done")

# we are going to query whether something is == equal to
#with == equals you are ASKING whether the value is equal to each other
#inside the if statmennt you'll never want a single = sign, you'll want a == sign
temperature=input("What is the temperature? ")
temperature=int(temperature)

if temperature == 90:
    print("It is hot outside.")

print ("Done")

# This is NOT equals 
#Unless exactly equals it will print the if text
temperature=input("What is the temperature? ")
temperature=int(temperature)

if temperature != 90:
    print("It is hot outside.")

print ("Done")

# This is about the else statement
#else statements NEEDS to be indented otherwise it is not a valid statement
temperature=input("What is the temperature? ")
temperature=int(temperature)

if temperature >= 90:
    print("It is hot outside.")
else:
    print("It is not hot outside")

print ("Done")

# elif (else if) a strange hybrid statement
#if it is not above 90 it will skip the if statement
temperature=input("What is the temperature? ")
temperature=int(temperature)

if temperature >= 90:
    print("It is hot outside.")
elif temperature < 30:
    print ("It is cold outside.")
else:
    print("It is not hot outside")

print ("Done")