from bs4 import BeautifulSoup
import requests
import re
import base64
import json


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.src = None
        self.soup = None

    def fetch_page(self):
        req = requests.get(self.url)
        self.src = req.text

    def save_page(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.src.encode('utf-8'))

    def parse_wikipedia_page(self):
        self.soup = BeautifulSoup(self.src, 'lxml')
        unfiltered_res = self.soup.find('table', class_='wikitable sortable').find_all('tr')
        res = unfiltered_res[1:-1]
        final_data = {}
        names = []

        for i in res:
            a_res = i.find('a')
            name = a_res.text
            names.append(name)
            names_list = [re.sub(r'[\s\n]+', '_', j) for j in names]

        count = 0
        for i in res:
            data = [i.find('span', class_='plainlinks').find('a')['href'], i.find_all('td')[2].text.strip(),
                    float(i.find_all('td')[3].text)]
            description = re.sub(r'\[.*?\]', '', i.find_all('td')[4].text).strip()
            data.append(description)
            description = re.sub(r'\[.*?\]', '', i.find_all('td')[5].text).strip()
            data.append(description)
            data.append(i.find_all('td')[6].find('a').text)
            final_data[names_list[count]] = data
            count += 1

        return final_data


class WebScraper2(WebScraper):
    def parse_bankmycell_page(self):
        self.soup = BeautifulSoup(self.src, 'lxml')
        res = self.soup.find(class_='ts-advanced-tables-wrapper').find_all('tr')
        years_data = {}

        for row in res:
            cells = row.find_all('td')

            if len(cells) == 2:
                year_encoded = cells[0].get('data-cell-value')
                active_users_encoded = cells[1].get('data-cell-value')

                year = base64.b64decode(year_encoded).decode('utf-8')
                active_users = base64.b64decode(active_users_encoded).decode('utf-8')
                year = year.replace('*', '')

                years_data[int(year)] = float(active_users)

        return years_data


def main():
    url1 = 'https://en.wikipedia.org/wiki/List_of_most-subscribed_YouTube_channels'
    url2 = 'https://www.bankmycell.com/blog/number-of-youtube-users/'

    scraper1 = WebScraper(url1)
    scraper1.fetch_page()
    scraper1.save_page('page.html')
    channels_data = scraper1.parse_wikipedia_page()

    scraper2 = WebScraper2(url2)
    scraper2.fetch_page()
    scraper2.save_page('page2.html')
    customers_data = scraper2.parse_bankmycell_page()

    with open('channels_data.json', 'w', encoding='utf-8') as json_file1:
        json.dump(channels_data, json_file1, ensure_ascii=False, indent=4)

    with open('customers_data.json', 'w', encoding='utf-8') as json_file2:
        json.dump(customers_data, json_file2, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()




