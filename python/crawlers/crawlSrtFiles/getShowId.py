'''
written by Vignesh Ramanathan
Aug, 2013
Requirements: install Levenshtein python package

NOTE: first generate the file show_list.csv by running
scrapy crawl listShows -o show_list.csv -t csv

The above command crawls tvsubtitles.net to get list of tv shows
'''

import os
from Levenshtein import *
import re

# Levenshtein threshold inorder to get corresponding srt files
SCORE_THRESH = 0.9

'''
@members:
  show_matches - for each script file in the directory show_matches[$file_name] = $show_name_from_tvsubtitles.net
  srt_show_list - srt_show_list[$show_name_from_tvsubtitles.net] = $id_in_tvsubtitle.net, for all tv-show-names
                 in pdf script directory
'''

class srtMatches:

  def __init__(self):
    self.show_matches = {}
    self.srt_show_list = {}


'''
@brief: identify the show name as specified corresponding to each script pdf-file in the script directory
        and also generate a list of unique tv-series episodes in the script directory to crawl tvsubtitles.net

@parameters:
  pdfDirectory - the script directory contatining the pdf script files

@output: an object of srtMatches

'''

def getSrtHtmlList(pdfDirectory = '/home/vignesh/Desktop/CVPR2014/scriptDataGoogle/'):
  list_of_episodes_all = os.listdir(pdfDirectory)

  list_of_episodes = [(l[0:re.search('_\d+x\d+_', l).start(0)].replace('_', ' ').lower(), re.search('_\d+x\d+_', l).group(0)[1:-1], l) for l in list_of_episodes_all if re.search('_\d+x\d+_', l) is not None]

  fid = open('show_list.csv')
  show_list = [f for f in fid]
  fid.close()

  show_matches = {}
  srt_show_list = {}

  for tv_show_name, ep_id, full_episode_name in list_of_episodes:

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
      show_matches[full_episode_name] = (shows[max_id][1].replace(' ' , '_'), ep_id)
      srt_show_list[shows[max_id][1].replace(' ' , '_')] = shows[max_id][0]

  print('Number of matches = %d, Number of shows = %d' % (len(show_matches), len(srt_show_list)) )
  
  scriptDirMatches = srtMatches()
  scriptDirMatches.show_matches = show_matches
  scriptDirMatches.srt_show_list = srt_show_list

  return(scriptDirMatches)
