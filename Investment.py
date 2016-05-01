"""
This program will compute and display an investment report
It will ask for an intial amount to be invested, a period of years, and an intrest rate


By: Joe McCaffrey

"""

# Accept the inputs for the number of years, balance and intrest rate

START_BALANCE = float( input ("Please enter the initial amount: "))
YEARS = int (input ("Please enter the number of years: "))
RATE = int (input ( "Pleas enter the intrest rate as a %: "))

# Convert the rate to a decimal
RATE = RATE / 100

# Initialize the accumulator for the intrest
TOTAL_INTREST = 0.0

# The header for the table

print ("%4s%18s%10s%16s" % \
       ("Year", "Starting balance", "Intrest", "Ending balance"))

# compute the results for each year
for YEAR in range (1, YEARS+1):
    INTREST = START_BALANCE * RATE
    END_BALANCE = START_BALANCE + INTREST
    print ("%4d%18.2f%10.2f%16.2f" % \
           (YEAR, START_BALANCE, INTREST, END_BALANCE))
    START_BALANCE = END_BALANCE
    TOTAL_INTREST += INTREST
# display the totals

print ("Ending balance: $%0.2f" % END_BALANCE)
print ("Total intrest earned: $%0.2f" % TOTAL_INTREST) 

