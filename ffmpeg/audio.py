'''
Created on 6 Apr 2017

@author: redsw
'''

import ffmpeg

class Vector(ffmpeg.Ffmpeg):
    
    """Audio phase vectorscope process."""
    
    _ffmpeg_filter = ["[0:a]avectorscope=draw=line:s=626x340[v]"]
    _ffmpeg_name = "Audio Phase"
    
    
class Loudness(ffmpeg.Ffmpeg):
    
    """Audio loudness process."""
    
    _ffmpeg_filter = ["[0:a]ebur128=video=1:meter=18:peak=true:size=854x480[v][a]", "-map", "[a]", "-f", "null", "-"]
    _ffmpeg_name = "Loudness"
    
    
class Spectrum(ffmpeg.Ffmpeg):
    
    """Audio spectrum process."""
    
    _ffmpeg_filter = ["[0:a]showspectrum=slide=scroll:s=636x340:color=intensity:mode=separate,setpts=N/(25*TB)[v]"]
    _ffmpeg_name = "Audio Spectrum"
    
