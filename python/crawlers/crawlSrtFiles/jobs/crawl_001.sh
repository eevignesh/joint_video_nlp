#!bin/bash/sh
cd /home/vigneshr/Desktop/CVPR2014/python/crawlers/crawlSrtFiles
scrapy crawl listSrtFiles -o /home/vigneshr/Desktop/CVPR2014/python/crawlers/crawlSrtFiles/results//new_girl.json -t json -a show_id=tvshow-977-1.html
scrapy crawl listSrtFiles -o /home/vigneshr/Desktop/CVPR2014/python/crawlers/crawlSrtFiles/results//new_girl.json -t json -a show_id=tvshow-977-2.html
