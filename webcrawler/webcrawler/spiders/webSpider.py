import scrapy


class WebCrawler(scrapy.Spider):
    name = 'WebCrawler'
    with open('urls.txt') as url:
        all_urls = url.read().split('/n')
    final_url_list = []
    for url in all_urls:
        final_url_list.append(url)
    print(final_url_list)
    start_url = final_url_list

    def parse(self, response):
        return response




