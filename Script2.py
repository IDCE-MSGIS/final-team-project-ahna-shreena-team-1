# Ahna Knudsen and Shreena Pyakurel
# Final Project Part 2
# time: 

# ahna's lab 1 code

length = 50
width = 20
area = (length * width) 
#print (area)
print "plot_length is: ", + length, "feet"
print "plot_width is: ", + width, "feet"

#now convert to inches bc rainwater is measured in inches
# Since you are converting area from feet sq to inches sq, you want to multiply the area value by 144 instead of 12.
area_inches = area * 144
#print (area_inches)

rainfall_inches = 1
runoff_inches = area_inches * rainfall_inches
print "rainfall_inches is: ", + runoff_inches

#convert cubic inches to gallons: divide the volume value by 231

runoff_gallons = runoff_inches/ 231
print "runoff_gallons is: ", +  runoff_gallons

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
