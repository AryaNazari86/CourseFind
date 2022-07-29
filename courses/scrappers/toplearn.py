from bs4 import BeautifulSoup
import requests
import time

requests.get('http://127.0.0.1:8000/del?id=2')
input('Press Enter To Start: ')
counter = 1


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

        response = requests.post(
            'http://127.0.0.1:8000/api/?format=api', json=result)

        if response.status_code != 201:
            print(10*'=')
            print(response.text)
            print(10*'=')

        print(counter, response, time.time() - start_time)
        counter += 1
