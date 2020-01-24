"""parsespeedguide.py: 
This script aims at collecting the 40+ webpages of the ports used by malwares according to the website SpeedGuide.net
then it parses the result to JSON format to collect the knowledge in one place and to avoid network connectivity requirement."""

__author__ = "Tristan Pinceaux"
__copyright__   = "Copyright 2020, Tristan Pinceaux"
__license__ = "GPL"
__version__ = "1.1"

import urllib.request # to make GET query to speedguide.net
import urllib.parse # to parse the server response
import re # to use Regular Expression
import json #to format in JSON

fulljson = ""
url = "http://speedguide.net/ports_sg.php?sort=port&page="

for i in range(100):
    f = urllib.request.urlopen(url+str(i))
    response = f.read().decode('utf-8')

    searchObj = re.search("<table class=\"ports\">(.*)<br>Vulnerabilities",response,re.MULTILINE | re.DOTALL) #find only table content which is the interesting part (Ports and Malware that use them)

    if len(searchObj.group(1)) >= 400:
        splitTR = searchObj.group(1).split("</tr>") #filtrer sur le contenu du tab qui est ce qu'on recherche
        j = 1 # On ne prend pas la première ligne qui contient les entêtes (=0)
                
        while j < len(splitTR)-1:
            splitTH = str(splitTR[j]).split("</th>") # Pour chaque port de la page
            splitTD = str(splitTH).split("</td>")
            port = re.search("port\">(.*)</a>",splitTD[0]).group(1) # Les ports peuvent contenir des "," ou des "-"
            protocol = re.search(";\">(\D+|$)$",splitTD[1]).group(1) # Le protocole peut être vide
            name = re.search(";\">(.*)$",splitTD[2]).group(1)
            scanned = re.search(";\">(.*)$",splitTD[3]).group(1) # Je n'utilise pas l'info scanned pour le moment pour rester fidèle au format whatportis
            description = re.search(";\">(.*)$",splitTD[4]).group(1)
            # Strip et escape de certains caractères contenus dans les descriptions
            description = description.replace("\\\\","doubleslash")
            description = description.replace("\\","")
            description = description.replace("doubleslash","\\\\")
            description = description.replace("'","\\'")
            description = description.replace("\"","\\\"")
            description = description.replace(">","\>")
            description = description.replace("<br /\>rn","")
            json2 = (
                f'{{"name": "{name}",'
                f'"port": "{port}",'
                f'"protocol": "{protocol}",'
                f'"description": "{description}"}}'
            )
                
            if j == len(splitTR)-2:
                fulljson += json2 # Pas de virgule pour le dernier record JSON
            else:
                fulljson += json2 + ","
            j+=1
    else:
        break

print("["+fulljson+"]")