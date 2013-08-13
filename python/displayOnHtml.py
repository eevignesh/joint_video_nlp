import os
import sys
import glob

episodeDir = '/afs/cs.stanford.edu/u/vigneshr/scratch/CVPR2014/castle_1x02'
outFile = 'castle_2.html'

fid_html = open(outFile, 'w')

fileList = glob.glob('%s/videos/*.ogg'%(episodeDir))

fid_html.write('<!DOCTYPE html>\n')
fid_html.write('<html>\n')
fid_html.write('<body>\n')
fid_html.write('<table border = \"1\">\n')

for i in range(0, 100): #len(fileList)):
  #video_src = episodeDir + '/videos/clip_%04d.ogg'%(i)
  video_src = 'castle2_videos/' + 'clip_%04d.ogg'%(i)
 
  fid_descr = open(episodeDir + '/descriptions/clip_%04d.txt'%(i))
  
  des = ''
  for f in fid_descr:
    des = des + f
  fid_descr.close()

  des.replace('\n', ' ')
  fid_html.write('<tr>\n')

  # video id
  fid_html.write('<td> %d </td>\n'%(i))
  
  # video
  fid_html.write('<td>\n')
  fid_html.write('<video width = \"320\" height = \"240\" controls>\n')
  fid_html.write('<source src = \"%s\" type = \"video/ogg\">\n'%(video_src))
  fid_html.write('Your browser does not support video tag.\n')
  fid_html.write('</td>\n')

  # video description
  fid_html.write('<td>\n')
  fid_html.write('%s\n'%(des))
  fid_html.write('</td>\n')

  fid_html.write('</tr>\n')

fid_html.write('</table>\n')
fid_html.write('</body>\n')
fid_html.write('</html>\n')
