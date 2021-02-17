
import requests
from pyquery  import PyQuery as pq
import pandas as pd

#url = 'https://quotes.toscrape.com/page/1/'

#urls  = ['https://quotes.toscrape.com/author/Albert-Einstein', 'https://quotes.toscrape.com/author/J-K-Rowling', 'https://quotes.toscrape.com/author/Jane-Austen', 'https://quotes.toscrape.com/author/Marilyn-Monroe', 'https://quotes.toscrape.com/author/Andre-Gide', 'https://quotes.toscrape.com/author/Thomas-A-Edison', 'https://quotes.toscrape.com/author/Eleanor-Roosevelt', 'https://quotes.toscrape.com/author/Steve-Martin', 'https://quotes.toscrape.com/author/Bob-Marley', 'https://quotes.toscrape.com/author/Dr-Seuss', 'https://quotes.toscrape.com/author/Douglas-Adams', 'https://quotes.toscrape.com/author/Elie-Wiesel', 'https://quotes.toscrape.com/author/Friedrich-Nietzsche', 'https://quotes.toscrape.com/author/Mark-Twain', 'https://quotes.toscrape.com/author/Allen-Saunders', 'https://quotes.toscrape.com/author/Pablo-Neruda', 'https://quotes.toscrape.com/author/Ralph-Waldo-Emerson', 'https://quotes.toscrape.com/author/Mother-Teresa', 'https://quotes.toscrape.com/author/Garrison-Keillor', 'https://quotes.toscrape.com/author/Jim-Henson', 'https://quotes.toscrape.com/author/Charles-M-Schulz', 'https://quotes.toscrape.com/author/William-Nicholson', 'https://quotes.toscrape.com/author/Jorge-Luis-Borges', 'https://quotes.toscrape.com/author/George-Eliot', 'https://quotes.toscrape.com/author/George-R-R-Martin', 'https://quotes.toscrape.com/author/C-S-Lewis', 'https://quotes.toscrape.com/author/Martin-Luther-King-Jr', 'https://quotes.toscrape.com/author/James-Baldwin', 'https://quotes.toscrape.com/author/Haruki-Murakami', 'https://quotes.toscrape.com/author/Alexandre-Dumas-fils', 'https://quotes.toscrape.com/author/Stephenie-Meyer', 'https://quotes.toscrape.com/author/Ernest-Hemingway', 'https://quotes.toscrape.com/author/Helen-Keller', 'https://quotes.toscrape.com/author/George-Bernard-Shaw', 'https://quotes.toscrape.com/author/Charles-Bukowski', 'https://quotes.toscrape.com/author/Suzanne-Collins', 'https://quotes.toscrape.com/author/J-R-R-Tolkien', 'https://quotes.toscrape.com/author/Alfred-Tennyson', 'https://quotes.toscrape.com/author/Terry-Pratchett', 'https://quotes.toscrape.com/author/J-D-Salinger', 'https://quotes.toscrape.com/author/George-Carlin', 'https://quotes.toscrape.com/author/John-Lennon', 'https://quotes.toscrape.com/author/W-C-Fields', 'https://quotes.toscrape.com/author/Ayn-Rand', 'https://quotes.toscrape.com/author/Jimi-Hendrix', 'https://quotes.toscrape.com/author/J-M-Barrie', 'https://quotes.toscrape.com/author/E-E-Cummings', 'https://quotes.toscrape.com/author/Khaled-Hosseini', 'https://quotes.toscrape.com/author/Harper-Lee', 'https://quotes.toscrape.com/author/Madeleine-LEngle']
df = pd.read_excel('urls.xlsx'  , usecols= ['link']).values.tolist()
df = [x[0] for x in df]
#print(df)
#print(urls)
#url = 'https://quotes.toscrape.com/author/Pablo-Neruda/'
table = []
for url in urls:
	html = requests.get(url).text
	selector = pq(html)
	title = selector('.author-title').text()
	born_date = selector('.author-born-date').text()
	born_location = selector('.author-born-location').text()

	item = {}
	item['title']=title
	item['born_date']=born_date
	item['born_location']=born_location
	table.append(table)

df = pd.json_normalize(table)

df.to_excel('profiles.xlsx')
