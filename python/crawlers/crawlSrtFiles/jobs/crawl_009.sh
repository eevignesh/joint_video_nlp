#!bin/bash/sh
cd /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/happy_endings.json -t json -a show_id=tvshow-909-1.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/happy_endings.json -t json -a show_id=tvshow-909-2.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/happy_endings.json -t json -a show_id=tvshow-909-3.html
