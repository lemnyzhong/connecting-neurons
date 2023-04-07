from bs4 import BeautifulSoup

with open('webscraper\myFirstWebscraper\home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')

    all_divs = soup.find_all('div', class_='card')

    course = []
    prices = []

    for i in all_divs:
        course.append(i.h5.text)
        prices.append(i.a.text.split(' ')[2].replace('$', ''))
    
    for i in range(len(course)):
        print(f'\nThe price of "{course[i]}" costs ${prices[i]}')
    print()

