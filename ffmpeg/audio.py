'''
Created on 6 Apr 2017

@author: redsw
'''

import ffmpeg

class Vector(ffmpeg.Ffmpeg):
    
    _ffmpeg_filter = ["[0:a]avectorscope=draw=line:s=626x340[v]"]
    
class Loudness(ffmpeg.Ffmpeg):
    
    _ffmpeg_filter = ["[0:a]ebur128=video=1:meter=18:peak=true:size=854x480[v][a]", "-map", "[a]", "-f", "null", "-"]
    
class Spectrum(ffmpeg.Ffmpeg):
    
    _ffmpeg_filter = ["[0:a]showspectrum=slide=scroll:s=636x340:color=intensity:mode=separate,setpts=N/(25*TB)[v]"] 
    