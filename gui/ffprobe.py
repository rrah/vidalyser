'''
Created on 8 Apr 2017

@author: redsw
'''

import tkinter

class Ffprobe_Window():
    
    def __init__(self, master):
        
        self.master = master
        
        self.v = tkinter.StringVar()
        self.v.set("Loading...")
        self.frame = tkinter.Frame(self.master)
        self.label = tkinter.Label(self.master, textvariable = self.v, wraplength = 600, anchor=tkinter.W, justify=tkinter.LEFT)
        self.label.pack(expand = 1, fill =tkinter.BOTH)
        self.frame.pack(expand = 1, fill =tkinter.BOTH)
        
    def set(self, value):
        
        self.v.set(value)