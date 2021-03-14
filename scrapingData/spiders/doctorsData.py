import scrapy


class DoctorsDataSpider(scrapy.Spider):
    name = 'AdvCategory'

    start_urls = [
        'https://www.vrisko.gr/search/giatros/ioannina/'
    ]

    def parse(self, response):
        for advCategory in response.xpath("//div[@class = 'AdvAreaLeft']//a"):
            yield {
                'Office Name': advCategory.xpath("meta/@content").extract_first()
            }

        # for advCategory in response.xpath("//div[@class='PhonesBox']"):
        #     yield {
        #         'Phone': advCategory.xpath("label/text()").extract_first()
        #     }
