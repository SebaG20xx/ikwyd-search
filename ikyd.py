import requests
from bs4 import BeautifulSoup
listaips = open('ips.txt')
registro = open('ipsdetectadas.txt', 'w')
URL = "https://iknowwhatyoudownload.com/en/peer/?ip="
for ip in listaips:
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
    URLIP = URL + ip
    req = requests.get(url=URLIP, headers=headers)
    soup = BeautifulSoup(req.content,'html5lib')
    out = soup.find_all("div",class_="torrent_files")
    if out != []:
        print("IP Encontrada: " + str(ip))
        registro.write(ip)
print("Terminado")
