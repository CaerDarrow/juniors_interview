import scrapy

BEAST_LIST_FILE_PATH = 'list_of_beasts.csv'


class BeastsSpider(scrapy.Spider):
    name = 'beasts'

    def start_requests(self):
        urls = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
        yield scrapy.Request(url=urls, callback=self.parse)

    def parse(self, response):
        data = response.xpath(
            "//*[@id='mw-pages']/div/div/div/ul/li/a/text()").getall()
        next_page = response.xpath("//*[@id='mw-pages']/a[2]/@href").get()

        with open(BEAST_LIST_FILE_PATH, mode='a', encoding='utf-8') as f:
            for beast in data:
                f.write("%s\n" % beast)

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
