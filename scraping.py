import requests
from bs4 import BeautifulSoup
from datetime import datetime , timedelta
import requests
import json
from urllib.request import urlopen
import re
import socket
import random


def filter_end():
    from datetime import date 
    ini_time_for_now = date.today()

    return ini_time_for_now

def filter_start():
    from datetime import date 
    ini_time_for_now = date.today()

    bir_gün_öncesi = ini_time_for_now - \
                    timedelta(days= 1)
    
    return str(bir_gün_öncesi)

def request(start,end):
    url = f"https://api.orhanaydogdu.com.tr/deprem/live.php?limit=100"
    request_value= requests.get(url,)
    data = json.loads(request_value.text)
     


    
    array_sayısı = int(len(data['result']))

    
    
    yikicilik_list = []

    for i in range (0,array_sayısı):
       
        array = (data['result'])
        
        yikicilik = (array[i]['mag'])
        yikicilik_list.append(yikicilik)
        
        
        
    sonuc = max(yikicilik_list)
    minsonuc = min(yikicilik_list)
    ind2 = yikicilik_list.index(minsonuc)   
    ind = yikicilik_list.index(sonuc)
    
    res = data['result']
    print(res[ind])
    print(res[ind2])
    json_data = {
 
  "data": [
    {"max" : res[ind]},
    
    {"min": res[ind2]}
  ],
   
   "author": "LavanderProjects",
   "status": "success"
}
    
    return json_data
veri = None
def scrapheaal():
 header = {

    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0",
   
}

 resim_url = "https://heaal.meb.k12.tr"

 try: 
    r = requests.get("https://heaal.meb.k12.tr/tema/icerik.php?KATEGORINO=94501" ,timeout=5,headers=header)
    source = BeautifulSoup(r.content,"lxml")
 except:
    return json.loads(veri)




 for i in source.select("#liste > div:nth-child(2) > div:nth-child(1) > div.tarih > p.gun > time"):
        if i.has_attr('datetime'):
            tarih1 = i["datetime"]
 for i in source.select("#liste > div:nth-child(3) > div:nth-child(1) > div.tarih > p.gun > time"):
    if i.has_attr('datetime'):
            tarih2 = i["datetime"]
 for i in source.select("#liste > div:nth-child(4) > div:nth-child(1) > div.tarih > p.gun > time"):
    if i.has_attr('datetime'):
            tarih3 = i["datetime"]
 
    

 tarih1 = tarih1.split("-")
 tarih1date = tarih1[2]+"/"+tarih1[1]+"/"+tarih1[0]


 tarih2 = tarih2.split("-")
 tarih2date = tarih2[2]+"/"+tarih2[1]+"/"+tarih2[0]
 

 tarih3 = tarih3.split("-")
 tarih3date = tarih3[2]+"/"+tarih3[1]+"/"+tarih3[0]

 # print(tarih1[2]+"/"+tarih1[1]+"/"+tarih1[0])


 haber1 = source.select("#liste > div:nth-child(2) > div.row > div.col-sm-8 > p")
 haber2 = source.select("#liste > div:nth-child(3) > div.row > div.col-sm-8 > p")
 haber3 = source.select("#liste > div:nth-child(4) > div.row > div.col-sm-8 > p")

 baslik1 = source.select("#liste > div:nth-child(2) > div:nth-child(1) > div.liste_baslik > a")
 baslik2 = source.select("#liste > div:nth-child(3) > div:nth-child(1) > div.liste_baslik > a")
 baslik3 = source.select("#liste > div:nth-child(4) > div:nth-child(1) > div.liste_baslik > a")


 resim1 = source.select("#liste > div:nth-child(2) > div.row > div.col-sm-4 > a > img")
 resim2 = source.select("#liste > div:nth-child(3) > div.row > div.col-sm-4 > a > img" )
 resim3 = source.select("#liste > div:nth-child(4) > div.row > div.col-sm-4 > a > img" )

 resim1_url = resim_url + resim1[0]['src']
 resim2_url = resim_url + resim2[0]['src']
 resim3_url = resim_url + resim3[0]['src']
 

 json_data = {
 
  "data": [
    {"haber": haber1[0].text, "baslik": baslik1[0].text , "resim" : resim1_url,"tarih" : tarih1date},
    {"haber": haber2[0].text, "baslik": baslik2[0].text , "resim" : resim2_url,"tarih" : tarih2date},
    {"haber": haber3[0].text, "baslik": baslik3[0].text , "resim" : resim3_url,"tarih" : tarih3date}
  ],
   
   "author": "LavanderProjects",
   "status": "success"
}
 veri = json_data
 print(veri)
 return json_data


