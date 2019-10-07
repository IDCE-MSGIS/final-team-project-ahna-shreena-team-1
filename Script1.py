'''
#Name: Ahna Knudsen and Shreena Pyakurel
# Assignment title: Final Project- Web-scraping Weather Forecast
# Date: 10/04/2019
# Description: The script web-scrapes the weather.gov website to extract the 5-Day weather forecast for a given location
# Inputs: Latitude & Longitude in Decimal Degrees
# Outputs: 5-Day Weather Forecast
# Time:90 minutes
'''

# import required libraries
import requests
from bs4 import BeautifulSoup

# List to store response
forecast = []

## Provide the latitude and longitude for the location you would like to check the forecast for
## Lat/lon in decimal degrees provided for Worcester, MA
#add in user input to specify latitude and longitude
#use the str function to convert latitude values into strings type 
lat = str(input("Latitiude of your choice within the US: "))
lon = str(input("Longitude of your choice within the US: "))


# Create url for the requested location through string concatenation
url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon
# Check if the URL exists- incremental testing
print (url)

# Send request to retrieve the web-page using the get() function from the requests library
# The page variable stores the response from the web-page
page = requests.get(url)

# Create a BeautifulSoup object with the response from the URL
# Access contents of the web-page using .content
# html_parser is used since our page is in HTML format
soup=BeautifulSoup(page.content,"html.parser")

# Locate elements on page to be scraped
# findAll() locates all occurrences of div tag with the given class name
# stores it in the BeautifulSoup object
weather_forecast = soup.findAll("li", {"class": "forecast-tombstone"})
# Loop through the BeautifulSoup object to extract text text from every class instance using .text
# Store results in a list
for i in weather_forecast:
    i = i.text
    forecast.append(i)


# Print list to remove unicode characters
#used forloop to iterate through forcast and used .replace function to clean up spacing in output
for day in forecast:
 # day = day.replace('\n',)
 # day = day.replace('High', ' High') #tried different spacing options
  day = day.replace('Sunny', 'Sunny, ')
  day = day.replace('Clear', 'Clear, ')
  day = day.replace('Sunny,', 'Sunny, ')
  day = day.replace('Patchy', 'Patchy ')
  day = day.replace('Frost', 'Frost ')
  day = day.replace('Likely', 'Likely ')
  day = day.replace('Chance', 'Chance ' )
  day = day.replace('Cloudy', 'Cloudy ')
  day = day.replace('Mostly', 'Mostly ')
  day= day.upper() #capitalize every letter 
  print day
