'''
written by Vignesh Ramanathan
Aug, 2013

NOTE: first generate the file <show_list_file> by running
(see getShowId.py for more details)

call as python genScrapySrtJobs.py <job-directory> <result-directory>

@paramters:
  job-directory - the directory where all the job files will be saved
  result-directory - each of the jobs will save the links of the srt-files
                     in json format in this folder
                     (existing files in this directory will be removed)
'''

import os
import sys
from getShowId import *
import re

args = sys.argv
cmd_dir = os.getcwd()
cmd_dir = cmd_dir + '/crawlSrtFiles'
#cmd_dir = cmd_dir.replace('crawlScriptFiles', 'crawlSrtFiles')

if len(args)<3:
  print('Minimum need 2 argument giving job dir, result dir')

jobDir = args[1]
resultDir = args[2]

srt_matches = getSrtHtmlList()

ctr = 0
for key in srt_matches.srt_show_list:
  job_file = jobDir + '/crawl_%03d.sh'%(ctr)
  fid = open(job_file, 'w')
  fid.write('#!bin/bash/sh\n')
  fid.write('cd %s\n'%(cmd_dir))
  key_name = key.replace(' ', '_')
  home_id_html = srt_matches.srt_show_list[key]
  match_season = re.search('-\d+.html', home_id_html)
  base_name = home_id_html[0:match_season.start(0)]
  num_seasons = int(match_season.group(0)[1:-5])
  for season in range(1, num_seasons+1):
    tv_show_id = '%s-%d.html'%(base_name, season)
    if os.path.exists('%s/%s.json'%(resultDir, key_name)):
      os.system('rm %s/%s.json'%(resultDir, key_name))
    key_name = key_name.replace('\'', '_')
    fid.write('scrapy crawl listSrtFiles -o %s/%s.json -t json -a show_id=%s\n'%(resultDir, key_name, tv_show_id))
  fid.close()
  ctr = ctr + 1
