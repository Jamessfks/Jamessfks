import os
from lxml import etree
import requests
import time
import csv


#Proxy ip
proxies = {
    "https://":"https://113.28.90.67:9480"
}

#Request header
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

#url of IMDb
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"    

#requests website
resp = requests.get(url,headers=header,proxies=proxies)

#encoding utf-8
resp.encoding = 'utf-8'

html = etree.HTML(resp.text)

#user input number
p = int(input("Enter rank 1 to 250\n"))

# path
divs = html.xpath(f"/html/body/div[3]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[{p}]")


#Open csv in write mode
f = open("movie.csv",mode="w")
csvwriter = csv.writer(f)

#Processing information
for div in divs:
    name = "".join(div.xpath("./td[2]/a/text()")) #the name of the movie

    score = div.xpath("./td[3]/strong/text()")[0] # Movie score

    year = div.xpath("./td[2]/span/text()")[0].strip("()") # The year of the movie

    img = div.xpath("./td[1]/a/img/@src")[0]  #Picture download address
    

    #output to csv file
    csvwriter.writerow(name.split(','))
    csvwriter.writerow(score.split(','))
    csvwriter.writerow(year.split(','))
    csvwriter.writerow(img.split(','))

    time.sleep(0.03)
      


print("All OVER!")
--->
