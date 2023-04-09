from scraper import *
import os
import time

# designed to waste your time.
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

                try:
                    s.scrape()
                    
                    making_you_wait(5)

                    s.printAll()

                except:
                    continue

                welcome_ans = input('What would you like to do:\n')

            case 'print':
                for i in scraper_obj:
                    i.printAll()
                welcome_ans = input('What would you like to do:\n')

            case 'path':
                for i in scraper_obj:
                    i.print_path()
                welcome_ans = input('What would you like to do:\n')
            
            case 'open':
                print('\nThese are the current search paths:\n')

                for i in range(0, len(scraper_obj)):
                    print(f'{i+1}. {scraper_obj[i].get_path()}\n')
                
                n = input("Which would you like to open:\n")
                
                if(int(n) != 0):
                    scraper_obj[int(n)-1].openPage()

                welcome_ans = input('What would you like to do:\n')

            case other:
                welcome_ans = input('What would you like to do:\n')
    
    # goodbye
    print('\nThank you for using JbScrpr v0.1 and good luck with your applications!\n')

if __name__ == "__main__":
    main()