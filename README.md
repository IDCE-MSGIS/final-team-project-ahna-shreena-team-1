## Final Project Documentation  
### Ahna Knusden and Shreena Pyakurel 
### October 6, 2019
### Time: 75 minutes 

### Script 1 Project Description: Web-scraping Weather Forecast Information with Python
The goal for part one of the lab was to modify an existing python code that web scrapes weather data from a library that was provided to us. The code that we were given took the latitude and longitude of Worcester, Massachusetts and scraped the web for the weather report of the following seven days. Our first goal for this project was to change the script so that the user had to type in a latitude and longitude of their choice instead of defining the latitude and longitude. We did this by using the raw.input function. After this, we used the str function to convert the latitude and longitude from float type data to a string type data. After the user input the desired coordinates, we checked if the URL existed online to ensure that the data we were scraping for actually existed. Next, the script extracted information from the National Weather Service using the beautiful soup library. Then after our information was scraped from the web, all of the formatting in the output was incorrectly displayed. This lead us to our next goal which was to clean up the code to make sure everything was spaced correctly and formatted in a way that was legible and visually pleasing. We utilized the .replace() function in a for-loop. Finally, we converted all of the characters to uppercase to fulfill one of the requirements. 

For the most part, the code worked as we planned it to. Every time a user input a desired latitude and longitude, the code successfully scraped the web for weather for the desired location. One of the challenges that we faced was that occasionally certain coordinates did not scrape well, and in order to have the coordinates scraped successfully, the latitude and longitudes needed to have a specific set of coordinates in the United States. Additionally, every time we input another set of latitude and longitude coordinates, the formatting significantly changed. Web scraping is a powerful tool and this specific script works well for extracting data really fast. However, the script could be improved for use in the future so that the formatting would not change every time we input a new set of coordinates. 


### Script 2 Project Description: Raw Input and Calculating Runoff for Plots of Land 
Our goal for the script of Part 2 was to recreate the first python lab with adding user input, for loops, and if statements. The lab involved calculating the volume of runoff for a plot of paved land (i.e. no absorbtion) in a 1 inch rainstorm in Kenya. Our project modified the lab by calculating runoff for multiple plots of land using for loops. We also converted between feet squared, inches squared, and gallons. At the end we asked for the user to type the plot they want to know runoff information for. Hence, the required inputs are a list of areas in feet squared, the amount of rainfall in inches, and user input of desired plot information. The outputs are the amount of runoff in gallon for each plot that the user asks to know about and a done statment when the user is done asking.  Using this code, runoff could be calculated for any area and amount of rainfall. This is helpful for storing calculations and information about many different plots of land. 
Writing the code was straightforward for the most part. If was helpful to use incremental development and execute print statements after new variables, for loops, and if statements. This helped to identify what was working and navigate where the problems were. We struggled with doing conversions on the lists with for loops. Using Stackoverflow (https://stackoverflow.com/questions/40973081/list-comprehensions-and-one-line-for-loops) we found that we could use for loops in defining the variable to clean up the code and get it to apply the operation on each index. We also struggled with the output only giving one plot, although we wanted to continue asking. We got help from Priyanka who suggested writing a second question and a second for loop. 
Overall, the code outputs runoff for plots of land. It improved our knowledge of various uses of for loops, specifically by doing conversions of a list in defining new variables, and asking the user multiple questions. It also heighted our debugging skills by using incremental testing.  


