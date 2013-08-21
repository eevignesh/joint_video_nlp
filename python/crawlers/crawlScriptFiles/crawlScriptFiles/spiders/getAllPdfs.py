from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from crawlScriptFiles.items import CrawlscriptfilesItem
from scrapy.item import Item, Field
import ntpath
import re

def path_leaf(path):
  head, tail = ntpath.split(path)
  return tail or ntpath.basename(head)

class sampleItem(Item):
  title = Field()
  url = Field()
  orig_name = Field()

class GetallpdfsSpider(CrawlSpider):
    name = 'getAllPdfs'
    allowed_domains = ['sites.google.com', 'leethomson.myzen.co.uk', 'zen134237.zen.co.uk']
    start_urls = ['https://sites.google.com/site/tvwriting']
    rules = [Rule(SgmlLinkExtractor(allow=r'/*'), callback='parse_item', follow=True)]

# modify the default callback parser function
    def parse_item(self, response):
      x = HtmlXPathSelector(response)
      tvshows = []
      all_links = x.select("//a/@href").extract()
      for a in all_links:
        #print(a)
        a_text = str(a)
        if '.pdf' in a_text:
          print(a_text)
          tvshow = sampleItem()
          tvshow['title'] = path_leaf(a_text)
          a_text = a_text.replace('\"','')
	  if re.search('http', a_text) is None:
		tvshow['url'] = response.url + a_text
          else:
          	tvshow['url'] = a_text
          tvshow['orig_name'] = a_text
	  tvshows.append(tvshow)
          
      return tvshows
