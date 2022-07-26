from bs4 import BeautifulSoup
import requests

requests.get('http://127.0.0.1:8000/del?id=2')
input('Start?')

for page in range(1, 55):
    page = requests.get(
        'https://toplearn.com/courses?pageId=' + str(page) + '&Search=&orderby=createAndUpdatedate&filterby=all')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find Courses
    courses = soup.find_all('div', attrs={
        'class': 'col-lg-4 course-col'})

    for course in courses[:3]:
        result = {
            'name': course.find('a')['title'].strip(),
            'image_url': 'https://toplearn.com' + course.find('img')['data-src'],
            'source': 2,
            'url': 'https://toplearn.com' + course.find('a')['href']
        }

        # Price
        price = course.find('span', attrs={'class': 'price'}).find(
            'i').text.strip()
        if 'رایگان' in price:
            result['price'] = 0
        elif 'اعضای ویژه' in price:
            result['price'] = 0

        else:
            result['price'] = int(price.replace(',', ''))

        # Participants
        result['participants'] = -1

        response = requests.post('http://127.0.0.1:8000/add/?format=api',
                                 json=result)

        print(page, response)
