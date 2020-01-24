# SpeedGuideCollector
This script aims at collecting the 40+ webpages of the ports used by malwares according to the website SpeedGuide.net.
Then it parses the result to JSON format, to collect the knowledge in one place and to avoid network connectivity requirement.

Just run the script with a shell output to your file : 

HTML
#./parsespeedguide.py > malwareports.html

JSON
#./speedguide_to_json.py > malwareports.json
