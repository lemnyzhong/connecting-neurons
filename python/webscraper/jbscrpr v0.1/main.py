from scraper import *
import os
import time

def making_you_wait(waste):
    for i in range(1, waste):
        if i % 2 == 0:
            os.system('clear')
            print('scraping..')
            time.sleep(1)
        else:
            os.system('clear')
            print('scraping.')
            time.sleep(1)
    os.system('clear')
    print('scraped!')
    time.sleep(3)
    os.system('clear')

def main():
    welcome_ans = input("Welcome to JbScrpr v0.1\nWhat would you like to do:\n")
    while welcome_ans != 'quit':
        match welcome_ans:
            case 'scrape':
                keyword_ans = input('Please enter the keywords you would like to use:\n(Please remember the format for keywords is "key1-key2..-keyn-")\n')
                area_ans = input('Please enter the area you would like to use:\n(Please remember the format for keywords is "in-All-Sydney-NSW")\n')

                s = scraper(keyword_ans, area_ans)
                s.scrape()
                
                making_you_wait(5)

                s.printAll()

                welcome_ans = input('\nWhat would you like to do:\n')

            case 'print':
                for i in scraper_obj:
                    i.printAll()
                welcome_ans = input('\nWhat would you like to do:\n')

            case 'path':
                for i in scraper_obj:
                    i.print_path()
                welcome_ans = input('\nWhat would you like to do:\n')
            
            case other:
                welcome_ans = input('\nWhat would you like to do:\n')
    
if __name__ == "__main__":
    main()