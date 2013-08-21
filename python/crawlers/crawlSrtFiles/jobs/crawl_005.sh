#!bin/bash/sh
cd /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/community.json -t json -a show_id=tvshow-507-1.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/community.json -t json -a show_id=tvshow-507-2.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/community.json -t json -a show_id=tvshow-507-3.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/community.json -t json -a show_id=tvshow-507-4.html
