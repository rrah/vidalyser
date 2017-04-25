"""Vidalyser.

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