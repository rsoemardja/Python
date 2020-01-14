# we are going to be taking a look at logic with if Statements
# Their is actually a hidden error
# The error is that computer looks at each statement
# and is 120 > 90. It is indeed and the else would execute but the else DID not excute hence the logic error
temperature=input("What is the temperature in Fahrenheit? ")
temperature=int(temperature)

if temperature > 90:
    print("It is hot outside.")
elif temperature > 110:
    print ["Oh man, you could fry egg on the pavement"]
elif temperature < 30:
    print ("It is cold outside.")
else:
    print("It is not hot outside")

print ("Done")

# This is now correct and now the statement should be okay
temperature=input("What is the temperature in Fahrenheit? ")
temperature=int(temperature)

if temperature > 110:
    print("It is hot outside.")
elif temperature > 90:
    print ["Oh man, you could fry egg on the pavement"]
elif temperature < 30:
    print ("It is cold outside.")
else:
    print("It is not hot outside")

print ("Done")
