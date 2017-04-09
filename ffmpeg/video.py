'''
Created on 6 Apr 2017

@author: redsw
'''

import ffmpeg

class Vector(ffmpeg.Ffmpeg):
    
    _ffmpeg_filter = ["[0:v]vectorscope=g=color[v]"]
    _ffmpeg_name = "Vectorscope"
    
class Wave(ffmpeg.Ffmpeg):
    
    _ffmpeg_filter = ["[0:v]waveform=d=parade:c=7:g=green:r=0:fl=dots,scale=626x340[v]"]
    _ffmpeg_name = "Video Waveform"
