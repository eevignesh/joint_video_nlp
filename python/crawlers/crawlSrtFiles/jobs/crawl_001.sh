#!bin/bash/sh
cd /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/new_girl.json -t json -a show_id=tvshow-977-1.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/new_girl.json -t json -a show_id=tvshow-977-2.html
