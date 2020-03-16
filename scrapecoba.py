from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
url = 'https://monexnews.com/harga-emas.htm?searchdatefrom=10-03-2014&searchdateto=10-03-2020'
#open connection, grab page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grab each product
containers = page_soup.findAll("tr",{"class":"verySoftGreyBg"})

filename = "scrapeemas2.csv"
f = open(filename,"w")

headers = "tanggal,hargaemas \n"
f.write(headers)

for container in containers:
    Goldgr = container.find_all("td")[3].text.strip()
    date = container.find_all("td")[0].text.strip()

    print('Tanggal: '+ date)
    print('Harga: '+ Goldgr)
    f.write(date+ "," + Goldgr + "\n")

f.close()