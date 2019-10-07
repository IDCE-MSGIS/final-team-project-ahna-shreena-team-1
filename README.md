## Final Project 
## Ahna Knusden and Shreena Pyakurel 
## Oct/6/2019
## Time: 
#### Final Project: Documentation
### Web-scraping Weather Forecast Information with Python


### Script 1 project description: 
The goal for part one of the lab was to modify an existing python code that web scrapes weather data from a library that was provided to us. The code that we were given took the latitude and longitude of Worcester, Massachusetts and the scraped the web for weather for the following seven days. Our first goal for this project was to change the script so that the user had to type in a latitude and longitude of their choice instead of using a defined latitude and longitude using the raw.input function. After this, we used the str function to convert the latitude and longitude from float type data to a string type data. After the user input the desired coordinates, we checked if the URL existed online to ensure that the data we were scraping for actually existed. Next, the script extracted information from the National Weather Service using the beautiful soup library. And then after our information was scraped from the web, all of the formatting in the output were incorrectly displayed which leads us to our next goal which was to clean up the code to make sure everything was spaced correctly and formatted in a way that was visually pleasing using the .replace() function in a given for-loop. Finally, we converted all of the characters to uppercase to fulfill one of the requirements. 

For the most part the code worked as we planned it to. Every time a user input a desired latitude and longitude, the code successfully scraped the web for weather for the desired location. One of the challenges that we faced was that occasionally certain coordinates did not scrape well, and in order to have the coordinates scraped successfully, the latitude and longitudes needed to have a specific ser of coordinates in the United States. Additionally, every time we input another set of latitude and longitude coordinates, the formatting also significantly changed. I believe web scraping is a powerful tool and this specific script works well for extracting data really fast but, I would improve the script in a way so that the formatting would not change every time we input a new set of coordinates if I were to use this in the future. 
 

#### Final Project: Script 2
### Your Chosen Assignment
For this script, you will complete the assignment that you have proposed, which involves modifying a previous exercise. Remember to update the Script2.py file to include comments and documentation in your script to tell me what it’s doing!


For script 2, clearly explain what the goal of the script is; what inputs are required; what outputs are expected. Ideally, you’d have a real-life scenario in hand (e.g. “by allowing user input for the script to _______, we ensure that it can be easily run without a user needing to program in Python.”). That is only an example but should give you an idea for what I’m looking for. Additionally, you should describe the process of writing the script: was it easy, hard, what challenges or errors did you face and how did you resolve the issue? If you use any resources to help write your code (e.g. Stackoverflow.com; the text book; etc.) then please describe these in the body of the text. E.g. “After repeated syntax errors, I checked Stackoverflow.com to find that…”  If you can link to a specific thread or page that would be great.

https://stackoverflow.com/questions/40973081/list-comprehensions-and-one-line-for-loops  
### Script 2: 
Our goal for the script of Part 2 was to recreate the first python lab with adding user input, for loops, and if statements. The lab involved calculating the volume of runoff for a plot of paved land (i.e. no absorbtion) in a 1 inch rainstorm in Kenya. Our project modified the lab by calculating runoff for multiple plots of land using for loops. We also converted between feet squared, inches squared, and gallons. At the end we asked for the user to type the plot they want to know runoff information for. Using this code, runoff could be calculated for any area and amount of rainfall. This is helpful for storing calculations and information about many different plots of land. 
Writing the code was straightforward for the most part. If was helpful to use incremental development and execute print statements after new variables, for loops, and if statements. This helped to identify what was working and navigate where the problems were. We struggled with doing conversions on the lists with for loops. Using Stackoverflow (I forget the link???) we found that we could use for loops in defining the variable to clean up the code and get it to apply the operation on each index. 


This will require the user to interact with the code and an if statement for which units to output. In order to complete these steps, we will use incremental testing to build our problem solving and debugging skills. 



