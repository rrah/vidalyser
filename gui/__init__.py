"""Gui elements for Vidalyser

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
import ffmpeg.audio
import ffmpeg.video

import tkinter
import tkinter.filedialog

import gui.ffprobe

import netifaces

import files


def get_addrs():
    
    """Get the IP addresses for this system."""
    
    for interface in netifaces.interfaces():
        
        try:
            addresses = netifaces.ifaddresses(interface)[netifaces.AF_INET]
        except KeyError:
            continue
        for address in addresses:
            yield address['addr']


class Launch_bar(tkinter.Frame):
    
    """Class to hold the text input and buttons for launching various tools."""
    
    def __init__(self, master, stream_url = None, loc_ip = None):
        
        """Construct the launch bar.
        
        Arguments:
            master - The TK master for the launch bar.
        """
        
        super().__init__(master)
        
        self.master = master
        
        input_frame = tkinter.Frame(self.master)
        
        self.stream_input = tkinter.Entry(input_frame)
        self.stream_input.pack(fill = tkinter.X, expand = 1, side = tkinter.LEFT)
        self.stream_input.insert(0, stream_url if stream_url else "udp://239.1.1.1:5000")
        
        addr_frame = tkinter.Frame(input_frame)
        
        addr_label = tkinter.Label(addr_frame, text = "Local address:")
        addr_label.pack(side = tkinter.LEFT)
        
        self.ip_addr = tkinter.StringVar()
        self.ip_select = tkinter.OptionMenu(addr_frame, self.ip_addr, *get_addrs())
        self.ip_addr.set(loc_ip if loc_ip else next(get_addrs()))
        self.ip_select.pack(fill = tkinter.X, expand = 1, side = tkinter.RIGHT)
        
        addr_frame.pack(fill = tkinter.X, expand = 1)
        
        input_frame.pack(fill = tkinter.X, expand = 1)
        
        button_frame = tkinter.Frame(self.master)
        
        self.play_button = tkinter.Button(button_frame, text="Play original", command=self.start_play)
        self.play_button.pack(side = tkinter.LEFT)
        
        self.probe_button = tkinter.Button(button_frame, text="Probe", command=self.start_probe)
        self.probe_button.pack(side = tkinter.LEFT)

        self.mv_button = tkinter.Button(master, text="Multiview tile", command=self.start_mv)
        self.mv_button.pack(side = tkinter.LEFT)
        
        self.vscope_button = tkinter.Button(button_frame, text="Video Vectorscope", command=self.start_vscope)
        self.vscope_button.pack(side = tkinter.LEFT)
        
        self.vwave_button = tkinter.Button(button_frame, text="Video Waveform (parade)", command=self.start_vwave)
        self.vwave_button.pack(side = tkinter.LEFT)
        
        self.mv_button = tkinter.Button(button_frame, text="Audio Vectorscope", command=self.start_ascope)
        self.mv_button.pack(side = tkinter.LEFT)
        
        self.mv_button = tkinter.Button(button_frame, text="Audio Spectrum", command=self.start_aspec)
        self.mv_button.pack(side = tkinter.LEFT)
        
        self.mv_button = tkinter.Button(button_frame, text="Audio Loudness", command=self.start_loudness)
        self.mv_button.pack(side = tkinter.LEFT)
        
        button_frame.pack()
        
    def get_stream_source(self):
        
        """Pull the entered stream info out of the gui."""
        
        input_string = self.stream_input.get()
        
        if input_string[0:6] == "udp://":
            input_string += "?localaddr={}".format(self.ip_addr.get())
            
        return input_string
    
    
    def start_mv(self):
        
        """Start a Multiview style tile."""
        
        ffmpeg.MVTile(self.get_stream_source())
    
        
    def start_play(self):
        
        """Launch FFplay to display the stream as is."""
        
        ffmpeg.Ffplay(self.get_stream_source())
    
        
    def start_probe(self):
        
        """Launch a new window with FFprobe info."""
        
        root = tkinter.Toplevel(self.master)
        
        root.geometry("626x340")
        
        ffprobe_window = gui.ffprobe.Ffprobe_Window(root)
        
        ffmpeg.Ffprobe(self.get_stream_source(), ffprobe_window)
    
        
    def start_vscope(self):
        
        """Start a video vectorscope tile."""
        
        ffmpeg.video.Vector(self.get_stream_source())
    
    
    def start_vwave(self):
        
        """Start a video waveform tile."""
        
        ffmpeg.video.Wave(self.get_stream_source())
    
    
    def start_ascope(self):
        
        """Start an audio phase vectorscope tile."""
        
        ffmpeg.audio.Vector(self.get_stream_source())
    
        
    def start_aspec(self):
        
        """Start an audio spectrum tile."""
        
        ffmpeg.audio.Spectrum(self.get_stream_source())
    
        
    def start_loudness(self):
        
        """Start an audio loudness meter tile."""
        
        ffmpeg.audio.Loudness(self.get_stream_source())
        
    def save_dict(self):
        
        """Return the dictionary of stream_url and loc_ip."""
        
        return {"url": self.stream_input.get(), "loc_ip": self.ip_addr.get()}
    
        
class Main_Window():
    
    """Main window to hold everything in."""
    
    def __init__(self):
    
        """Construct and launch the main window."""
        
        self._launch_bars = []
        
        self.root = tkinter.Tk()
        
        self.root.title("Vidalyser")
    
        frame = tkinter.LabelFrame(self.root)
        frame.pack()
        add_button = tkinter.Button(frame, text = "Add stream", command = self.add_stream)
        add_button.pack()
        
        menubar = tkinter.Menu(self.root)
        
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open)
        filemenu.add_command(label="Save as", command=self.save)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        
        menubar.add_cascade(label="File", menu=filemenu)
        
        helpmenu = tkinter.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.about)
        
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        self.root.config(menu=menubar)
    
    def save(self):
        
        filename = tkinter.filedialog.asksaveasfilename(defaultextension = ".json", filetypes = [("JSON files", ".json"), ("All files", ".*")])
        
        files.save_file(filename, self)
    
    def open(self):
        
        filename = tkinter.filedialog.askopenfilename(defaultextension = ".json", filetypes = [("JSON files", ".json"), ("All files", ".*")])

        files.load_file(filename, self)
    
    def about(self):
        
        pass
    
    def add_stream(self, stream_url = None, loc_ip = None):
        
        """Add an instance of Launch_Bar into this window."""
    
        frame = tkinter.LabelFrame(self.root)
        frame.pack()
        launch_bar = gui.Launch_bar(frame, stream_url, loc_ip)
        
        self._launch_bars.append(launch_bar)
    
    
    def launch_bars(self):
        
        """Return the current launch bars."""
        
        return self._launch_bars
        
    def mainloop(self):
        
        """Make the things go."""
        
        self.root.mainloop()
