import requests 
from bs4 import BeautifulSoup 
import ctypes

# Make a request to the url formula
def getdata(url): 
    r = requests.get(url) 
    return r.text 

# Identify image url
htmldata = getdata("https://apod.nasa.gov/apod/astropix.html") 
# Parse image
soup = BeautifulSoup(htmldata, 'html.parser') 
# When the image is found, print the url
for item in soup.find_all('img'):
    url = "https://apod.nasa.gov/apod/"+item['src']
    print(url)

# Move image to local
img_data = requests.get(url).content
with open('PATH/astropix.jpg', 'wb') as handler:
    handler.write(img_data)

# Change the background   
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, 'PATH/astropix.jpg' , 0)
