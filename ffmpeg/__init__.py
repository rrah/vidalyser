import subprocess
import threading

class Ffmpeg(threading.Thread):
    
    _ffmpeg_cmd = ["ffmpeg"]
    _ffmpeg_head = ["-hide_banner", "-nostats", "-loglevel", "fatal"]
    _ffmpeg_filter_head = ["-filter_complex"]
    _ffmpeg_filter = ["volume=1"]
    _ffmpeg_tail = ["-map", "[v]", "-an", "-c:v", "rawvideo", "-pix_fmt", "yuv420p", "-s", "626x340", "-f", "sdl"]
    _ffmpeg_name = "Ffmpeg"
    
    def __init__(self, source):
        
        super().__init__(target = self.run)
        
        self.source = source
        self._name = "{} - {}".format(source, self._ffmpeg_name)
        self.start()
        
    def form_ffmpeg(self):
        
        cmd = [*self._ffmpeg_cmd, 
                *self._ffmpeg_head, 
                "-i", self.source, 
                *self._ffmpeg_filter_head, 
                *self._ffmpeg_filter, 
                *self._ffmpeg_tail, self._name]
        
        print(cmd)
        
        return cmd
        
    def run(self, *args, **kwargs):
        
        cmd = self.form_ffmpeg()
        
        subprocess.run(cmd)
        
class MVTile(Ffmpeg):
    
    _ffmpeg_filter = ["[0:a]showvolume=v=0:o=v:h=10:w=340:b=1,pad=w=626:h=340:x=605[vol0]; [0:v]scale=w=605:h=340[vid0]; [vol0][vid0]overlay[v]"]
        
class Ffplay(Ffmpeg):
    
    _ffmpeg_cmd = ["ffplay"]
    
    def form_ffmpeg(self):
        
        return [*self._ffmpeg_cmd, *self._ffmpeg_head, "-i", self.source]
    

class Ffprobe(Ffmpeg):
    
    _ffmpeg_cmd = ["ffprobe"]
    
    def __init__(self, source, gui):
        
        super().__init__(source)
        
        self.gui = gui
    
    def form_ffmpeg(self):
        
        return [*self._ffmpeg_cmd, "-hide_banner", "-i", self.source]
    
    def run(self, *args, **kwargs):
        
        cmd = self.form_ffmpeg()
        
        output = subprocess.check_output(cmd, stderr = subprocess.STDOUT)
        
        self.gui.set(output.decode("utf-8"))
        
        print(output)

if __name__ == '__main__':
    import time
    thread = Ffmpeg(None)
    
    time.sleep(10)