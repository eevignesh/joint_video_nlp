import os
import sys
import re
import zipfile

args = sys.argv

import os
import sys


def download(url, localFileName):
	"""Copy the contents of a file from a given URL
	to a local file.
	"""
	import urllib
	webFile = urllib.urlopen(url)
	localFile = open(localFileName, 'w')
	localFile.write(webFile.read())
	webFile.close()
	localFile.close()


script_file = args[1]
srt_directory = args[2]
dataset_dir = args[3]

fid = open(script_file)
ctr = 0
episodes = {}
for f in fid:
	#print(f)
	smatch_beg = re.search('http', f)
	smatch_end = re.search('pdf,', f)
	if smatch_beg is None or smatch_end is None:
		continue
	if smatch_beg.start(0) > smatch_end.start(0):
		continue
	script_file_link = f[smatch_beg.start(0):smatch_end.start(0)+3]
	#print(script_file_link)
	script_file_name, script_file_extension = os.path.splitext(script_file_link)
	script_path, script_name = os.path.split(script_file_name)
	
	match_regex = re.search('_\d+x\d+_', script_name)
	if match_regex is not None:
      		tv_show_name = script_name[0:match_regex.start(0)]
		episode_name = tv_show_name + match_regex.group(0)
		episode_value = match_regex.group(0)[1:-1]
		episode_name = episode_name.lower()
	else:
		continue

	tv_show_name = tv_show_name.lower()
	srt_file_name = srt_directory + '/' + tv_show_name + '.json'
    
	if os.path.exists(srt_file_name) and episode_name not in episodes.keys():
		json_fid = open(srt_file_name)
		strList = [jstr for jstr in json_fid if re.search(episode_value, jstr) is not None]
		json_fid.close()

		for s in strList:
			match_episodevalue = re.finditer(episode_value,s)
			g = [list(re.finditer('download-\d+.html', s[0:m.start(0)]))[-1].group(0) for m in match_episodevalue] #if match_download(i).start(0) < match_episodevalue(i).start(0)]
			if len(g) > 0:
				episodes[episode_name] = ('http://www.tvsubtitles.net/' + g[0], script_file_link)
				#print(script_name)
				ctr = ctr + 1
fid.close()
ctr = 0
for k in episodes.keys():
	print('%d : '%(ctr) + k + ' : ' + episodes[k][0] + ' : '  + episodes[k][1])
	
	episode_dir = dataset_dir + '/' + k[0:-1]
	
	if(not os.path.exists(episode_dir)):
		os.makedirs(episode_dir)
	
	episode_script_name = episode_dir + '/script.pdf'
	download(episodes[k][1], episode_script_name)
	
	episode_srt_zip = episode_dir + '/srt.zip'
	download(episodes[k][0], episode_srt_zip)
	episode_srt_filename = episode_dir + '/srt.txt'

	zfile = zipfile.ZipFile(episode_srt_zip)
	srt_name = zfile.namelist()[0]

	fd = open(episode_srt_filename, 'w')
	fd.write(zfile.read(srt_name))
	fd.close()
	
	os.remove(episode_srt_zip)	
	
	ctr += 1

print('\n number of script files with valid srt files = %d'%(ctr))

