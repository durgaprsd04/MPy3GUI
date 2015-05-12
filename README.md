MPy3GUI
=======
## General Outlines
A simple program intended as a wrapper for some python code. Mostly done using
tkinter and using ttk class for a better appearance. Pretty bad part with the
coding. Improvements include

* Removing unwanted comments and comment on necessary stuff.
* Terminal displays made minimal and meaningful
* Adding listbox click-open functionality.
* Multithreading(optional might start a branch for it)
* Please wait message dialog boxes.

## Dependencies
Code demands several dependencies to be met.
* A working tkinter installation.
* ffmpeg
* VLC or mplayer according to the users choice. Mostly this will be dropped
and any suitable video player might be added.
* As of 12/5/2015 mplayer is not a  must. User have option to choose players
* Thumbnailer is done using ffmpegthumbnailer, standard application for this.

## User guide
The basic functionalities of the program include, reading a Video file,
extracting audio layer from it saving it under Workspace/audio.mp3 . Finding the positions of the audio cuts and
generating a cut list is done by matlab executable(not available here)  that contains the exact details and timings of
different sound classes, which program splits and puts in a folder named in
accordance to sound class it belongs to and shows a grid view of these.
### Things to do to get started
* Open a video file( which automatically gets saved to workspace and audio
  layer will be extracted.
* Select cut video option, it will do the rest and provide you with thumbnails.
