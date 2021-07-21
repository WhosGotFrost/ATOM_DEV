#this script will use an API to get fake information!
import requests
import json

#tries to get the info on the website.
API = requests.get("https://api.namefake.com");

#will try to deserialize the API into json
info = API.json();


print("NAME: " + info['name']);
print("ADDRESS: " + info['address']);
print("MAIDEN NAME: " + info['maiden_name']);
print("BIRTH: " + info['birth_data']);
print('PHONE NUMBER: ' + info['phone_h']);
print('USERNAME: ' + info['username']);
print('PASSWORD: ' + info['password']);
print('USERAGENT: ' + info['useragent']);
print("IP ADDRESS: " + info['ipv4']);
print("MACADDRESS: " + info['macaddress']);
print('CARDNUMBER: ' + info['plasticcard']);
print('CARD EXPIRATION: ' + info['cardexpir']);
print('COMPANY: ' + info['company']);
print('COLOR: ' + info['color']);
print('HEIGHT: ' + str(info['height'])); #STR is another way of saying to string.
print('WEIGHT: ' + str(info['weight'])); # STR changes int to string.
print('EYE-COLOR: ' + info['eye']);
print('HAIR: ' + info['hair']);
print('SPORT: ' + info['sport']);
