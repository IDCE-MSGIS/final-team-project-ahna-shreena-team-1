# Ahna Knudsen and Shreena Pyakurel
# Final Project Part 2
# due: October 6, 2019
# time: 


area_list = [100, 200, 300]
print "Plot 1 area is: ", + area_list[0]
print "Plot 2 area is: ", + area_list[1]
print "Plot 3 area is: ", + area_list[2]
#print "plot_length is: ", + length, "feet"
#print "plot_width is: ", + width, "feet"

#now convert to inches because rainwater is measured in inches
# Since you are converting area from feet sq to inches sq, you want to multiply the area value by 144 instead of 12.
area_inches = [i * 144 for i in area_list]
print (area_inches)

rainfall_inches = 1
runoff_inches = [i * rainfall_inches for i in area_inches]
print runoff_inches

#convert cubic inches to gallons: divide the volume value by 231
runoff_gallons = [i/ 231 for i in runoff_inches]
#print "runoff_gallons is: ", +  runoff_gallons
print runoff_gallons

#get user input for which plot runoff to output
ask_user= str(input('Type which plot you would like to know the runoff for. Options are: Plot 1, Plot 2, Plot 3. ' )) 
# define function for what to do with the user's input
def plot_output(ask_user):
  if ask_user == "Plot 1": 
    print "Plot 1 runoff is: ", + runoff_gallons[0] 
  elif ask_user == "Plot 2":
    print "Plot 2 runoff is: ", + runoff_gallons[1]
  elif ask_user == "Plot 3":
    print "Plot 3 runoff is: ", + runoff_gallons[2]
  else: #for values less than 32
    print "Try again."
#call the function with arguement as ask_user
plot_output(ask_user)
# here is where we get an EOF error, except the else past of the if statement works 

#_____________________________________
#new code
area = [100,200,300]
area_inches = [i * 12 for i in area]
print(area_inches)

for i in area_inches:
    rainfall_inches_is = area*1
    rainfall_gallon_is = (rainfall_inches_is / gal_convert)
#test

'''
plot_length_is = 50 *12


plot_width_is = 20 *12


#calculate Area
area = plot_length_is * plot_width_is


#calculating rainfall in inches
rainfall_inches_is = area*1  

#conversion value 
gal_convert = 231

#rainfall in gallon 
rainfall_gallon_is = (rainfall_inches_is / gal_convert)


#Total runoff in gallons
print ('plot_length_is', plot_length_is)
print('plot_width_is', 
plot_width_is)
print ('area', area)
print (' rainfall_gallon_is', rainfall_gallon_is)
'''
