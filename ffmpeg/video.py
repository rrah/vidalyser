'''
Created on 6 Apr 2017

@author: redsw
'''

import ffmpeg

class Vector(ffmpeg.Ffmpeg):
    
    _ffmpeg_filter = ["[0:v]vectorscope=g=color[v]"]
    
class Wave(ffmpeg.Ffmpeg):
    
    _ffmpeg_filter = ["[0:v]waveform=d=parade:c=7:g=green:r=0,scale=626x340[v]"]