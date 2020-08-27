from bs4 import BeautifulSoup
import requests
import json


demo = [1840,1844,1848,1852,1856,1860,1864,1868,1872,1876,1880,1884,1888,1892,1896,1900,1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020]
repub = [1856,1860,1864,1868,1872,1876,1880,1884,1888,1892,1896,1900,1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016, 2020]



# d_platforms=[]

# for d in demo:

# 	r = requests.get(f'https://www.presidency.ucsb.edu/documents/{d}-democratic-party-platform')

# 	soup = BeautifulSoup(r.text)


# 	platform = soup.find("div", attrs={"class":"field-docs-content"})
# 	date = soup.find("div", attrs={"class":"field-docs-start-date-time"})
# 	print(date.text)

# 	d_platforms.append({'date':date.text,'text':platform.text})

# 	json.dump(d_platforms,open('democrats.json','w'),indent=2)

r_platforms=[]

for rep in repub:

	url = f'https://www.presidency.ucsb.edu/documents/republican-party-platform-{rep}'

	# because THEY DONT HAVE A FUCKING PLATFORM in 2020
	if rep == 2020:
		url = 'https://www.presidency.ucsb.edu/documents/resolution-regarding-the-republican-party-platform'
	elif rep > 1996:
		url = f'https://www.presidency.ucsb.edu/documents/{rep}-republican-party-platform'		


	r = requests.get(url)

	print(url)
	soup = BeautifulSoup(r.text)


	platform = soup.find("div", attrs={"class":"field-docs-content"})
	date = soup.find("div", attrs={"class":"field-docs-start-date-time"})
	print(date.text)

	r_platforms.append({'date':date.text,'text':platform.text})

	json.dump(r_platforms,open('republicans.json','w'),indent=2)