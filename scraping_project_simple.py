import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')

def list_sorted_by_votes(list):
	return sorted(list, key= lambda k: k['points'], reverse=True)

def custom_stories_by_votes(links):
	scores = soup.select('.score')
	hn = []
	for i in range(len(links)):
		score = scores[i].getText()
		if len(score):
			score = score.replace(' points', '')
			title = links[i].getText()
			link = links[i].get('href')
			if int(score) > 99:
				hn.append({'title': title, 'link': link, 'points': score})
	return list_sorted_by_votes(hn)

pprint.pprint(custom_stories_by_votes(links))
