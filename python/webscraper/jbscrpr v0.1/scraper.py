import requests
from bs4 import BeautifulSoup
import webbrowser

scraper_obj = []

class scraper:

    def __init__(self, key: str, area: str):
        self.keywords = key
        self.area = area
        self.search_path = f'https://www.seek.com.au/{self.keywords}jobs/{self.area}'
        scraper_obj.append(self)
        self.current_roles = []
        self.employers = []

    def scrape(self):
        rq = requests.get(self.search_path).text
        soup = BeautifulSoup(rq, 'lxml')

        job_h3 = soup.find_all('h3', class_='_1wkzzau0 a1msqi4y lnocuo0 lnocuol _1d0g9qk4 lnocuos lnocuo21')
        company_span = soup.find_all('span', class_='_1wkzzau0 a1msqi4y lnocuo0 lnocuo2 lnocuo21 _1d0g9qk4 lnocuod')

        for i in range(len(job_h3)):
            self.current_roles.append(job_h3[i].text)
            self.employers.append(company_span[i].text)

    def printAll(self):
        print(f"\nThese are the current jobs available using keywords: {self.keywords} in area: {self.area}:\n")
        for i in range(len(self.current_roles)):
            print(f'        {self.current_roles[i]} {self.employers[i]}\n')



    # open browser at page
    def openPage(self):
        webbrowser.open_new(self.search_path)


    # print functions for scraper
    def print_keywords(self):
        print(self.keywords)

    def print_path(self):
        print(self.search_path)