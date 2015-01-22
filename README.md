MPy3GUI
=======
## General Outlines
A simple program intended as a wrapper for some python code. Mostly done using
tkinter and using ttk class for a better appearance. Pretty bad part with the
coding. Improvements include

* Splitting the code to several parts
* Adding warnings and implied actions.
* Adding keybindings.
* Making it efficient in terms of work done.
* Including a Scrollbar??

## Dependencies
Code demands several dependencies to be met.
* A working tkinter installation.
* ffmpeg
* VLC or mplayer according to the users choice. Mostly this will be dropped
and any suitable video player might be added.
* As of 22/1/2015 mplayer is a a must. It is the one which generates thumbnails
  and ImageMagick is the one which scales them.
* mencoder is used along with mplayer for thumbnail generation.
* Thumbnailer heavily depends on os utilities, need to be redone for any system
  other than linux based.

## User guide
The basic functionalities of the program include, reading a Video file,
extracting audio layer from it. Finding the positions of the audio cuts and
generating a configuration file that contains the exact details and timings of
different sound classes. The program up on request splits these into five
classes and shows a grid view of these. Users can save the file according to
need.
### Things to do to get started
* Users should create a Workspace Directory.
* Open a video and save it to the Workspace.
* Provide a configuration file.
* Segment the video file according to the configuration file provided.
* Most of this has to have some or another tweaking to be done to make it
  better. For the time being this is the story.
