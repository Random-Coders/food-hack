#Imports
from bs4 import BeautifulSoup as bs # process html
from requests import get # to request page url code

class Scrape():
    def __init__(self, url):
        self.url = url
        r = get(self.url) # request page
        page = r.text # formatting
        self.soup = bs(page, 'html.parser') # parse html
    def scrapeGeniusKitchen(self):
        directions = self.soup.find('ol', attrs={'class':'expanded'})
        children = directions.findChildren('li')
        print(children)


if __name__ == '__main__':
    test = Scrape('https://www.geniuskitchen.com/recipe/bbq-chicken-rice-burrito-cowboy-crunch-burrito-333095')
    test.scrapeGeniusKitchen()
