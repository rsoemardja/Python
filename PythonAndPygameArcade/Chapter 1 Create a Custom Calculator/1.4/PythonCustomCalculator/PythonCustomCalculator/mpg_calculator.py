#This is code that just gives an answer
# milesDriven=294
# gallonsUsed=10.5
# mpg=milesDriven/gallonsUsed
# print(mpg)

# This is almost complete
#With this input function i will create a input prompt and they followed by entering a string
# This Works a lot like a print statement, it will stop the user and ask the user to type the variable
# milesDriven=input("Enter miles driven: ")
# gallonsUsed=input("Enter gallons used: ")
# mpg=milesDriven/gallonsUsed
# print (mpg)
#This is a common error because it is treated as text
# because since you cannot divide text 
# You need to the treat it as if the value is a number

#This is a nested function with integers
#nesting is typically confusing for new coders.
milesDriven=int (input("Enter miles driven: "))
gallonsUsed=int (input("Enter gallons used: "))
mpg=milesDriven/gallonsUsed
print (mpg)

#Or i could do the same as the top code above but with two lines
#You are telling the computer that you are treating the users values at integers instead of strings
#int Handles integers that are Whole Numbers
milesDriven=input("Enter miles driven: ")
# if you know it is a integer use int
#the computer can handle int number faster than float number so be sure of what you are using
milesDriven = int(milesDriven)
gallonsUsed=input("Enter gallons used: ")
gallonsUsed = int(gallonsUsed)
mpg=milesDriven/gallonsUsed
print ("Your mpg:",mpg)

# float(floating point Variable) Handles integers with decimals
milesDriven=input("Enter miles driven: ")
#if what you are working on has a decimal point use float
milesDriven = float(milesDriven)
gallonsUsed=input("Enter gallons used: ")
gallonsUsed = float(gallonsUsed)
mpg=milesDriven/gallonsUsed
print ("Your mpg:",mpg)


#if you wanted to apply real calculative  equations/examples like kinetic energy do it like  flowchart like so

#Final Calculator
# Get data from user
milesDriven=input("Enter miles driven: ")
milesDriven = float(milesDriven)
gallonsUsed=input("Enter gallons used: ")
gallonsUsed = float(gallonsUsed)
# Do calculation
mpg=milesDriven/gallonsUsed

# print Result
print ("Your mpg:",mpg)