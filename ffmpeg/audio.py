"""FFmpeg processes that analyse audio.

Author: Robert Walker <rrah99@gmail.com>

    This file is part of Vidalyser.
    
    Vidalyser is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    Vidalyser is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with Vidalyser.  If not, see <http://www.gnu.org/licenses/>.
"""

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
    
