from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from crawlSrtFiles.items import CrawlsrtfilesItem
from scrapy.item import Item, Field

class sampleItem(Item):
  title = Field()
  url = Field()
  filename = Field()

class ListsrtfilesSpider(CrawlSpider):
    name = 'listSrtFiles'
    allowed_domains = ['tvsubtitles.net']
    start_urls = []
    rules = (Rule(SgmlLinkExtractor(allow=r'/subtitle-\d+\.html'), callback='parse_item', follow=True), Rule(SgmlLinkExtractor(allow=r'/episode'), callback='parse_item', follow=True))

    def __init__(self, show_id = None, *args, **kwargs):
      super(ListsrtfilesSpider, self).__init__(*args, **kwargs)
      self.start_urls = ['http://www.tvsubtitles.net/%s' % (show_id)]

    def parse_item(self, response):
      x = HtmlXPathSelector(response)

      tvshows = sampleItem()

# get all table entries in the form of rows 
      rows = x.select('//tr')
# get the entry against the listing called filename which will give the details of the srt file
      tvshows['filename'] = ''.join([row.select('td[3]/text()').extract()[0] for row in rows if 'filename' in ''.join(row.select('td/b/text()').extract())])
      print(response.url + ' --- ' + tvshows['filename'])
 
# Only extract english srts
      if 'en.srt' in tvshows['filename']:
        tvshows['title'] = x.select('//h2/text()').extract()
        tvshows['url'] = response.url
        tvshows['url'] = tvshows['url'].replace('subtitle-', 'download-')
      else:
        tvshows = sampleItem()
      return tvshows
