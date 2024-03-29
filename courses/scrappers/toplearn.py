from bs4 import BeautifulSoup
import requests
import time
# kfEbrzZ7.3gaZkZq8E7lXtwhRz0mFzZBhlP8VuZxB
requests.post(
    'http://127.0.0.1:8000/del/',
    data={'id': 1},
    headers={'Authorization': 'Api-Key kfEbrzZ7.3gaZkZq8E7lXtwhRz0mFzZBhlP8VuZxB'}
)
input('Press Enter To Start: ')
start_time = time.time()

courses = []

for page in range(1, 55):
    page = requests.get(
        'https://toplearn.com/courses?pageId=' + str(page) + '&Search=&orderby=createAndUpdatedate&filterby=all')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find Courses
    courses = soup.find_all('div', attrs={
        'class': 'col-lg-4 course-col'})

    for course in courses:
        start_time = time.time()
        result = {
            'name': course.find('a')['title'].strip(),
            'image_url': 'https://toplearn.com' + course.find('img')['data-src'],
            'source': 2,
            'url': 'https://toplearn.com' + course.find('a')['href'],
            'teacher': course.find('div', attrs={'class': 'detail'}).find('a')['title'],
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

        # Description
        course_page = BeautifulSoup(
            requests.get(result['url']).text, 'html.parser')
        result['description'] = course_page.find(
            'div', attrs={'class': 'course-content-text'}).text.strip()

        courses.append(result)

response = requests.post(
    'http://127.0.0.1:8000/api/?format=api',
    data=courses,
    headers={'Authorization': 'Api-Key kfEbrzZ7.3gaZkZq8E7lXtwhRz0mFzZBhlP8VuZxB'}
)

print(response, time.time() - start_time)

