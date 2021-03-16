import scrapy
from scrapy.loader import ItemLoader


class DoctorsDataSpider(scrapy.Spider):
    name = 'doctors'

    start_urls = [
        'https://www.vrisko.gr/search/giatros/ioannina/'
    ]

    def parse(self, response):
        blank_line = 0
        for doctor in response.xpath("//div[@class = 'AdvAreaLeft']/div"):
            # l = ItemLoader(item=DoctorsItem(), selector=doctor)
            # l.add_xpath('Office_Name', "div/div/h2/a/meta/@content")
            # yield l.load_item()
            if blank_line % 2 != 0:
                blank_line = blank_line + 1
                continue
            yield {
                'Office_Name': doctor.xpath("div/div/h2/a/meta/@content").extract_first(),
                'Description': doctor.xpath("div/div/h2/meta/@content").extract_first(),
                'Category': doctor.xpath("div[3]/div/div[3]/div/span/text()").extract_first(),
                'Address': doctor.xpath("div[3]/div/div[2]/text()").extract_first().strip(),
                'Office_Phone': doctor.xpath("div[4]/div[3]/div[2]/text()").extract_first(),
                'Mobile_Phone': doctor.xpath("div[4]/div[3]/div[5]/text()").extract_first(),
                'Email': doctor.xpath("div[4]/div[3]/div[8]/a[contains(@href, 'mailto')]/@href").extract_first(),
                'Website': doctor.xpath("div[4]/div[3]/div[11]/a/text()").extract_first().strip()
            }
            blank_line = blank_line + 1
        for doctor in response.xpath("//div[@class = 'LightAdvAreaLeft']/div"):
            if blank_line % 2 != 0:
                blank_line = blank_line + 1
                continue
            yield {
                'Office_Name': doctor.xpath("div/div/h2/a/meta/@content").extract_first(),
                'Description': doctor.xpath("div/div/h2/meta/@content").extract_first(),
                'Category': doctor.xpath("div[2]/div/div/div[1]/label/span/text()").extract_first(),
                'Address': doctor.xpath("div[2]/div/div/div[2]/text()").extract_first(),
                'Office_Phone': doctor.xpath("div[2]/div[2]/div[3]/div[2]/text()").extract_first(),
                'Mobile_Phone': doctor.xpath("div[2]/div[2]/div[3]/div[5]/text()").extract_first(),
                'Email': doctor.xpath("div[2]/div[2]/div[3]/div[8]/a[contains(@href, 'mailto')]/@href").extract_first(),
                'Website': doctor.xpath("div[2]/div[2]/div[3]/div[11]/a/text()").extract_first()
            }
            blank_line = blank_line + 1

        page_number = response.xpath("//*[@id='pagerPlaceHolder']/div/div[2]/span.text()").extract_first()
        num = int(page_number) + 1
        next_page = response.xpath(
            "//*[@id='pagerPlaceHolder']/div/div[2]/a["+page_number+"]/@href").extract_first()
        if next_page:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)
