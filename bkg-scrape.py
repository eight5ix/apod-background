import requests 
from bs4 import BeautifulSoup 
import ctypes

def getdata(url): 
    r = requests.get(url) 
    return r.text 
    
htmldata = getdata("https://apod.nasa.gov/apod/astropix.html") 
soup = BeautifulSoup(htmldata, 'html.parser') 
for item in soup.find_all('img'):
    url = "https://apod.nasa.gov/apod/"+item['src']
    print(url)
    
img_data = requests.get(url).content
with open('C:/Users/tkaplan/Documents/conda/ScrapeAPOD/astropix.jpg', 'wb') as handler:
    handler.write(img_data)
    
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, 'C:/Users/tkaplan/Documents/conda/ScrapeAPOD/astropix.jpg' , 0)
