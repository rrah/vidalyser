import ffmpeg
import ffmpeg.audio
import ffmpeg.video

import tkinter

import gui.ffprobe

class Launch_bar(tkinter.Frame):
    def __init__(self, master):
        
        super().__init__(master)
        
        self.master = master
        
        self.stream_input = tkinter.Entry(master)
        self.stream_input.pack(fill = tkinter.X, expand = 1)
        self.stream_input.insert(0, "udp://239.1.1.1:5000?localaddr=192.168.1.10")
        
        self.play_button = tkinter.Button(master, text="Play original", command=self.start_play)
        self.play_button.pack(side = tkinter.LEFT)
        
        self.probe_button = tkinter.Button(master, text="Probe", command=self.start_probe)
        self.probe_button.pack(side = tkinter.LEFT)

        self.mv_button = tkinter.Button(master, text="Multiview tile", command=self.start_mv)
        self.mv_button.pack(side = tkinter.LEFT)
        
        self.vscope_button = tkinter.Button(master, text="Video Vectorscope", command=self.start_vscope)
        self.vscope_button.pack(side = tkinter.LEFT)
        
        self.vwave_button = tkinter.Button(master, text="Video Waveform (parade)", command=self.start_vwave)
        self.vwave_button.pack(side = tkinter.LEFT)
        
        self.mv_button = tkinter.Button(master, text="Audio Vectorscope", command=self.start_ascope)
        self.mv_button.pack(side = tkinter.LEFT)
        
        self.mv_button = tkinter.Button(master, text="Audio Spectrum", command=self.start_aspec)
        self.mv_button.pack(side = tkinter.LEFT)
        
        self.mv_button = tkinter.Button(master, text="Audio Loudness", command=self.start_loudness)
        self.mv_button.pack(side = tkinter.LEFT)

    def start_mv(self):
        ffmpeg.MVTile(self.stream_input.get())
        
    def start_play(self):
        
        ffmpeg.Ffplay(self.stream_input.get())
        
    def start_probe(self):
        
        root = tkinter.Toplevel(self.master)
        
        root.geometry("626x340")
        
        ffprobe_window = gui.ffprobe.Ffprobe_Window(root)
        
        ffmpeg.Ffprobe(self.stream_input.get(), ffprobe_window)
        
    def start_vscope(self):
        
        ffmpeg.video.Vector(self.stream_input.get())
    
    def start_vwave(self):
        
        ffmpeg.video.Wave(self.stream_input.get())
    
    def start_ascope(self):
        
        ffmpeg.audio.Vector(self.stream_input.get())
        
    def start_aspec(self):
        
        ffmpeg.audio.Spectrum(self.stream_input.get())
        
    def start_loudness(self):
        
        ffmpeg.audio.Loudness(self.stream_input.get())