import os
import sys
import glob

#episodeDir = '/afs/cs.stanford.edu/u/vigneshr/scratch/CVPR2014/castle_1x02'
#outDir = '/afs/cs.stanford.edu/u/vigneshr/www/castle_1x02'

episodeDir = '/afs/cs.stanford.edu/u/vigneshr/scratch/CVPR2014/HIMYM_1x01'
outDir = '/afs/cs.stanford.edu/u/vigneshr/www/HIMYM_1x01'


fileList = glob.glob('%s/videos/*.ogg'%(episodeDir))

outFile_index = '%s/index_page.html'%(outDir)
fid_index = open(outFile_index, 'w')
fid_index.write('<!DOCTYPE html>\n')
fid_index.write('<html>\n')
fid_index.write('<body>\n')
fid_index.write('There are 10 videos per page along with descriptions for this episode.\n <br> <br> \n')
fid_index.write('<a href=page1.html> page 1 </a> <br>\n')

page_ctr = 1

outFile = '%s/page%d.html'%(outDir, page_ctr)
fid_html = open(outFile, 'w')
fid_html.write('<!DOCTYPE html>\n')
fid_html.write('<html>\n')
fid_html.write('<body>\n')
fid_html.write('<table border = \"1\">\n')

for i in range(0, len(fileList)):
  #video_src = episodeDir + '/videos/clip_%04d.ogg'%(i)
  video_src = 'videos/' + 'clip_%04d.ogg'%(i)
 
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

  if ((i+1)%10==0):
    fid_html.write('</table>\n')
    fid_html.write('</body>\n')
    fid_html.write('</html>\n')
    fid_html.close()

    page_ctr = page_ctr + 1

    fid_index.write('<a href=page%d.html> page %d </a> <br>\n'%(page_ctr, page_ctr))

    outFile = '%s/page%d.html'%(outDir, page_ctr)
    fid_html = open(outFile, 'w')
    fid_html.write('<!DOCTYPE html>\n')
    fid_html.write('<html>\n')
    fid_html.write('<body>\n')
    fid_html.write('<table border = \"1\">\n')


fid_html.write('</table>\n')
fid_html.write('</body>\n')
fid_html.write('</html>\n')
fid_html.close()


fid_index.write('</body>\n')
fid_index.write('</html>\n')
fid_index.close()
