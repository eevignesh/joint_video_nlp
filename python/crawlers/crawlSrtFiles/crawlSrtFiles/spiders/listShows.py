from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from crawlSrtFiles.items import CrawlsrtfilesItem
from scrapy.item import Item, Field

class sampleItem(Item):
  title = Field()
  url = Field()

class ListshowsSpider(CrawlSpider):
    name = 'listShows'
    allowed_domains = ['tvsubtitles.net']
    start_urls = ['http://www.tvsubtitles.net/tvshows.html']

# modify the default callback parser function
    def parse(self, response):
      x = HtmlXPathSelector(response)

      tvshows = []
      #rows = x.select('//tr')
      rows = x.select("//table[@id='table5']")
      rows = rows.select('//tr')
      #print(rows.extract())
      for row in rows:
        print(row.select('td/a/b/text()').extract())
        #print(row.select('/td/text()').extract())
        if len(row.select('td[2]/a/@href').extract()) > 0 and len(row.select('td[2]/a/b/text()').extract()) > 0:
          tvshow = sampleItem()
          tvshow['url'] = row.select('td[2]/a/@href').extract()
          tvshow['title'] = row.select('td[2]/a/b/text()').extract()
          tvshows.append(tvshow)
      
      print(tvshows)

      return tvshows
