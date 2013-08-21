#!bin/bash/sh
cd /home/vigneshr/Desktop/CVPR2014/python/crawlers/crawlSrtFiles
scrapy crawl listSrtFiles -o /home/vigneshr/Desktop/CVPR2014/python/crawlers/crawlSrtFiles/results//off_centre.json -t json -a show_id=tvshow-673-1.html
scrapy crawl listSrtFiles -o /home/vigneshr/Desktop/CVPR2014/python/crawlers/crawlSrtFiles/results//off_centre.json -t json -a show_id=tvshow-673-2.html
