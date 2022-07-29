from bs4 import BeautifulSoup
import requests
import time

requests.get('http://127.0.0.1:8000/del?id=1')
input('Press Enter To Start: ')
counter = 1
start_time = time.time()

for page in range(34):
    page = requests.get(
        'https://faradars.org/explore?page=' + str(page) + '&category_ids=1049')
    soup = BeautifulSoup(page.text, 'html.parser')

    # Find Courses
    courses = soup.find_all('div', attrs={
        'class': 'course-card grid-item upcoming_style treasure treasure-color'})

    for course in courses:
        result = {
            'name': course.find('div', attrs={
                'class': 'show-text-card'}).text.strip(),
            'image_url': course.find('img')['src'],
            'source': 1,
            'url': course.find('a')['href'],
        }

        # Teacher
        result['teacher'] = BeautifulSoup(requests.get(
            result['url']).text, 'html.parser').find('h6').text.strip()

        # Price
        price = course.find('div', attrs={'class': 'card-footer'}).text.strip()
        if 'رایگان!' in price:
            result['price'] = 0
        else:
            result['price'] = int(price[:6].replace(',', ''))

        # Participants
        course_page = BeautifulSoup(requests.get(
            result['url']).text, 'html.parser')
        result['participants'] = int(course_page.find(
            'div', attrs={'id': 'soldCount'}).text.strip()[:-3].replace(',', ''))

        # Description
        result['description'] = course_page.find(
            'section', attrs={'id': 'course-navigation-summary'}).find('p').text.strip()

        response = requests.post(
            'http://127.0.0.1:8000/api/?format=api', json=result)

        if response.status_code != 201:
            print(10*'=')
            print(response.text)
            print(10*'=')

        print(counter, response, time.time() - start_time)
        counter += 1
