from Tkinter import *
from ttk import *
import tkFileDialog
import os
from PIL import ImageTk
from Thumbnailer import *
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
        try:
            self.openedfile = tkFileDialog.askopenfile(parent=self.fileopener, mode='rb', title="Choose a file",filetypes=[ ("Standard formats","*.avi *.mp4 *.flv"),("Open domain formats"," *.webm, *.mkv")])
            if self.openedfile is not None:
                data = self.openedfile.read()
                self.openedfile.close()
            self.fileopener.destroy()
            fp = open('Workspace/video.mp4', 'wb')
            fp.write(data)
            fp.close()
        except Exception as e:
            pass
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
        self.openedcutlist = tkFileDialog.askopenfile(parent=self.cutlist, mode='rb', title="Choose a file", filetypes=[("Cut files", "*.txt, *.conf, *.ctl")])
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
    # This function displays the thumbnails and provides links to them. There is
    # a huge chance that this might not works

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

    # Now we need a function that pops up and shows the entire list of files

    def popupwindow(self, filepath):
        typeofsound = filepath.split("/")[2]
        self.frame1 = Toplevel()
        self.pop1 = Frame(self.frame1)
        self.frame1.title(typeofsound)
        self.canvas = Canvas(self.frame1, borderwidth=0)
        self.pop2 = Frame(self.canvas)
        self.sclbr = Scrollbar(self.frame1, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.sclbr.set)
        self.sclbr.pack(side="right", fill="y")
        self.canvas.pack(side="left", expand=True)
        self.canvas.create_window((4, 4), window=self.pop2, tags="self.frame")
        self.pop2.bind("<Configure>", self.OnFrameConfigure)

        if typeofsound == "MUSIC":
            mxlmt = self.msclmt
            filelist = self.msclist
        elif typeofsound == "SPEECH":
            mxlmt = self.spchlmt
            filelist = self.spchlist
        elif typeofsound == "SILENCE":
            mxlmt = self.slnclmt
            filelist = self.slnclist
        elif typeofsound == "SPEECHWMUSIC":
            mxlmt = self.spmslmt
            filelist = self.spmslist
        elif typeofsound == "SPEECHWNOISE":
            mxlmt = self.spnslmt
            filelist = self.spnslist

        print filelist

        for i in range(0, mxlmt):
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/" + typeofsound + "image" + str(i) + ".png")
            Button(self.pop2, text=filelist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "MUSIC"),image=self.igm, compound=BOTTOM).grid(row = i , column=0, padx=45, pady=4)

    def OnFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    # Function for displaying the results that are cut.

    def showresults(self):
        # Note that the following part is required only if you have done the
        # cutting. Comment it or uncomment it accordingly. They are intended to
        # save the time of thumnail generation of  the video.
        # thumbnailer()
        # os.system("ls Workspace/MUSIC/ > list.txt")
        # fp = open('list.txt')
        # self.msclist = fp.readlines()
        # fp.close()
        # self.msclmt = len(self.msclist)
        # fp.close()

        self.msclist = os.listdir(os.curdir + "/Workspace/MUSIC/")
        for line in self.msclist:
            if ".mp4" not in line:
                self.msclist.remove(line)
        self.msclist.sort()
        self.msclmt = len(self.msclist)

        self.spchlist = os.listdir(os.curdir + "/Workspace/SPEECH/")
        for line in self.spchlist:
            if ".mp4" not in line:
                self.spchlist.remove(line)
        self.spchlist.sort()
        self.spchlmt = len(self.spchlist)

        self.slnclist = os.listdir(os.curdir + "/Workspace/SILENCE/")
        for line in self.slnclist:
            if ".mp4" not in line:
                self.slnclist.remove(line)
        self.slnclist.sort()
        self.slnclmt = len(self.slnclist)

        self.spmslist = os.listdir(os.curdir + "/Workspace/SPEECHWMUSIC/")
        for line in self.spmslist:
            if ".mp4" not in line:
                self.spmslist.remove(line)
        self.spmslist.sort()
        self.spmslmt = len(self.spmslist)


        self.spnslist = os.listdir(os.curdir + "/Workspace/SPEECHWNOISE/")
        for line in self.spnslist:
            if ".mp4" not in line:
                self.spnslist.remove(line)
        self.spnslist.sort()
        self.spnslmt = len(self.spnslist)
         # self.attrib.pack(fill = BOTH)
        for i in range(0, self.msclmt):
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/" + "MUSIC" + "image" + str(i) + ".png")
            attrib = "tab1mainbuttontab"+str(i)
            # This part is pretty specific I will change it soon.
            # We will go with a 3*3 grid.
            j = 0
            if i <= 2:
                j = 0
            elif i > 2 and i <= 5:
                j = 1
            elif i > 5 and i < 9:
                j = 2
            Button(self.tab1, text=self.msclist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "MUSIC"),image=self.igm, compound=BOTTOM).grid(row=i%3, column=j, padx=67,pady=5)
            if i >= 9:
                Button(self.tab1, text="More...", command = lambda filepath = os.curdir + "/Workspace/MUSIC" : self.popupwindow(filepath)).grid(row=4, column=1)
        for i in range(0, self.spchlmt):
            j = 0
            if i <= 2:
                j = 0
            elif i > 2 and i <= 5:
                j = 1
            elif i > 5 and i < 9:
                j = 2
            self.igm = ImageTk.PhotoImage(file="Workspace/lists/" + "SPEECH" + "image" + str(i) + ".png")
            attrib = "tab2mainbuttontab" + str(i)
            Button(self.tab2, text=self.spchlist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SPEECH"),image=self.igm, compound=BOTTOM).grid(row=j, column=i%3, padx=67, pady=5)
            if i >= 9:
                Button(self.tab2, text="Previous").grid(row=4, column=0)
                Button(self.tab2, text="Next").grid(row=4, column=2)

        for i in range(0, self.slnclmt):
            j = 0
            if i <= 2:
                j = 0
            elif i > 2 and i <= 5:
                j = 1
            elif i > 5 and i < 9:
                j = 2

            self.igm = ImageTk.PhotoImage(file="Workspace/lists/"+"SILENCE"+"image"+str(i)+".png")
            attrib = "tab3mainbuttontab" + str(i)
            Button(self.tab3, text=self.slnclist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SILENCE"),image=self.igm, compound=BOTTOM).grid(row=j, column=i%3, padx=67, pady=5)
            #self.attrib.pack(fill=BOTH)
        for i in range(0, self.spmslmt):
            j = 0
            if i <= 2:
                j = 0
            elif i > 2 and i <= 5:
                j = 1
            elif i > 5 and i < 9:
                j = 2

            self.igm = ImageTk.PhotoImage(file="Workspace/lists/"+"SPEECHWMUSIC"+"image"+str(i)+".png")
            attrib = "tab4mainbuttontab" + str(i)
            Button(self.tab4, text=self.spmslist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SPEECHWMUSIC"),image=self.igm, compound=BOTTOM).grid(row=j, column=i%3, padx=67, pady=5)
            #self.attrib.pack(fill=BOTH)
        for i in range(0, self.spnslmt):
            j = 0
            if i <= 2:
                j = 0
            elif i > 2 and i <= 5:
                j = 1
            elif i > 5 and i < 9:
                j = 2

            self.igm = ImageTk.PhotoImage(file="Workspace/lists/" + "SPEECHWNOISE" + "image" + str(i) + ".png")
            attrib = "tab5mainbuttontab" + str(i)
            Button(self.tab5, text=self.spnslist[i], command=lambda i=i, image=self.igm: self.playvideo(i, "SPEECHWNOISE"),image=self.igm, compound=BOTTOM).grid(row=j, column=i%3, padx=67, pady=5)
            # self.attrib.pack(fill=BOTH)

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
