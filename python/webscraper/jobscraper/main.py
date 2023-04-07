from bs4 import BeautifulSoup
import requests
import webbrowser

rq = requests.get('https://www.seek.com.au/python-jobs/in-All-Sydney-NSW').text
soup = BeautifulSoup(rq, 'lxml')

job_div = soup.find_all('h3', class_='_1wkzzau0 a1msqi4y lnocuo0 lnocuol _1d0g9qk4 lnocuos lnocuo21')
employers_span = soup.find_all('span', class_='_1wkzzau0 a1msqi4y lnocuo0 lnocuo2 lnocuo21 _1d0g9qk4 lnocuod')

# prints job titles
current_roles = []
for i in job_div:
    current_roles.append(i.text)

employers = []
for i in range(0, len(employers_span)):
    employers.append(employers_span[i].text)

for i in range(len(current_roles)):
    print(f'{current_roles[i]} {employers[i]}\n')

if(input("open?\n").lower() == 'yes'):
    webbrowser.open_new('https://www.seek.com.au/python-jobs/in-All-Sydney-NSW')



