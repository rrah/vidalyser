'''
Created on 6 Apr 2017

@author: redsw
'''

import tkinter

import gui

root = tkinter.Tk()

root.title("Vidalyser")
frame1 = tkinter.LabelFrame(root)
frame1.pack()
bar1 = gui.Launch_bar(frame1)
frame2 = tkinter.LabelFrame(root)
frame2.pack()
bar2 = gui.Launch_bar(frame2)

root.mainloop()