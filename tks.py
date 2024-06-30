from scrapify import Scraper

url = 'https://www.example.com'
scraper = Scraper(url)

phone_number = scraper.find('<span class="phone">123-456-7890</span>')
print('Phone Number:', phone_number)