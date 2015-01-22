from Tkinter import *
from ttk import *
import tkFileDialog
import os
from PIL import ImageTk

class MyApp:
    def __init__(self, parent):

        # Main window consisting of two panes
        self.panemajor = PanedWindow(parent, orient=HORIZONTAL)
        self.menubar = Menu(parent)
        # Adding file menu
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Create", command=self.workspace)
        self.filemenu.add_command(label="Open Video/Audio", command=self.fileopen)
        self.filemenu.add_command(label="Open cut list", command=self.filecutlist)
        self.filemenu.add_command(label="Save", command=self.save)
        self.filemenu.add_command(label="Extract audio", command=self.fileaudioextract)
        self.filemenu.add_command(label="Cut Video", command=self.showresults)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=parent.quit())
        # Adding Edit menu
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Find")
        self.editmenu.add_command(label="Cut")
        self.editmenu.add_command(label="Paste")
        # Adding Help Menu
        self.message = "This is a GUI Wrapper written in Tkinter\n for a Python module with \nScipy, Numpy and Matlplotlib as main components of programme."
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help")
        self.helpmenu.add_command(label="About", command=self.about)
        # Adding this to the menu bar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        # Adding the menu bar to parent
        parent.config(menu=self.menubar)
        # Adding two panes
        self.framemajor1 = Labelframe(self.panemajor, text="Pane1")
        self.framemajor2 = Labelframe(self.panemajor, text="Pane2")
        # Adding the five tabs
        self.tab = Notebook(self.framemajor2)
        self.tab1 = Frame(self.tab)
        self.tab2 = Frame(self.tab)
        self.tab3 = Frame(self.tab)
        self.tab4 = Frame(self.tab)
        self.tab5 = Frame(self.tab)
        # Adding button configurations
        Style().configure("TButton", padding=10, relief="flat", background="#444")
        self.sidebutton1 = Button(self.framemajor1, text="Click me!", command=lambda: self.callback(3))
        self.sidebutton1.pack(fill=BOTH, expand=1)
        self.tab.add(self.tab1, text="MUSIC")
        self.tab.add(self.tab2, text="SPEECH")
        self.tab.add(self.tab3, text="SILENCE")
        self.tab.add(self.tab4, text="SPEECH WITH MUSIC BACKGROUND")
        self.tab.add(self.tab5, text="SPEECH WITH NOISE BACKGROUND")
        self.tab.pack(fill=BOTH, expand=1)
        # Adding these tabs to panes
        self.panemajor.add(self.framemajor1)
        self.panemajor.add(self.framemajor2)
        self.panemajor.pack(fill=BOTH, expand=1)
    # Function for displaying 'About' message

    def about(self):
        self.top = Toplevel()
        self.top.title("About")
        Label(self.top, text=self.message).pack()
        self.aboutbutton1 = Button(self.top, text="Close")
        self.aboutbutton1.pack()
        print "hello"
    # Function for opening the file.

    def fileopen(self):
        self.fileopener = Toplevel()
        self.openingmsg = "Opening file......"
        self.fileopener.title("Opening File")
        Label(self.fileopener, text=self.openingmsg).pack()
        self.openedfile = tkFileDialog.askopenfile(parent=self.fileopener, mode='rb', title="Choose a file")
        if self.openedfile is not None:
            data = self.openedfile.read()
            self.openedfile.close()
        self.fileopener.destroy()
        fp = open('Workspace/video.mp4', 'wb')
        fp.write(data)
        fp.close()
    # Function for saving the file.

    def save(self):
        self.formats = [('video', '.mp4'), ('music', '.mp3'), ('video2', '.avi')]
        self.filesaver = Toplevel()
        self.savedfile = tkFileDialog.asksaveasfilename(parent=self.filesaver, filetypes=self.formats, title="Save the image as...")
        self.filesaver.destroy()
        if len(self.savedfile) > 0:
            print "File is saved under"
            print nomFichier
    # Functions for making the workspace directory

    def workspace(self):
        os.system("mkdir Workspace")

    # For generating a cutlist file from a normal conf file
    def filecutlist(self):
        self.cutlist = Toplevel()
        self.cutlistmsg = "Opening cut list......"
        self.cutlist.title("Opening File")
        Label(self.cutlist, text=self.cutlistmsg).pack()
        self.openedcutlist = tkFileDialog.askopenfile(parent=self.cutlist, mode='rb', title="Choose a file")
        if self.openedcutlist is not None:
            data = self.openedcutlist.read()
            self.openedcutlist.close()
        self.cutlist.destroy()
        fp = open("Workspace/cutlist.ctlst", 'wb')
        fp.write(data)
        print "Cutlist written to workspace"

    # For extracting audio from the Video file
    def fileaudioextract(self):
        self.extractor = Toplevel()
        self.extractormsg = "Extracting mp3 from video......"
        self.extractor.title("Extracting audio layer")
        Label(self.extractor, text=self.extractormsg).pack()
        os.system("ffmpeg -i Workspace/video.mp4 -ab 320k -ac 2 -ar 44100 -vn Workspace/audio.mp3")
        print "Audio Layer successfully extracted"
        self.extractor.destroy()

    # For cutting the video
    # Warning this might take a long time.
    def filevideocutter(self):
        self.cutter = Toplevel()
        self.cuttermsg = "Cutting the audio..."
        self.cutter.title("Segmenting the video")
        self.msclist = []
        self.msclmt = 0
        self.spchlist = []
        self.spchlmt = 0
        self.slnclist = []
        self.slnclmt = 0
        self.spmslist = []
        self.spmslmt = 0
        self.spnslist = []
        self.spnslmt = 0
        Label(self.cutter, text=self.cuttermsg).pack()
        fp = open('Workspace/cutlist.ctlst', 'rb')
        firstline = fp.readline()
        for i in range(0, 5):
            secondline = fp.readline()
            cmd1 = "mkdir Workspace/" + secondline.split('#')[1]
            print cmd1
            os.system(cmd1)
            limit = int(secondline.split('#')[2])
            print limit
            for i in range(0, limit):
                init1 = fp.readline()
                init2 = init1.split('-')[1]
                init1 = init1.split('-')[0]
                init2 = init2.split('\n')[0]
                cmd2 = "ffmpeg -i Workspace/video.mp4 -ss " + init1 + " -t " + init2 + " -async 1 " + "Workspace/"+secondline.split('#')[1]+"/"+init1 + "-" +init2 + ".mp4"
                print cmd2
                os.system(cmd2)
                if (secondline.split('#')[1] == 'MUSIC'):
                    self.msclist.append(init1+init2)
                    self.msclmt = self.msclmt + 1
                elif (secondline.split('#')[1] == 'SPEECH'):
                    self.spchlist.append(init1 + init2)
                    self.spchlmt = self.spchlmt + 1
                elif (secondline.split('#')[1] == 'SILENCE'):
                    self.slnclist.append(init1 + init2)
                    self.spchlmt = self.spchlmt + 1
                elif (secondline.split('#')[1] == 'SPEECHWMUSIC'):
                    self.spmslist.append(init1 + init2)
                    self.spmslmt = self.spmslmt + 1
                elif (secondline.split('#')[1] == 'SPEECHWNOISE'):
                    self.spnslist.append(init1 + init2)
                    self.spnlmt = self.spnslmt + 1
        self.showresults()

    # Function for displaying the results that are cut.
    def showresults(self):
        # Note that the following part is required only if you have done the
        # cutting. Comment it or uncomment it accordingly. They are intended to
        # save the time of cutting the video.
        os.system("ls Workspace/MUSIC/ > list.txt")
        fp = open('list.txt')
        self.msclist = fp.readlines()
        fp.close()
        self.msclmt = len(self.msclist)
        fp.close()

        os.system("ls Workspace/SPEECH/ > list.txt")
        fp = open('list.txt')
        self.spchlist = fp.readlines()
        fp.close()
        self.spchlmt = len(self.spchlist)
        fp.close()

        os.system("ls Workspace/SILENCE/ > list.txt")
        fp = open('list.txt')
        self.slnclist = fp.readlines()
        fp.close()
        self.slnclmt = len(self.slnclist)
        fp.close()

        os.system("ls Workspace/SPEECHWMUSIC/ > list.txt")
        fp = open('list.txt')
        self.spmslist = fp.readlines()
        fp.close()
        self.spmslmt = len(self.spmslist)
        fp.close()

        os.system("ls Workspace/SPEECHWNOISE/ > list.txt")
        fp = open('list.txt')
        self.spnslist = fp.readlines()
        fp.close()
        self.spnslmt = len(self.spnslist)

        for i in range(0, self.msclmt):
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/"+"MUSIC"+"image"+str(i)+".jpg")
            attrib = "tab1mainbuttontab"+str(i)
            Button(self.tab1, text=self.msclist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "MUSIC"),image=self.igm, compound=BOTTOM).pack()
            #self.attrib.pack(fill=BOTH)
        for i in range(0, self.spchlmt):
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/"+"SPEECH"+"image"+str(i)+".jpg")
            attrib = "tab2mainbuttontab" + str(i)
            Button(self.tab2, text=self.spchlist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SPEECH"),image=self.igm, compound=BOTTOM).pack()
        for i in range(0, self.slnclmt):
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/"+"SILENCE"+"image"+str(i)+".jpg")
            attrib = "tab3mainbuttontab" + str(i)
            Button(self.tab3, text=self.slnclist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SILENCE"),image=self.igm, compound=BOTTOM).pack()
            #self.attrib.pack(fill=BOTH)
        for i in range(0, self.spmslmt):
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/"+"SPEECHWMUSIC"+"image"+str(i)+".jpg")
            attrib = "tab4mainbuttontab" + str(i)
            Button(self.tab4, text=self.spmslist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SPEECHWMUSIC"),image=self.igm, compound=BOTTOM).pack()
            #self.attrib.pack(fill=BOTH)
        for i in range(0, self.spnslmt):
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/"+"SPEECHWNOISE"+"image"+str(i)+".jpg")
            attrib="tab5mainbuttontab" + str(i)
            Button(self.tab5, text=self.spnslist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SPEECHWNOISE"),image=self.igm, compound=BOTTOM).pack()
            #self.attrib.pack(fill=BOTH)

    # A dummy test function
    def callback(self, t):
        print "hello World", t

    # Function to play video can use vlc also
    def playvideo(self, i, string):
        # print i
        if string == "MUSIC":
            t = self.msclist
        elif string == "SPEECH":
            t = self.spchlist
        elif string == "SILENCE":
            t = self.slnclist
        elif string == "SPEECHWMUSIC":
            t = self.spmslist
        elif string == "SPEECHWNOISE":
            t = self.spnslist
        cmd1 = "mplayer Workspace/" + string + "/" + t[int(i)].split('\n')[0]
        print cmd1
        os.system(cmd1)
        print i, string

root = Tk()
myapp = MyApp(root)
root.mainloop()
