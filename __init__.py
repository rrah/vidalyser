'''
Created on 6 Apr 2017

@author: redsw
'''

import ffmpeg
import ffmpeg.audio
import ffmpeg.video

from tkinter import Tk, Label, Button

class Launch_bar:
    def __init__(self, master):
        self.master = master
        master.title("Vidalyser")

        self.label = Label(master, text="Make selection below.")
        self.label.pack()
        
        self.play_button = Button(master, text="Play original", command=self.start_play)
        self.play_button.pack()

        self.mv_button = Button(master, text="Multiview tile", command=self.start_mv)
        self.mv_button.pack()
        
        self.mv_button = Button(master, text="Video Vectorscope", command=self.start_vscope)
        self.mv_button.pack()
        
        self.mv_button = Button(master, text="Video Waveform (parade)", command=self.start_vwave)
        self.mv_button.pack()
        
        self.mv_button = Button(master, text="Audio Vectorscope", command=self.start_ascope)
        self.mv_button.pack()
        
        self.mv_button = Button(master, text="Audio Spectrum", command=self.start_aspec)
        self.mv_button.pack()
        
        self.mv_button = Button(master, text="Audio Loudness", command=self.start_loudness)
        self.mv_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def start_mv(self):
        ffmpeg.MVTile(None)
        
    def start_play(self):
        
        ffmpeg.Ffplay(None)
        
    def start_vscope(self):
        
        ffmpeg.video.Vector(None)
    
    def start_vwave(self):
        
        ffmpeg.video.Wave(None)
    
    def start_ascope(self):
        
        ffmpeg.audio.Vector(None)
        
    def start_aspec(self):
        
        ffmpeg.audio.Spectrum(None)
        
    def start_loudness(self):
        
        ffmpeg.audio.Loudness(None)

root = Tk()
my_gui = Launch_bar(root)
root.mainloop()