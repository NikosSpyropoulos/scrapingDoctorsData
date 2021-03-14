import scrapy


class DoctorsDataSpider(scrapy.Spider):
    name = 'AdvCategory'

    start_urls = [
        'https://www.vrisko.gr/search/giatros/ioannina/'
    ]

    def parse(self, response):
        for advCategory in response.xpath("//div[@class = 'AdvAreaLeft']/div"):
            yield {
                'Office Name': advCategory.xpath("div/div/h2/a/meta/@content".strip()).extract_first(),
                'Description': advCategory.xpath("div/div/h2/meta/@content".strip()).extract_first(),
                'Category': advCategory.xpath("div[3]/div/div[3]/div/span/text()".strip()).extract_first(),
                'Address': advCategory.xpath("div[3]/div/div[2]/text()".strip()).extract_first(),
                'Office Phone': advCategory.xpath("div[4]/div[3]/div[2]/text()".strip()).extract_first(),
                'Office Phone': advCategory.xpath("div[4]/div[3]/div[2]/text()".strip()).extract_first(),
                'Mobile Phone': advCategory.xpath("div[4]/div[3]/div[5]/text()".strip()).extract_first(),
                'Email': advCategory.xpath("div[4]/div[3]/div[8]/a[contains(@href, 'mailto')]/@href".strip()).extract_first(),
                'Website': advCategory.xpath("div[4]/div[3]/div[11]/a/text()".strip()).extract_first()

            }

        # for advCategory in response.xpath("//div[@class='PhonesBox']"):
        #     yield {
        #         'Phone': advCategory.xpath("label/text()").extract_first()
        #     }
