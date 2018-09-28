import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

def get_list(row):
	try:
		data = row
		if (len(data) == 2):
			location = data[0]
			latlong = data[1]

			with open('countries.json', 'r') as f:
				countries = json.load(f)

			country = location.split(',')
			if len(country) >= 2:
				country[1] = country[1].replace(' ','')
				for x in countries: 
					if x['country'] == country[1]:
						url = "https://www.harley-davidson.com/dealerservices/services/rest/dealers/proximitySearch.json?_type=json&size=100&latlng=" + str(latlong) + "&miles=5000&locale=en_US&country=" + str(x['alpha3'])
						
						response = requests.get(url)
						json_data = json.loads(response.text)
						dealerResponse = json_data['dealerResponse']

						if 'dealers' in dealerResponse:
							dealers = dealerResponse['dealers']
							for deal in dealers:
								x = []
								x.append(data[0])
								x.append('https://www.harley-davidson.com/us/en/tools/find-a-dealer.html#dealer?dealer_id=' + str(deal['id']))
								x.append(deal['name'])

								if 'contact' in deal:
									contact = deal['contact']


									if 'address1' in contact:
										x.append(str(contact['address1']))
									else:
										x.append('')
									if 'city' in contact:
										x.append(str(contact['city']))
									else:
										x.append('')
									x.append(country[1])							
									if 'phoneNumber' in contact:
										x.append(str(contact['phoneNumber']))
									else:
										x.append('')
									if 'state' in contact:
										x.append(str(contact['state']))
									else:
										x.append('')
									if 'postalCode' in contact:
										x.append(str(contact['postalCode']))
									else:
										x.append('')
									if 'email' in contact:
										x.append(str(contact['email']))
									else:
										x.append('')

								if 'website' in deal:
									x.append(deal['website'])
								else:
									x.append('')

								# print (x)

								final_list = []
								final_list.append(x)
								print (final_list)

								filename = "record1.csv"
								with open(filename, 'a+') as csvfile:
									csvwriter = csv.writer(csvfile) 
									csvwriter.writerows(final_list)


	except Exception as e:
						print(e)
					
					


		

if __name__ == '__main__':
	ifile = open('final1.csv', "r")
	reader = csv.reader(ifile)

	i= 0 
	for row in reader:
		get_list(row)

	ifile.close()
