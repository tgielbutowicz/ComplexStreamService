import urllib2
import ctypes
from HTMLParser import HTMLParser

# Grab image url
response = urllib2.urlopen('http://apod.nasa.gov/apod/astropix.html')
html = response.read()

class MyHTMLParser(HTMLParser):


    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   if value[len(value)-3:len(value)]=="jpg":
                       #print value
                       self.output=value

parser = MyHTMLParser()
parser.feed(html)
imgurl='http://apod.nasa.gov/apod/'+parser.output
print imgurl

# Save the file
img = urllib2.urlopen(imgurl)
localFile = open('desktop.jpg', 'wb')
localFile.write(img.read())
localFile.close()

# set to desktop(windows method)
#SPI_SETDESKWALLPAPER = 20
#ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "desktop.jpg" , 0)