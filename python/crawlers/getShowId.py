'''
written by Vignesh Ramanathan
Aug, 2013
Requirements: install Levenshtein python package

NOTE:
look at globals.py for useful file names
first generate the file <show_list_file> by running
(after entering ./crawSrtFiles)
scrapy crawl listShows -o <show_list_file> -t csv
The above command crawls tvsubtitles.net to get list of tv shows

next generate the file <script_list_file> by running
(after entring ./crawlScriptFiles/)
scrapy crawl getAllPdfs -o <script_list_file> -t csv
'''

import os
from Levenshtein import *
import re
from globals import *

# Levenshtein threshold inorder to get corresponding srt files
SCORE_THRESH = 0.9

'''
@members:
  script_files - for each script file in the list script_files[$file_name] = download_link for the $file_name
  srt_show_list - srt_show_list[$show_name_from_tvsubtitles.net] = $id_in_tvsubtitle.net, for all tv-show-names
                 in pdf script directory
'''

class scriptMatches:

  def __init__(self):
    self.show_files = {}
    self.srt_show_list = {}


'''
@brief: identify whether there exist srt files for the tv-series corresponding to script files in the script-list
        and also generate a list of unique tv-series episodes in the list of script files to crawl tvsubtitles.net

@output: an object of srtMatches

'''

def getSrtHtmlList():

  script_list = {}
  fid = open(script_list_file)
  for f in fid:
    [beg_part, sep_part, end_part] = f.partition('.pdf,')
    script_list[end_part] = beg_part + '.pdf'
  fid.close()

  fid = open(show_list_file)
  show_list = [f for f in fid]
  fid.close()

  script_files = {}
  srt_show_list = {}

  for pdf_name in script_list:
    match_regex = re.search('_\d+x\d+_', pdf_name)
    if match_regex is not None:
      tv_show_name = pdf_name[0:match_regex.start(0)].replace('_', ' ').lower()
    else:
      continue
    print(tv_show_name)
    shows = []
    max_score = 0
    ctr = 0
    for f in show_list:
      [show_id, seperator, show_name] = f.partition(',')
      show_name = show_name.rstrip('\n\r')
      match_score = ratio(show_name.lower(), tv_show_name)
      shows.append((show_id, show_name.lower(), match_score))
      if match_score > max_score:
        max_score = match_score
        max_id = ctr
      ctr = ctr + 1
    
    if max_score > SCORE_THRESH:
      #show_matches[full_episode_name] = (shows[max_id][1].replace(' ' , '_'), ep_id)
      script_files[tv_show_name + match_regex.group(0)[0:-1]] = script_list[pdf_name]
      srt_show_list[shows[max_id][1].replace(' ' , '_')] = shows[max_id][0]

  print('Number of possible valid scripts = %d, Number of shows = %d' % (len(script_files), len(srt_show_list)) )
  
  scriptListMatches = scriptMatches()
  scriptListMatches.script_files = script_files
  scriptListMatches.srt_show_list = srt_show_list

  return(scriptListMatches)

'''
	Starting main function
'''

print('Starting matching ...')
scriptListMatchesWhole = getSrtHtmlList()


