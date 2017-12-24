# vidalyser [![Build Status](https://ci.rrah.me/buildStatus/icon?job=vidalyser)](https://ci.rrah.me/job/vidalyser)
GUI to launch various ffmpeg commands to analyse RTMP/UDP streams. 

## Requirements
* Python3.5 or greater
* Netifaces module `python -m pip install netifaces`
* ffmpeg/ffplay/ffprobe in path, or copy into same directory as __main__.py

## Usage

* Run __main__.py (`python __main__.py`)
* A window will open, click on add stream to add a launch bar.
* Enter a stream URL, and chose which network interface to use (if using UDP multicast).
* Click on the tiles you want to view. 

The combination of launch bars (along with their url's) can be saved, by going to `File->Save as`. Equally, a previously saved set of launch bars can be opened, by going to `File->Open`.

## Tiles

### Multiview
Window with the video, and stereo audio bars to the right.

### Original
FFplay, with no processing on the stream - it's displayed completely as is.

### Probe
FFprobe output, currently experimental.

### Video Vectorscope
As per the [FFmpeg vectorscope filter](https://ffmpeg.org/ffmpeg-filters.html#vectorscope) 

### Video Waveform
Also known as YUV parade.
As per the [FFmpeg waveform filter](https://ffmpeg.org/ffmpeg-filters.html#waveform)

### Audio Vectorscope
Audio phase vectorscope, as per [FFmpeg avectorscope filter](https://ffmpeg.org/ffmpeg-filters.html#avectorscope)

### Audio Spectrum
Audio spectrum display, as per [FFmpeg showspectrum filter](https://ffmpeg.org/ffmpeg-filters.html#showspectrum)

### Audio Loudness
Audio loudness (EBU R128) as per [FFmpeg ebur128 filter](https://ffmpeg.org/ffmpeg-filters.html#ebur128)
