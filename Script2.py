# Ahna Knudsen and Shreena Pyakurel
# Final Project Part 2
# due: October 6, 2019
#Assignment Description: 
# time: 3 hours 


area_list = [14400, 28800, 43200]
print "Plot 1 area is: ", + area_list[0]
print "Plot 2 area is: ", + area_list[1]
print "Plot 3 area is: ", + area_list[2]
#print "plot_length is: ", + length, "inches"
#print "plot_width is: ", + width, "inches"

#now convert to inches because rainwater is measured in inches
# Since you are converting area from feet sq to inches sq, you want to multiply the area value by 144 instead of 12.
area_inches = [i * 1 for i in area_list]
print (area_inches)

rainfall_inches = 1
runoff_inches = [i * rainfall_inches for i in area_inches]
print runoff_inches

#convert cubic inches to gallons: divide the volume value by 231

runoff_gallons = [i/ 231 for i in runoff_inches]
#print "runoff_gallons is: ", +  runoff_gallons
print runoff_gallons
print "Plot 1 rainfall is: ", + runoff_gallons[0],"gallons"
print "Plot 2 rainfall is: ", + runoff_gallons[1],"gallons"
print "Plot 3 rainfall is: ", + runoff_gallons[2],"gallons"
   
#asking the user what plot they would like to know the runoff for

def ask_user_():
    ask_user = raw_input("which plot would you like to know the runoff for?")
    if ask_user == "plot 1":
        print runoff_gallons[0]
    elif ask_user == "plot 2":
         print runoff_gallons[1]
    elif ask_user == "plot 3":
        print runoff_gallons[2]
    #after finding out the runoff for one plot keep going to find the runoff for next plot 
    cont= raw_input('do you want to find the runoff for another plot y/n')
    if cont == 'y':
        ask_user_()
    else:
        print 'done' 
    
print ask_user_()
