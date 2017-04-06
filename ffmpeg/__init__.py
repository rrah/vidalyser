import subprocess
import threading

class Ffmpeg(threading.Thread):
    
    _ffmpeg_cmd = ["ffmpeg"]
    _ffmpeg_head = ["-hide_banner", "-nostats", "-loglevel", "error"]
    _ffmpeg_filter_head = ["-c:v", "h264_cuvid", "-filter_complex"]
    _ffmpeg_filter = ["volume=1"]
    _ffmpeg_tail = ["-map", "[v]", "-an", "-c:v", "rawvideo", "-pix_fmt", "yuv420p", "-s", "626x340", "-f", "sdl"]
    
    def __init__(self, source):
        
        super().__init__(target = self.run)
        
        self.start()
        
    def form_ffmpeg(self):
        
        return [*self._ffmpeg_cmd, 
                *self._ffmpeg_head, 
                "-c:v", "mpeg2_cuvid", "-i", "udp://230.1.1.1:5000?localaddr=192.168.0.73", 
                *self._ffmpeg_filter_head, 
                *self._ffmpeg_filter, 
                *self._ffmpeg_tail, "Test"]
        
    def run(self, *args, **kwargs):
        
        cmd = self.form_ffmpeg()
        
        subprocess.run(cmd)
        
class MVTile(Ffmpeg):
    
    _ffmpeg_filter = ["[0:a]showvolume=v=0:o=v:h=10:w=340:b=1,pad=w=626:h=340:x=605[vol0]; [0:v]scale=w=605:h=340[vid0]; [vol0][vid0]overlay[v]"]
        
class Ffplay(Ffmpeg):
    
    _ffmpeg_cmd = ["ffplay"]
    
    def form_ffmpeg(self):
        
        return [*self._ffmpeg_cmd, *self._ffmpeg_head, "-i", "udp://230.1.1.1:5000?localaddr=192.168.0.73"]

if __name__ == '__main__':
    import time
    thread = Ffmpeg(None)
    
    time.sleep(10)