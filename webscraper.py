import requests
from bs4 import BeautifulSoup
url = 'http://nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,  'html.parser')
for story_heading in soup.find_all(class_="css-1qwxefa esl82me0"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
'''title = soup.find('span', 'articletitle').string
print title'''
