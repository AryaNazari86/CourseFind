from attr import attr, attrs
from bs4 import BeautifulSoup
import requests

page = requests.get('https://faradars.org/explore?category_ids=1049')
soup = BeautifulSoup(page.text, 'html.parser')

# Find Courses
courses = soup.find_all('div', attrs={
    'class': 'course-card grid-item upcoming_style treasure treasure-color'})


for course in courses[:5]:
    result = {
        'name': course.find('div', attrs={
            'class': 'show-text-card'}).text.strip(),
        'image_url': course.find('img')['src'],
        'source': 1,
        'url': course.find('a')['href']
    }

    # Price
    price = course.find('div', attrs={'class': 'card-footer'}).text.strip()
    if 'رایگان!' in price:
        result['price'] = 0
    else:
        result['price'] = int(price[:6].replace(',', ''))

    # Participants
    result['participants'] = int(BeautifulSoup(requests.get(result['url']).text, 'html.parser').find(
        'div', attrs={'id': 'soldCount'}).text.strip()[:-3].replace(',', ''))

response = requests.post('http://127.0.0.1:8000/a/?format=api', json=result)
print(response)
