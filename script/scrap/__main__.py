from scrapy.crawler import CrawlerRunner
from scrapy.spiders import Spider
from twisted.internet import reactor
import db_operations as db

class BacklinkSpider(Spider):
    name = "backlink_spider"
    #custom_settings = {
    #    'REQUEST_FINGERPRINTER_IMPLEMENTATION' : 'scrapy.utils.request.RequestFingerprinter'
    #}
    def start_requests(self):
        print("Starting backlink spider...")
        domains = db.get_domains()
        print(f"Found {len(domains)} domains to crawl.")
        for domain in domains:
            print(f"Starting to crawl domain: {domain}")
            yield self.make_requests_from_url(f'https://{domain}')

    def parse(self, response):
        print(f"Crawling domain: {response.url}")
        current_domain = response.url.split("//")[-1].split("/")[0]
        from_page_id = db.get_page_id(current_domain)

        if from_page_id is not None:
            print(f"Page ID for current domain ({current_domain}): {from_page_id}")
            for link in response.css('a::attr(href)').getall():
                if link.startswith('https://'):
                    to_domain = link.split("//")[-1].split("/")[0]
                    to_page_id = db.get_page_id(to_domain)
                    if to_page_id is not None:
                        print(f"Found backlink from {current_domain} to {to_domain}. Inserting into DB.")
                        db.insert_link(from_page_id, to_page_id)

runner = CrawlerRunner()
d = runner.crawl(BacklinkSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()
