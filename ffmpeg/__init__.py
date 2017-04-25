"""FFmpeg wrapper classes, for various FFmpeg processes.

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

import logging
import subprocess
import threading

logger = logging.getLogger(__name__)

class Ffmpeg(threading.Thread):
    
    """Thread to run and contain a single FFmpeg instance."""
    
    _ffmpeg_cmd = ["ffmpeg"]
    _ffmpeg_head = ["-hide_banner", "-nostats", "-loglevel", "fatal"]
    _ffmpeg_filter_head = ["-filter_complex"]
    _ffmpeg_filter = ["volume=1"]
    _ffmpeg_tail = ["-map", "[v]", "-an", "-c:v", "rawvideo", "-pix_fmt", "yuv420p", "-s", "626x340", "-f", "sdl"]
    _ffmpeg_name = "Ffmpeg"
    
    
    def __init__(self, source):
        
        """Construct and start the thread."""
        
        super().__init__(target = self.run)
        
        self.source = source
        self._name = "{} - {}".format(source, self._ffmpeg_name)
        self.start()
        
        
    def form_ffmpeg(self):
        
        """Form the command from various class and instance attributes."""
        
        cmd = [*self._ffmpeg_cmd, 
                *self._ffmpeg_head, 
                "-i", self.source, 
                *self._ffmpeg_filter_head, 
                *self._ffmpeg_filter, 
                *self._ffmpeg_tail, self._name]
        
        logger.debug(cmd)
        
        return cmd
        
        
    def run(self, *args, **kwargs):
        
        """Create and run the FFmpeg process."""
        
        cmd = self.form_ffmpeg()
        
        subprocess.run(cmd)
        
        
class MVTile(Ffmpeg):
    
    """Multiview style tile process."""
    
	
    _ffmpeg_filter = ["[0:a]showvolume=v=0:o=v:h=10:w=340:b=1:f=0.001,pad=w=626:h=340:x=605[vol0]; [0:v]scale=w=605:h=340[vid0]; [vol0][vid0]overlay[v]"]
        
        
class Ffplay(Ffmpeg):
    
    """Runs and holds an FFplay process instead of FFmpeg."""
    
    _ffmpeg_cmd = ["ffplay"]
    
    
    def form_ffmpeg(self):
        
        """Overload of Ffmpeg.form_ffmpeg, as command doesn't want filters/encoding."""
        
        return [*self._ffmpeg_cmd, *self._ffmpeg_head, "-i", self.source]
    

class Ffprobe(Ffmpeg):
    
    """Runs and holds an FFprobe process instead of FFmpeg."""
    
    _ffmpeg_cmd = ["ffprobe"]
    
    
    def __init__(self, source, gui):
        
        super().__init__(source)
        
        self.gui = gui
        
    
    def form_ffmpeg(self):
        
        """Overload of Ffmpeg.form_ffmpeg, as command doesn't want filters/encoding."""
        
        return [*self._ffmpeg_cmd, "-hide_banner", "-i", self.source]
    
    
    def run(self, *args, **kwargs):
        
        """Run FFprobe, and put the output into the required TK window."""
        
        cmd = self.form_ffmpeg()
        
        output = subprocess.check_output(cmd, stderr = subprocess.STDOUT)
        
        self.gui.set(output.decode("utf-8"))


if __name__ == 'vidalyser':
    import time
    thread = Ffmpeg(None)
    
    time.sleep(10)