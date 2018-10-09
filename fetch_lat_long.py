import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import random


proxy = ['193.93.76.161:48231',
		'5.160.127.194:59995',
		'203.95.220.178:52200',
		'177.126.89.188:3128',
		'109.104.199.11:31636',
		'193.201.81.83:61308',
		'181.65.168.76:3128',
		'113.53.83.252:33028',
		'89.177.43.49:39110',
		'94.130.69.5:46283',
		'103.238.109.86:51827',
		'81.133.55.7:55802',
		'5.202.40.130:8080',
		'185.158.9.15:61678',
		'78.30.208.154:44194',
		'110.76.147.130:9191',
		'151.249.136.2:38476',
		'177.87.223.194:8888',
		'181.10.195.91:8888',
		'91.213.119.246:38333',
		'31.186.54.203:38121',
		'83.39.227.224:40855',
		'158.174.89.250:57636']


def get_list(city):

	try:
		url = random.choice(proxy)
		http_proxy  = "http://83.69.180.83:42195"
		https_proxy = "https://" + url
		ftp_proxy   = "ftp://10.10.1.10:3128"
		proxyDict = { 
		"http"  : http_proxy, 
		"https" : https_proxy, 
		"ftp"   : ftp_proxy
		}
		payload = {}
		headers = {}
		payload ["action"] = 'gpcm' 
		payload ["c1"] = str(city)
		payload ["cp"] = ''
		print (payload)
		print (https_proxy)
		headers = {
		'cookie': "_ga=GA1.2.1456151731.1538115453; _gid=GA1.2.770331370.1538115453; PHPSESSID=9437efk3tfdcdae7se2fbkn3c5",
		'accept-language': "en-US,en;q=0.8",
		'accept-encoding': "gzip, deflate, br",
		'referer': "https://www.latlong.net/",
		'accept': "*/*",
		'content-type': "application/x-www-form-urlencoded",
		'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
		'x-requested-with': "XMLHttpRequest",
		'origin': "https://www.latlong.net",
		'cache-control': "no-cache",
		}
		url = 'https://www.latlong.net/_spm4.php'
		response1 = requests.post(url, data=payload, headers=headers, proxies=proxyDict)
		html1 = BeautifulSoup(response1.content, 'html.parser')
		print (html1)
		if str(html1) == '0000':
			print ("Sorry")
			proxy.remove(url)
			get_list(city)
		else:
			final_list = []
			x = []
			x.append(city)
			x.append(html1)
			final_list.append(x)
			print (final_list)
			filename = "final1.csv"
			with open(filename, 'a+') as csvfile:
				csvwriter = csv.writer(csvfile) 
				csvwriter.writerows(final_list)
	except Exception as e:
		print(e)
		get_list(city)

		

if __name__ == '__main__':
	cities = open('cities.txt','r')
	for city in cities:
		city = city.replace('\n','')
		get_list(str(city))
