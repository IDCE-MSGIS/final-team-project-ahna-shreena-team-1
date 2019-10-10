# Ahna Knudsen and Shreena Pyakurel
# Final Project Part 2
# Date: October 6, 2019
# Assignment Description: Finding plot area with conversions, for loops, and user input. 
# Time: 3 hours 

# input is in feet squared because area is measured in feet 
area_list = [100, 200, 300]
# To know start values, print area_list
print "Plot 1 area is: ", + area_list[0]
print "Plot 2 area is: ", + area_list[1]
print "Plot 3 area is: ", + area_list[2]

# Convert to inches because rainwater is measured in inches.
# When converting area from feet sq to inches sq, multiply the area value by 144.
# Used a for loop within the definition of the variable 
area_inches = [i * 144 for i in area_list]
#print (area_inches)

# Define rainfall as variable. (This could be defined as a larger integer depending on rainfall measurement.)  
rainfall_inches = 1
runoff_inches = [i * rainfall_inches for i in area_inches]
print runoff_inches

# To convert cubic inches to gallons: divide the volume value by 231
runoff_gallons = [i/ 231 for i in runoff_inches]
#print "runoff_gallons is: ", +  runoff_gallons
#print runoff_gallons
#print "Plot 1 runoff is: ", + runoff_gallons[0],"gallons"
#print "Plot 2 runoff is: ", + runoff_gallons[1],"gallons"
#print "Plot 3 runoff is: ", + runoff_gallons[2],"gallons"
   
# Ask the user what plot they would like to know the runoff for. Use if statement for all options of outputs (run off for each plot). 
def ask_user_():
    ask_user = raw_input("Which plot would you like to know the runoff for? Options are: plot 1, plot 2, or plot 3. ")
    if ask_user == "plot 1":
        #print runoff_gallons[0]
         print "Plot 1 has ", + runoff_gallons[0],"gallons of run off."
    elif ask_user == "plot 2":
         #print runoff_gallons[1]
         print "Plot 2 has ", + runoff_gallons[1],"gallons of run off."
    elif ask_user == "plot 3":
        #print runoff_gallons[2]
         print "Plot 3 has ", + runoff_gallons[2],"gallons of run off."
    # After finding the runoff for one plot, ask user if they want to know more or not. 
    cont = raw_input('Do you want to find the runoff for another plot? y/n')
    if cont == 'y':
        ask_user_()
    else:
        print 'Done' 
# Call function     
ask_user_()
