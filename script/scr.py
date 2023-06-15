import os
from dotenv import load_dotenv
import mysql.connector
from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider
from twisted.internet import reactor

load_dotenv()

DB_SETTINGS = {
    'db': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'passwd': os.getenv('DB_PASS'),
    'host': os.getenv('DB_HOST'),
}

class BacklinkSpider(Spider):
    name = "backlink_spider"

    def start_requests(self):
        cnx = mysql.connector.connect(**DB_SETTINGS)
        cursor = cnx.cursor()
        query = "SELECT domain FROM domains;"
        cursor.execute(query)
        domains = [item[0] for item in cursor.fetchall()]
        cnx.close()

        for domain in domains:
            yield self.make_requests_from_url(f'https://{domain}')

    def parse(self, response):
        cnx = mysql.connector.connect(**DB_SETTINGS)
        cursor = cnx.cursor()

        current_domain = response.url.split("//")[-1].split("/")[0]
        query = f'SELECT id FROM domains WHERE domain = "{current_domain}";'
        cursor.execute(query)
        from_page_id = cursor.fetchone()[0]

        for link in response.css('a::attr(href)').getall():
            if link.startswith('https://'):
                to_domain = link.split("//")[-1].split("/")[0]
                query = f'SELECT id FROM domains WHERE domain = "{to_domain}";'
                cursor.execute(query)
                to_page_id = cursor.fetchone()
                if to_page_id:
                    query = f"INSERT INTO links (from_page_id, to_page_id) VALUES ({from_page_id}, {to_page_id[0]});"
                    cursor.execute(query)
                    cnx.commit()

        cnx.close()

runner = CrawlerRunner()
d = runner.crawl(BacklinkSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()