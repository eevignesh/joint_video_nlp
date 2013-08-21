#!/bin/python2.6

import os
import sys


if (len(sys.argv) < 4):
  print('provide 3 arguments: 1. alignment output file, 2. video file, 3. output directory')
  sys.exit()

alignOutfile = sys.argv[1]
videoFile = sys.argv[2]
outDir = sys.argv[3]

outVideoDir = outDir + '/' + 'videos/'
outDescrDir = outDir + '/' + 'descriptions/'

if not(os.path.exists(outDir)):
  os.makedirs(outDir)

if not(os.path.exists(outVideoDir)):
  os.makedirs(outVideoDir)

if not(os.path.exists(outDescrDir)):
  os.makedirs(outDescrDir)

fid = open(alignOutfile)

# open job file to write ffmpeg commands
job_file = outDir + '/job_ffmpeg.sh'
fid_ffmpeg = open(job_file, 'w')

# 0 -> time-begin, 1 -> time-duration, 2 -> description
lineId = 0
ss_time = 'NULL'
t_time = 'NULL'
clip_ctr = 0

for f in fid:
  if (f == '\n'):
    lineId = 0
    ss_time = 'NULL'
    t_time = 'NULL'
    continue

  if (lineId==0):
    ss_time = f
    lineId = 1
    continue

  if (lineId==1):
    t_time = f
    lineId = 2
    continue

  if (lineId == 2):
    if (ss_time == 'NULL' or t_time == 'NULL'):
      print('Error at clip_id %04d ... '%(clipId))
      print('ss = %s'%(ss_time))
      print('t = %s'%(t_time))
      sys.exit()

    # write the description
    outDescrFile = outDescrDir + 'clip_%04d.txt'%(clip_ctr)
    fid_out = open(outDescrFile, 'w')
    fid_out.write('%s\n'%(f))
    fid_out.close()

    # create the ffmpeg job command
    outVideoFile = outVideoDir + 'clip_%04d.mp4'%(clip_ctr)
    #ffmpeg_job = 'ffmpeg -ss %s -t %s -vcodec copy -acodec copy -i %s %s'%(ss_time[0:-1], t_time[0:-1], videoFile, outVideoFile)
    ss_time2 = int(ss_time[0:2])*3600 + int(ss_time[3:5])*60 + int(ss_time[6:8])
    t_time2 = int(t_time[0:2])*3600 + int(t_time[3:5])*60 + int(t_time[6:8])
    t_time2 = t_time2 + ss_time2 - 1
    t_time2_s = '%02d:%02d:%02d\n'%(int(t_time2/3600), int((t_time2 % 3600)/60), ((t_time2 % 3600) % 60) )
    #ffmpeg_job = 'ffmpeg -ss %s -t %s -vcodec copy -acodec copy -i %s %s'%(ss_time[0:-1], t_time2[0:-1], videoFile, outVideoFile)
    ffmpeg_job = 'mencoder -ss %s -endpos %s -ovc copy -oac copy %s -o %s'%(ss_time[0:-1], t_time[0:-1], videoFile, outVideoFile)

    # for html5 compatiblity
    outVideoFile_ogg = outVideoDir + 'clip_%04d.ogg'%(clip_ctr)
    ffmpeg_ogg_job = 'ffmpeg -i %s -acodec libvorbis -aq 50 %s'%(outVideoFile, outVideoFile_ogg)
    fid_ffmpeg.write('%s\n'%(ffmpeg_job))
    fid_ffmpeg.write('%s\n'%(ffmpeg_ogg_job))

    clip_ctr = clip_ctr + 1
    lineId = 0

fid_ffmpeg.close()
fid.close()

