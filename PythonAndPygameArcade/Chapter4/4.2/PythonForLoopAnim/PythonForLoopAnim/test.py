# This will only print Hello 5 times and There 1 time
# Because the for loop is asscociated with the indent and the unindented line is not 
for i in range(5):
    print ("Hello")
print ("There")

# This code everything indented is associated with the for loop
for i in range(5):
    print ("Hello")
    print ("There")