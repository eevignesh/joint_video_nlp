#!bin/bash/sh
cd /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/off_centre.json -t json -a show_id=tvshow-673-1.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/off_centre.json -t json -a show_id=tvshow-673-2.html
