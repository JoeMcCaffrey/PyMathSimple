#This program asks for the distance in light-years, converts into miles /
#and then displays the distance

#By: Joseph McCaffrey


#Ask user for the distance in light-years
DISTANCE =float(input("Please enter distance in light-years:"))


#Declare speed of light in miles per minute
MILES_PER_MINUTE = 11176943.8 
MINUTES_IN_A_YEAR = 525949

#Compute the conversion and store them, computes to minutes
#Then computes to miles
MINUTES= DISTANCE * MINUTES_IN_A_YEAR
MILES= MINUTES * MILES_PER_MINUTE

#Display the distance

print ("The distance in miles is " + str (MILES))
