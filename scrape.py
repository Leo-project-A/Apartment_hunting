import requests
from bs4 import BeautifulSoup as bs
import io
import time
import json
import import_module

CONFIG_FILE = "config.json"
SLEEP_TIME = 3

PAGE_NUMBER_SELECTOR = 'button.page-num'
NO_PRICE_LABEL = "לא צוין מחיר"

def buildURL(configuration) -> str:
    """returns a URL string for the webpage needed based on the configuraion file"""
    # base url to add the prefrences
    newURL = configuration['data']['URL_HAIFA']         

    # the input arguments of the url
    items = configuration['arguments'].items()
    for key, value in items:
        if value and value != '-1--1':
            newURL += f"&{key}={value}"
    return newURL

# scrapes the given soup webPage
def scrape(soup: bs, apartament_list: list[dict]) -> None:
    """scrapes the current webpage for data, adds if to the total apartament list"""
    new_list = []
    ## scrape process ##
    listings = soup.findAll('div', class_="feeditem table")
    for item in listings:
        
        id = item.div.get('item-id')

        address=  item.find('span', class_='title', recursive=True).text.strip()
        area= item.find('span', class_='subtitle', recursive=True).text.strip()

        rooms = item.find('div', class_='data rooms-item', recursive=True).find('span', class_='val').text.strip()
        floor = item.find('div', class_='data floor-item', recursive=True).find('span', class_='val').text.strip()
        squareMeter = item.find('div', class_='data SquareMeter-item', recursive=True).find('span', class_='val').text.strip()

        price = item.find('div', class_='price', recursive=True).text.strip()
        if price != NO_PRICE_LABEL:
            price = int(price[:-2].replace(',',''))
        else:
            price = -1

        new_list.append({
            "item_id": id,

            "address": address,
            "area": area,

            "rooms": rooms,
            "floor": floor,
            "squareMeter": squareMeter,

            "price": price
        })
    ## FINISHED scrape process ##
    apartament_list.extend(new_list)

# return the soup object of the url page
def getSoup(url: str) -> bs:
    try:
        req = requests.get(url)
        soup = bs(req.text, 'html.parser')
        title = soup.find('title').text
    except Exception as e:
        print("cant reach site")
        return None
    # check if bot detected
    if detectionAlert(title):
        return None
    return soup

# checks if page was loaded properly, no decetion or errors
def detectionAlert(pageTitle: str) -> bool:
    #checks if page loaded properly, without detection
    if pageTitle == "ShieldSquare Captcha":     # weve been had
        print("godamn CAPTCHA... work around it")
        return True   
    if pageTitle == "403 Forbidden":     # weve been had
        print("403 Forbidden -> forbidden request, to many?")
        return True

def run(file_format):
    apartament_list = []
    # user configurations for search
    try:
        with open(CONFIG_FILE) as jsonFile:
            configuraiton = json.load(jsonFile)
    except:
        print("failed loading configuration file")
        return

    # the main url of the selected arguments
    curUrl = buildURL(configuraiton)

    soup = getSoup(curUrl)
    if not soup:
        return -1
    
    # get the number of pages at the bottom of returend page
    mySelector = soup.select(PAGE_NUMBER_SELECTOR)
    if mySelector:
        numOfPages = int(mySelector[0].text.strip())      #the number of search results pages
    else:                                                 #if selector not found - its means only 1 result page
        numOfPages = 1
    print(f"number of result plages: {numOfPages}")

    # scrape the first page, since we already got the soup
    scrape(soup, apartament_list)       # EXTENDS the aparatment list
    print("page 1 loaded to FILE")

    # scrape any other page in the results
    for page in range(1,numOfPages):
        time.sleep(SLEEP_TIME)
        try:
            scrape(getSoup(curUrl + f"&page={page+1}"), apartament_list)
            print(f"page {page+1} loaded to FILE")
        except:
            print(f"failed to scrape page {page+1}")

    ## unload the data in the format we want
    import_module.unload_data(apartament_list, file_format)
    return

## currenly default is CSV. make it a command line argument. for choosing which file format you want
if __name__ == '__main__':
    result = run('csv')
    if result == -1:
        print('operation failed!')
    else:
        print("all done")
    
