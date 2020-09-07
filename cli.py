import click
import requests
from bs4 import BeautifulSoup 


# Author: Victor Urdaneta

@click.group()
def main():
    """
    Simple CLI for web scrapping All the Radiant Orders in the Coppermind
    """
    pass

@main.command()
@click.argument('order')
def search(order):
	#The page from which the data is going to be scraped
	URL = 'https://coppermind.net/wiki/Knights_Radiant'
	page = requests.get(URL)

	#Encapsulating the HTML as a BeatifulSoup object
	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id="mw-content-text")
	items = results.find_all("dl")

	item_title = [item.find('dt') for item in items]
	item_title.pop()
	cnt = 1 
	for item in item_title:
		if order == item.text.lower():
			order = order.split()[2]
			break
		elif cnt >= len(item_title):
			print('The order does not exist')
			
		cnt += 1
	print('\n')

	cnt = 1 
	for item in items:
		content = item.find('dd')
		
		if order in content.text.lower(): 
			print(order.title())
			print(content.text)

			break
		elif cnt <= len(items):
			pass
		cnt+=1
	print('\n')
if __name__ == "__main__":
    main()
