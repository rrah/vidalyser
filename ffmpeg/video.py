"""FFmpeg processes that analyse video.

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
    
    """Video Colour Vectorscope process."""
    
    _ffmpeg_filter = ["[0:v]vectorscope=g=color[v]"]
    _ffmpeg_name = "Vectorscope"
    
class Wave(ffmpeg.Ffmpeg):
    
    """Video Waveform (YUV Parade) process."""
    
    _ffmpeg_filter = ["[0:v]waveform=d=parade:c=7:g=green:r=0:fl=dots,scale=626x340[v]"]
    _ffmpeg_name = "Video Waveform"
