from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import re
import urllib2


'''
@brief: inherits from HTMLParser and is used to parse the html page showing the list of episodes
        in a tv-show and identify the english srt file pages

@members:
  episode_pages - stores the link to the download page for the srt file
  episode_names - list of (episode_number in format such as 04x02 for season.4 and episode.2, name of episode)

'''
class EpisodeListParser(HTMLParser):
    episode_pages = []
    episode_names = []

    # entry point to start parsing the tv-show page
    def get_episode_names(self, html_data):
        self.tag_stack = []
        self.episode_pages = []
        self.episode_names = []
        self.episode_number = []
        self.episod_name_identified = False
        self.feed(html_data)
        
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag.lower())
        
        for attr in attrs:
          # get all the links
          if attr[0] == 'href':
            self.subtitle_file = attr[1]
            
          # download only the srt which has an english flag image
          if tag == 'img' and attr[0]=='src' and self.tag_stack[-2] == 'a':
              if 'images/flags/en.gif' in attr[1]:
                if self.episode_name_identified:
                  self.episode_pages.append(self.subtitle_file)


    def handle_endtag(self, tag):
        # if end of row, then start new episode entry
        if tag == 'tr':
          self.episode_name_identified = False
        self.tag_stack.pop()

    def handle_data(self, data):
        if len(self.tag_stack)>0:
          
          # check if episode number is given
          if self.tag_stack[-1] == 'td':
            if not(not(re.search('^[0-9]+x[0-9]+$',data))):
              self.episode_number = data
              #print('EP number = ' + data)

          # enter the name only if the episode number was also found before
          if self.tag_stack[-1] == 'b':            
            if not(not(self.episode_number)):
              self.episode_names.append((self.episode_number, data))
              self.episode_number = []
              self.episode_name_identified = True
              #print('DATA = ' + data)
            
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
'''
@brief: inherits from HTMLParser and is used to parse the html page showing the list of tv-show names

@members:
  show_pages - list of links to the page for the tv-show
  show_names - list of tv-show names

'''


class ShowListParser(HTMLParser):
    show_pages = []
    show_names = []

    # entry point
    def get_show_names(self, html_data):
        self.tag_stack = []
        self.feed(html_data)
        
    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag.lower())

        # get the show-page link
        for attr in attrs:
          if attr[0] == 'href':
            self.show_pages.append(attr[1])
    
    def handle_endtag(self, tag):
        self.tag_stack.pop()

    def handle_data(self, data):
        if len(self.tag_stack)>0:
          if self.tag_stack[-1] == 'b':
            if len(self.show_names) == len(self.show_pages):
              self.show_names[-1] = self.show_names[-1] + ' ' + data
            else:
              self.show_names.append(data)
            
    def handle_entityref(self, name):
        c = unichr(name2codepoint[name])

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))

'''
fid = open('tv_shows_srt.html')
parser = ShowListParser()
data = [f for f in fid]
fid.close()
data = " ".join(data)
parser.get_show_names(data)
show_data = [ (parser.show_names[i], 'www.tvsubtitles.net/' + parser.show_pages[i]) for i in range(0, len(parser.show_pages))]
'''
episode_parser = EpisodeListParser()
#fid = open('sample_episode_page.html')
#data = [f for f in fid]
#fid.close()
#data = " ".join(data)
aResp = urllib2.urlopen('http://www.tvsubtitles.net/tvshow-42-4.html')
data = aResp.read()
data = data.replace('SCR\'+\'IPT', 'SCRIPT')

episode_parser.get_episode_names(data)

for i in range(0, len(episode_parser.episode_pages)):
  m = re.search('-[0-9]+.html', episode_parser.episode_pages[i])
  if not(not(m)):
    print('www.tvsubtitles.net/download' + m.group(0))
  print('%s %s %s\n'%(episode_parser.episode_pages[i], episode_parser.episode_names[i][0], episode_parser.episode_names[i][1]))
  #print('%s: %s\n'%(episode_parser.episode_names[i][0], episode_parser.episode_names[i][1]))
