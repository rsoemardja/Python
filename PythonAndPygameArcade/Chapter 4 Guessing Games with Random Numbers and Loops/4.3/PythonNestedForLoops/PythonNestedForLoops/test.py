# We will start with code like so
#The brackets means that how many times it will be repeated
for i in range(3):
    print ("a")
for j in range(3):
    print("b")

#This will loop 3 times and the for loop in the indentation will loop 3 times
# but with b since the loop is 3 times and b's loop 3 times b will be printed 9 times
# This is called a NESTED loop
for i in range(3):
    print ("a")
    for j in range(3):
        print("b")

# this is the same as the top one but it will print 5 a's and 10 b's within each loop
# This is a nested loop
for i in range(5):
    print ("a")
    for j in range(10):
        print("b")
#Where as this one is NOT a nested loop
# This one will not multiply like nested loop it will only add
for i in range(5):
    print ("a")
for j in range(10):
    print("b")