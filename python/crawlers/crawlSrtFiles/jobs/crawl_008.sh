#!bin/bash/sh
cd /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/modern_family.json -t json -a show_id=tvshow-510-1.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/modern_family.json -t json -a show_id=tvshow-510-2.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/modern_family.json -t json -a show_id=tvshow-510-3.html
scrapy crawl listSrtFiles -o /home/vignesh/Desktop/CVPR2014/crawlers/crawlSrtFiles/results/modern_family.json -t json -a show_id=tvshow-510-4.html
