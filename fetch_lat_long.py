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


proxy = ['50.252.42.253:31820',
		'194.187.216.182:43909',
		'75.71.180.197:49243',
		'77.233.165.152:53102',
		'194.79.60.240:50740',
		'190.0.242.178:52774',
		'94.19.112.222:59044',
		'213.21.191.114:41863',
		'1.10.186.100:57253',
		'212.112.113.27:37262',
		'185.28.250.173:8080',
		'91.93.39.220:34354',
		'78.157.79.120:59763',
		'95.47.136.182:55352',
		'85.114.105.58:46897',
		'177.85.112.234:47201',
		'146.66.184.129:53521',
		'62.80.183.233:44174',
		'92.245.100.50:50192',
		'115.178.25.134:42223',
		'176.117.64.41:45325',
		'188.173.225.165:54059',
		'210.1.58.201:8080',
		'94.228.245.58:45401']

def get_list(city):

	try:

		http_proxy  = "http://83.69.180.83:42195"
		https_proxy = "https://" + random.choice(proxy)
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
