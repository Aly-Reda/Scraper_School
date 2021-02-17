# import pandas as pd

# df = pd.read_html('https://yoga.ca/find-a-teacher/')[0]
# df.to_excel('teacher.xlsx',index=False)
# print(df)
#HTML Done
#CSS
#HTML ---- CSS selectors  ---- store 
#requests -- pyquery  ---- pandas 

# selenium
# requests

import requests
from pyquery  import PyQuery as pq
import pandas as pd

table = []
#print( [x for x in range(1,11) ])
url = 'https://quotes.toscrape.com/page/1/'

#https://quotes.toscrape.com + /page/6/

#urls = [f'https://quotes.toscrape.com/page/{x}/' for x in range(1,10 + 1)]
#for url in urls:
while 1:
	print(url)
	response = requests.get(url)
	if response.status_code == 200:
		#print(response.status_code)
		html = response.text
		selector = pq(html)
		url = selector('.next a').attr('href')
		
		containers = selector('.quote').items()
		for container in containers:
			#print(container)
			qoute = container('.text').text()
			author = container('small.author[itemprop="author"]').text()
			author = container('a[href^="/author"]').parent('span')('small').text()

			link = container('a').eq(0).attr('href')
			link = container('a:contains("(about)")').attr('href')
			link = container('small[itemprop="author"] + a').attr('href')
			link = 'https://quotes.toscrape.com' + container('[href^="/author"]').attr('href')
			
			#numbers = [f'{x}_aly' for x in range(1,10)]
			#print(numbers)
			tags = [x.text() for x in container('.tag').items() ]
			tags_string  = ', '.join(tags)
			item = {
			'author':author,
			'qoute':qoute,
			'link':link,
			'tags_string':tags_string,


			}
			table.append(item)
		if url==None:
			break
		else:
			url ='https://quotes.toscrape.com' + url

df = pd.json_normalize(table)
print(df)
df.to_excel('pagination.xlsx')
