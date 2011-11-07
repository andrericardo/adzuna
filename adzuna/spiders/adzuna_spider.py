
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from adzuna.items import AdzunaItem

class AdzunaSpider(BaseSpider):
    name = "adzuna"
    allowed_domains = ["jobs.adzuna.co.uk"]
    start_urls = [
        "http://jobs.adzuna.co.uk/london/php",
        "http://jobs.adzuna.co.uk/london/python"
    ]
#
#    def parse(self, response):
#        filename = response.url.split("/")[-2]
#        open(filename, 'wb').write(response.body)
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        stat_values = hxs.select('//p[@class="stat_value"]/text()').extract()
        vacancies = stat_values[0]
        average = stat_values[1]
        print "vacancies: %s" % vacancies
        print "average: %s" % average
        item = AdzunaItem()
        item['vacancies'] = vacancies
        item['average'] = average
        return item


