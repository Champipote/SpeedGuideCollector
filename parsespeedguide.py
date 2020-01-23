"""parsespeedguide.py: 
This script aims at collecting the 40+ webpages of the ports used by malwares according to the website SpeedGuide.net 
to collect the knowledge in one place and to avoid network connectivity requirement."""

__author__ = "Tristan Pinceaux"
__copyright__   = "Copyright 2020, Tristan Pinceaux"
__license__ = "GPL"
__version__ = "1.0"

import urllib.request # to make GET query to speedguide.net
import urllib.parse # to parse the server response
import re # to use Regular Expression

result = """<html><head><title>Ports used by Malware - SpeedGuide</title>
<style type="text/css">
table.ports {width: 100%; margin: auto;}
table.ports, table.ports td, table.ports th {border: 1px solid #AAAAAA; padding: 3px;}		
table.ports th {background: #D4D4D4;}
table.ports th a:link, table.stats th a:visited {text-decoration: none;}
table.ports th a:hover, table.stats th a:active {text-decoration: underline;}
tr.ports {cursor: pointer; background: #F4F4F4;}
tr.ports:hover {background: #E4E4E4;}
html, body {background: #3a484c;margin: 0;padding: 0;height:100%;scrollbar-base-color: #3a484c;scrollbar-face-color: #576267;scrollbar-track-color: #3a484c;scrollbar-arrow-color: #9faaac;scrollbar-highlight-color: #9faaac;scrollbar-3dlight-color: #576267;scrollbar-shadow-color: #000000;scrollbar-darkshadow-color: #000000;}
::selection {color: #ffffff;background: #1e6a8e;}
::-moz-selection {color: #ffffff;background: #1e6a8e;}
body,p,table,td,th,div,ul,ol {font: normal 15px Arial, Helvetica, sans-serif;}
table,td,th {margin: 0;padding: 0;border: 0;border-spacing: 0;border-collapse: collapse;}
th, th a {text-align: center;vertical-align: middle;white-space: nowrap;font-weight: bold;}
td {text-align: left;vertical-align: top;}
</style>
</head><body><table class='ports'>"""
print(result) # to add HTML format and CSS

url = "http://speedguide.net/ports_sg.php?sort=port&page="

for i in range(100):
    f = urllib.request.urlopen(url+str(i))
    response = f.read().decode('utf-8')

    searchObj = re.search("<table class=\"ports\">(.*)<br>Vulnerabilities",response,re.MULTILINE | re.DOTALL) #find only table content which is the interesting part (Ports and Malware that use them)

    if len(searchObj.group(1)) >= 400:
        print("<table class='ports'>") #Add the class ports on the next table for CSS
        print(searchObj.group(1))
    else:
        break

print("</body></html>")

    
