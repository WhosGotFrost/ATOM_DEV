#using python modules
import requests
import json
import re

#checks for special characters
regex = re.compile('[@_!#%^&*()<>?/\|{~:]') ;

#gets the users IP input
IP = input("Enter an IP Address: ");

response = requests.get("https://json.geoiplookup.io/" + IP);

#deserializing the URL
data = response.json();

if(data['success'] == False):
    print("Sorry but this ins't a Valid IP Address!");
elif(regex.search(IP) == None): 
    #this will get specific json objects
    print("IP: " + data['ip']);
    print("ORG: " + data['org']);
    print("ISP: " + data['isp']);
    print("HOSTNAME: " + data['hostname']);
    print("POSTAL CODE: " + data['postal_code']);
    print("CITY: " + data['city']);
    print("REGION: " + data["region"]);
    print("COUNTRY: " + data['country_name']);
    print("ASN ORG: " + data["asn_org"]);
    print("ASN: " + data["asn"]);
    print("LATITUDE: " + str(data['latitude']));
    print("LONGITUDE: " + str(data["longitude"]));
    #end
else:
    print("Seems like you are using specials characters!");
