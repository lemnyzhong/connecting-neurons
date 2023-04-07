from bs4 import BeautifulSoup
import requests
import webbrowser

# extracting web data and booting it into BeautifulSoup
rq = requests.get('https://www.seek.com.au/programming-jobs/in-All-Sydney-NSW').text
soup = BeautifulSoup(rq, 'lxml')

# searching specific html elements for roles titles
# and employer's names
job_div = soup.find_all('h3', class_='_1wkzzau0 a1msqi4y lnocuo0 lnocuol _1d0g9qk4 lnocuos lnocuo21')
employers_span = soup.find_all('span', class_='_1wkzzau0 a1msqi4y lnocuo0 lnocuo2 lnocuo21 _1d0g9qk4 lnocuod')

# initialise arrays for storing collected data
current_roles = []
employers = []

# append data to storage
for i in range(0, len(employers_span)):
    current_roles.append(job_div[i].text)
    employers.append(employers_span[i].text)

# print stored job roles with respective employers
for i in range(len(current_roles)):
    print(f'{current_roles[i]} {employers[i]}\n')

# if you see anything interesting bust open the webpage
if(input("open?\n").lower() == 'yes'):
    webbrowser.open_new('https://www.seek.com.au/programming-jobs/in-All-Sydney-NSW')



