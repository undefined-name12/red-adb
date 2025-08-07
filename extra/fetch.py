import requests
import os

shodankey = "" # agrega tu clave aquí

ip_req = requests.get(f"https://api.shodan.io/shodan/host/search?key={shodankey}&query=android+debug+bridge").text
print(ip_req)
