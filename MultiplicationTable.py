""" This program asks the user for a starting number and a ending number in the x range
 then asks for the ending y range. This program then computes a multiplication table.
 By: Joe McCaffrey
 """


# Ask user for the inbound x value, outbound x value and the y value and store it
INBOUND_X = int(input("What is the starting integer n value? "))
RANGE = int ( input ( "What is the range of the table? "))
OUTBOUND_X = int(input("What is the ending integer n value? "))




#Set up the table heading

print("%5s|%5s|" % ("x","x*n"))
print("-----|-----|")


#Use the for loop to compute the table and print the answers

for x in range (INBOUND_X,OUTBOUND_X +1,):
    a = x*RANGE
    print ("%5d|%5d|"  % (x,a))

      




 
 
