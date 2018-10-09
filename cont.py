import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def get_list():
	try:
		with open('countries.json', 'r') as f:
				countries = json.load(f)
		
		for x in countries: 
					data = open('country.txt','a+')
					data.write(x['country'])
					data.write('\n')
					data.close()


	except Exception as e:
						print(e)
					
					


		

if __name__ == '__main__':
	get_list()

