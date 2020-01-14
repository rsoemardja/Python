# you could write functions Multiple times 
# it  works greats but  its just monotonous if you to it 100, 100 times etc.
print("I will not chew Gum in Class")
print("I will not chew Gum in Class")
print("I will not chew Gum in Class")
print("I will not chew Gum in Class")

# i have using a for loop 5 times
#it does the same function as the top 
# the range() function lets us loop a certain number of times
# the i or whatever you want to call it is the variable
for i in range(5):
    print("I will not chew gum in class.")

# What i am going to do is print i 
# the number it within the loop is the number 0
# this will NOT loop up to the number given on the range it will print number of times given on the range
for i in range(5):
    print("i")

#If i want to get THE numbers 1-5 i could do this 
for i in range(1, 6):
    print("i")
#Or this  make the print out the number + 1 as the result given
for i in range(5):
    print(i+1)

#If i want to print even numbers from 1 to 100 i could do the following
# 2 is the start, 100 is the end and the last int 2 is the step amount
for i in range(2,100,2):
    print(i)
#if i want to include the number 100 i change the number 100 to 101
for i in range(2,101,2):
    print(i)

#If i want to do a countdown from 100 down to 0 but NOT including 0
for i in range(100,0,-1):
    print(i)
#If you want to include the number 0
for i in range(100,-1,-1):
    print(i)

# And keep in mind that indentations are VERY important
# this is NOT included in the loop
for i in range(5):
    print("Please,")
print ("Can i go to the mall")
#where as this one it is
for i in range(5):
    print("Please,")
    print ("Can i go to the mall")

print ("Aww.")
#you CAN't indent and unindent a statement because it acts as if a loop  is happening
#it will get an error "unexpected indent because in the code you indented but you their is no if statement and it detects that their is a problem
    print("But i Really want to")
#The loop functions(for, while e.t.c) are universal in other programming languages