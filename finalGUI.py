from Tkinter import  *
from ttk import *
import tkFileDialog
import os
import Asif_test as merger
from PIL import ImageTk
import thread

class MyFirstGUI:
    def __init__(self, master):
        self.crossref ={'1':'Silence','2':'Speech','3':'SpeechWithNoise','4':'Music','5':'SpeechWithMusic'}
        self.mcrpath = "/media/carcosa/b2934c03-21ea-4d8b-9f19-fda9f942c72b/usr/local/MATLAB/R2014a/"
        self.master = master
        self.p = Panedwindow(self.master, orient=HORIZONTAL)
        # first pane, which would get widgets gridded into it:
        self.f1 = Labelframe(self.p, text='Pane1', width=100, height=100)
        self.f2 = Labelframe(self.p, text='Pane2', width=100, height=100); # second pane
        self.p.add(self.f1)
        self.p.add(self.f2)
        self.p.pack(fill=BOTH, expand=1)
        self.scrollbar1 = Scrollbar(self.f1, orient=VERTICAL)
        self.listbox = Listbox(self.f1, yscrollcommand=self.scrollbar1.set)
        self.listbox.insert(END, "MUSIC")
        self.scrollbar1.config(command=self.listbox.yview)
        self.scrollbar1.pack(side=RIGHT, fill=BOTH, expand=1)
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        # Adding the Menu bar. This has got options for manipulation
        self.menubar = Menu(master)
        # Adding filemenu
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open Video/Audio", command=self.fileopen)
        self.filemenu.add_command(label="Extract audio", command=self.fileaudioextract)
        self.filemenu.add_command(label="Cut Video", command=self.thumbnailer)
        self.filemenu.add_command(label="Train", command = self.train)
        self.filemenu.add_command(label="Cut Audio", command=self.audiocutter)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=master.quit())
        # Adding Edit menu
        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="VLC")
        self.editmenu.add_command(label="MPLAYER")
        self.editmenu.add_command(label="SMplayer")
        # Adding Help Menu
        self.message = "This is a GUI Wrapper written in Tkinter\n for a Python module with \nScipy, Numpy and Matlplotlib as main components of programme."
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="Help")
        self.helpmenu.add_command(label="About", command=self.about)
        # Adding this to the menu bar
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.menubar.add_cascade(label="Select Player", menu=self.editmenu)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        # Adding the menu bar to parent
        master.config(menu=self.menubar)
        self.isvideo=False
        self.islist= False
        self.folderlist=[]
        self.Musiclist =[]
        self.Speechlist =[]
        self.Silencelist =[]
        self.SpeechWithMusiclist=[]
        self.SpeechWithNoiselist=[]



        #self.displaythumbnails()
        #self.pop1 = Frame(self.master)
        #self.pop1
    # This is called after cutting the video.
    def audiocutter(self):
        print './run_Audiocutter1.sh ' + self.mcrpath
        print "Audio cutting is being done. Please Wait..."
        #self.message = "Detection Audio Cuts"
        os.system('./run_Audiocutter1.sh '+ self.mcrpath)
        os.system('dos2unix Workspace/audiocut.txt')
        """
        try:
            thread.start_new_thread(self.notification, ("Detecting Audio cuts will take a long time. Please click below to proceed",))
        except Exception as e:
            print "unable to run threads"
        """
        print "Audiocut extraction done."


        #os.system('sed -e "s/^M//" Workspace/audiocut.txt  > Workspace/audiocut2.txt')
        #fp1 = open('Workspace/audiocut2.txt','r')
        #for lines in  fp.readlines():
            #fp1.write(lines)
        #fp1.close()
        #fp1 = open('Workspace/audiocut1.txt','r')
        fp = open('Workspace/audiocut.txt','r')
        #init1 = fp.readline()
        #init1 = init1.split('\n')[0]
        init1  ="00:00:00.000"
        init2= fp.readline()
        init2 = init2.split('\n')[0]
        flag =0
        if not(init1 == "0"+init2):
            os.system( "ffmpeg  -i  Workspace/audio.mp3 -ss "+  init1+ " -to "  + "0"+init2  + " -ab 256k -y Workspace/audiocuts/audiocut0.mp3")
            print 'dfdsfsdafd'
            print "ffmpeg  -i  Workspace/audio.mp3 -ss "+  init1+ " -to "  + "0"+init2  + " -ab 256k -y Workspace/audiocuts/audiocut0.mp3"
            flag = 1
        for j, string in enumerate(fp.readlines()):
            init1 = init2
            init2 = string.split('\n')[0]
            #print init1
            #init1 = init1.split('\n')[0]
            #init2 = init1.split('-')[1]
            #init1 = init1.split('-')[0]
            #print "ffmpeg -i Workspace/"+ self.openedfilename +" -ss " + init1 + " -t " + init2 + " -async 1 " + "Workspace/videocuts/"+self.filetype +"/"+init1 + "-" +init2 + "."+self.openedfilenametype
            #print init1, init2
            cmd =  "ffmpeg  -i  Workspace/audio.mp3  -ss " + "0"+ init1+ " -to "  + "0" +init2  + " -ab 256k -y Workspace/audiocuts/audiocut" + str(j+flag) + ".mp3"
            print cmd
            os.system( "ffmpeg  -i  Workspace/audio.mp3 -ss "+ "0"+ init1+ " -to "  + "0"+init2  + " -ab 256k -y Workspace/audiocuts/audiocut" + str(j+1) + ".mp3")
            init1 = init2
        # Now classification of audio part has to take place. This is done using
        # New_classifiier.
        os.system('ffmpeg -i Workspace/video.mp4 2>&1 | grep Duration > t.txt')
        print "######################################################"
        fp1 = open('t.txt', 'rb')
        string = fp1.readline()
        print string
        t = string.split(' ')
        init3 = t[3].split(',')[0]
        print init2,init3

        if not("0"+init2 == init3+"0"):
            print 'finasdfa'
            os.system( "ffmpeg  -i  Workspace/audio.mp3 -ss "+ "0"+ init2 + " -to "  +init3  + " -ab 256k -y Workspace/audiocuts/audiocut" + str(j+2) + ".mp3")
            print "ffmpeg  -i  Workspace/audio.mp3 -ss "+ "0"+ init2 + " -to "  +init3  + " -ab 256k -y Workspace/audiocuts/audiocut" + str(j+flag+1) + ".mp3"
        print "##################################################"+string

        print './run_NewClassifier.sh ' + self.mcrpath
        print " Classifying according to Audio,Please wait this takes time..."
        os.system('./run_NewClassifier.sh '+self.mcrpath)
        os.system('dos2unix Workspace/classified.txt')


        # After this a file named classified.txt must be there in the  Workspace
        print "Merging the small Audio cuts."
        merger.merge()
        # Video Cutting is done here.
        print 'Video cutting is done.......'
        fp = open('Workspace/merged.txt','rb')
        string = fp.readline()
        init1 = string.split('\n')[0]
        soundtype = init1.split('-')[2]
        init1 = init1.split('-')[0]
        for string in fp.readlines():
            """
            try:
                thread.start_new_thread(self.notification, ("Classifying the audio segments. This might take time.",))
            except Exception as e:
                print "Thread could not be executed"
            """
            os.system('mkdir Workspace/videocuts/' + self.crossref[soundtype[0]])
            print 'mkdir Workspace/videocuts/' + soundtype[0]

            #self.filetype=init1.split('#')[1]
            #self.folderlist.append(self.filetype)
            #init1 = init1.split('\n')[0]
            init2 = string.split('\n')[0]
            init2 = init2.split('-')[0]
            #init1 = init1.split('-')[0]
            print "ffmpeg -i Workspace/"+ self.openedfilename +" -ss " + "0"+init1 + " -t " +"0"+ init2 + " -async 1 " + "Workspace/videocuts/"+self.crossref[soundtype[0]] +"/"+ "0"+init1 + "-" +"0"+init2 + "."+self.openedfilenametype
            try:
                os.system( "ffmpeg -i Workspace/"+ self.openedfilename +" -strict -2 -ss " "0" + init1 + " -to " +"0"+ init2 + " -async 1 " + "Workspace/videocuts/"+self.crossref[soundtype[0]] +"/"+"0"+init1 + "-" +"0"+init2 + "."+self.openedfilenametype)
            except Exception as e:
                os.system( "ffmpeg -i Workspace/"+ self.openedfilename +" -strict -2 -ss " "0" + init1 + " -to " +"0"+ init2 + " -async 1 " + "Workspace/videocuts/"+self.crossref[soundtype[0]] +"/"+"0"+init1 + "-" +"0"+init2 + "."+self.openedfilenametype)
            init1 = init2
            soundtype = string.split('-')[2]
            soundtype = soundtype.split('\n')
            fp.close()
        self.thumbnailer()





    def train(self):
        #print "hello this is the training session"
        if os.path.isdir('training_data'):
            self.message = "Training data sets"
            self.notification()
            print " Loading classifier MATLAB Executable"
            print './run_Identify.sh' + self.mcrpath
            os.system('./run_Identify.sh ' + self.mcrpath)
            #print "hellosdfs"
            #if os.path.isdir('Datasets/Music') and os.path.isdir('Datasets/Speech') and os.path.isdir('Datasets/Silence') and os.path.isdir('Datasets/Speech_With_Music') and os.path.isdir('Datasets/Speech_With_Noise'):
                #print "Test"
            #else:
                #print "ERROR\n All the five folders needed for training is absent"
                #self.message = "Error not all five folders are there"
                #self.errorfunction()
        else:
            #print "ERROR\n No folder named Datasets"
            self.message = "No folder named datasets"
            self.errorfunction()

    def errorfunction(self):
        #self.message="sdfssdfs"
        self.top = Toplevel()
        self.toplevelframe = Frame(self.top, width=150, height=150)
        self.top.geometry('300x100')
        self.top.title("ERROR!")
        self.msg = Message(self.toplevelframe, text=self.message, background='red')
        self.msg.pack(expand=True, fill="both")
        self.button = Button(self.toplevelframe, text="Close", command=self.top.destroy)
        self.button.pack()
        print "hello world"

    def notification(self, string):
        #self.message="sdfssdfs"
        self.top = Toplevel()
        self.toplevelframe = Frame(self.top)
        self.top.geometry('200x150')
        self.top.title("Information")
        self.msg = Message(self.toplevelframe, text=string, background='lightgreen', font=('times', 12, 'bold'), justify=CENTER)
        self.msg.pack(expand=True, fill="both")
        self.button = Button(self.toplevelframe, text="Close", command=self.top.destroy)
        self.button.pack()
        self.toplevelframe.pack(expand=True, fill="both")
        #print "Audiocut extraction done."
        #self.top.destroy()

    """
    def executable(self, number):
        if number == 1:
            os.system('./run_Audiocutter1.sh '+ self.mcrpath)
            os.system('dos2unix Workspace/audiocut.txt')
            print "hell"
        elif number ==2:
            os.system('./run_NewClassifier.sh '+self.mcrpath)
            os.system('dos2unix Workspace/classified.txt')
            print "df"
    """







    def displaythumbnails(self):
        self.notebook =Notebook(self.f2)
        self.frame1 = Frame(self.notebook)
        self.frame2 = Frame(self.notebook)
        self.frame3 = Frame(self.notebook)
        self.frame4 = Frame(self.notebook)
        self.frame5 = Frame(self.notebook)
        Style().configure("TButton", padding=10, relief="flat", background="#464")


        self.canvas1 = Canvas(self.frame1, borderwidth=0)
        self.frame1child = Frame(self.canvas1)
        self.sclbr1 = Scrollbar(self.frame1, orient="vertical",  command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.sclbr1.set)
        self.sclbr1.pack(side="right", fill="both")
        self.canvas1.pack(side="left", expand=True, fill=BOTH)
        self.canvas1.create_window((4, 4), window=self.frame1child, tags="self.frame1child")
        self.frame1child.bind("<Configure>", self.OnFrameConfigure1)
        #self.igm = ImageTk.PhotoImage(file="test.png")
        #for string in self.folderlist:
        #    attrib = string+"list"
        string = self.folderlist[0]
        self.list1 = os.listdir('Workspace/videocuts/'+string)
        print self.list1
        #print self.Musiclist
        for i in range(0,len(self.list1)/3 + 1):
            for j in range(0,3):
                #print "*"
                k = (i)*3 + j
                if k < len(self.list1):
                    #print "Workspace/Thumbnails/Music/"+self.list1[k]+".png"
                    self.igm = ImageTk.PhotoImage(file="Workspace/Thumbnails/Music/"+self.list1[k]+".png")
                    Button(self.frame1child, text=self.list1[k], command=lambda k=k, image=self.igm:self.playvideo(k, "Music"), image=self.igm, compound=BOTTOM).grid(row = i , column=j, padx=45, pady=4)
        self.canvas2 = Canvas(self.frame2, borderwidth=0)
        self.frame2child = Frame(self.canvas2)
        self.sclbr2 = Scrollbar(self.frame2, orient="vertical",  command=self.canvas2.yview)
        self.canvas2.configure(yscrollcommand=self.sclbr2.set)
        self.sclbr2.pack(side="right", fill="both")
        self.canvas2.pack(side="left", expand=True, fill=BOTH)
        self.canvas2.create_window((4, 4), window=self.frame2child, tags="self.frame2child")
        self.frame2child.bind("<Configure>", self.OnFrameConfigure2)
        #self.igm = ImageTk.PhotoImage(file="test.png")
        string = self.folderlist[1]
        self.list2 = os.listdir('Workspace/videocuts/'+ string)
        for i in range(0,len(self.list2)/3 + 1):
            for j in range(0,3):
                k = i*3 + j
                if k < len(self.list2):
                    self.igm = ImageTk.PhotoImage(file="Workspace/Thumbnails/Speech/" + self.list2[k]+".png")
                    Button(self.frame2child, text=self.list2[k],command=lambda k=k, image=self.igm:self.playvideo(k, "Speech"),  image=self.igm, compound=BOTTOM).grid(row = i , column=j, padx=45, pady=4)
        self.canvas3 = Canvas(self.frame3, borderwidth=0)
        self.frame3child = Frame(self.canvas3)
        self.sclbr3 = Scrollbar(self.frame3, orient="vertical",  command=self.canvas3.yview)
        self.canvas3.configure(yscrollcommand=self.sclbr3.set)
        self.sclbr3.pack(side="right", fill="both")
        self.canvas3.pack(side="left", expand=True, fill=BOTH)
        self.canvas3.create_window((4, 4), window=self.frame3child, tags="self.frame3child")
        self.frame3child.bind("<Configure>", self.OnFrameConfigure3)
        #self.igm = ImageTk.PhotoImage(file="test.png")
        string = self.folderlist[2]
        self.list3 = os.listdir('Workspace/videocuts/'+string)
        for i in range(0, len(self.list3)/3 + 1):
            for j in range(0,3):
                k = i*3 + j
                if k < len(self.list3):
                    self.igm = ImageTk.PhotoImage(file="Workspace/Thumbnails/Silence/"+self.list3[k]+".png")
                    Button(self.frame3child, text=self.list3[k],   command=lambda k=k, image=self.igm:self.playvideo(k, "Silence"), image=self.igm, compound=BOTTOM).grid(row = i , column=j, padx=45, pady=4)
        self.canvas4 = Canvas(self.frame4, borderwidth=0)
        self.frame4child = Frame(self.canvas4)
        self.sclbr4 = Scrollbar(self.frame4, orient="vertical",  command=self.canvas4.yview)
        self.canvas4.configure(yscrollcommand=self.sclbr4.set)
        self.sclbr4.pack(side="right", fill="both")
        self.canvas4.pack(side="left", expand=True, fill=BOTH)
        self.canvas4.create_window((4, 4), window=self.frame4child, tags="self.frame4child")
        self.frame4child.bind("<Configure>", self.OnFrameConfigure4)
        string = self.folderlist[3]
        self.list4 = os.listdir('Workspace/videocuts/' + string)
        #self.igm = ImageTk.PhotoImage(file="test.png")
        for i in range(0, len(self.list4) + 1):
            for j in range(0,3):
                k = i*3 + j
                if k < len(self.list4):
                    self.igm = ImageTk.PhotoImage(file="Workspace/Thumbnails/SpeechWithMusic/"+self.list4[k]+".png")
                    Button(self.frame4child, text=self.list4[k],  command=lambda k=k, image=self.igm:self.playvideo(k, "SpeechWithMusic"),image=self.igm, compound=BOTTOM).grid(row = i , column=j, padx=45, pady=4)
        self.canvas5 = Canvas(self.frame5, borderwidth=0)
        self.frame5child = Frame(self.canvas5)
        self.sclbr5 = Scrollbar(self.frame5, orient="vertical",  command=self.canvas5.yview)
        self.canvas5.configure(yscrollcommand=self.sclbr5.set)
        self.sclbr5.pack(side="right", fill="both")
        self.canvas5.pack(side="left", expand=True, fill=BOTH)
        self.canvas5.create_window((4, 4), window=self.frame5child, tags="self.frame5child")
        self.frame5child.bind("<Configure>", self.OnFrameConfigure5)
        #self.igm = ImageTk.PhotoImage(file="test.png")
        string = self.folderlist[4]
        self.list5 = os.listdir('Workspace/videocuts/'+string)
        for i in range(0, len(self.list5)):
            for j in range(0,3):
                k =3*i + j
                if k < len(self.list5):
                    self.igm = ImageTk.PhotoImage(file="Workspace/Thumbnails/SpeechWithNoise/"+self.list5[k]+".png")
                    Button(self.frame5child, text=self.list5[k],  command=lambda k=k, image=self.igm:self.playvideo(k, "SpeechWithNoise"), image=self.igm, compound=BOTTOM).grid(row = i , column=j, padx=45, pady=4)
        self.notebook.add(self.frame1, text="Music")
        self.notebook.add(self.frame2, text="Speech")
        self.notebook.add(self.frame3, text="Silence")
        self.notebook.add(self.frame4, text="Speech With Music")
        self.notebook.add(self.frame5, text="Speech With Noise")
        self.notebook.pack(fill=BOTH)
        self.listboxconfiguration()

    def OnFrameConfigure1(self, event):
        self.canvas1.configure(scrollregion=self.canvas1.bbox("all"), width = event.width, height=event.height)

    def OnFrameConfigure2(self, event):
        self.canvas2.configure(scrollregion=self.canvas2.bbox("all"), width = event.width, height=event.height)

    def OnFrameConfigure3(self, event):
        self.canvas3.configure(scrollregion=self.canvas3.bbox("all"), width = event.width, height=event.height)

    def OnFrameConfigure4(self, event):
        self.canvas4.configure(scrollregion=self.canvas4.bbox("all"), width = event.width, height=event.height)

    def OnFrameConfigure5(self, event):
        self.canvas5.configure(scrollregion=self.canvas5.bbox("all"), width = event.width, height=event.height)

    def listboxconfiguration(self):
        t=0
        string =["Music", "Speech","Silence", "Speech With Music", "Speech With Noise"]
        self.listbox.itemconfig(t,{'bg':'cyan'})
        for i in range(0,len(self.list1)):
            self.listbox.insert(END,self.list1[i])
        self.listbox.insert(END,string[1])
        t = t+ len(self.list1)+1
        self.listbox.itemconfig(t,{'bg':'blue'})
        for i in range(0,len(self.list2)):
            self.listbox.insert(END,self.list2[i])
        self.listbox.insert(END,string[2])
        t = t+ len(self.list2)+1
        self.listbox.itemconfig(t,{'bg':'green'})
        for i in range(0,len(self.list3)):
            self.listbox.insert(END,self.list3[i])
        self.listbox.insert(END,string[3])
        t = t+ len(self.list3)+1
        self.listbox.itemconfig(t,{'bg':'red'})
        for i in range(0,len(self.list4)):
            self.listbox.insert(END,self.list4[i])
        self.listbox.insert(END,string[4])
        t = t+ len(self.list4)+1
        self.listbox.itemconfig(t,{'bg':'yellow'})
        for i in range(0,len(self.list5)):
            self.listbox.insert(END,self.list5[i])

        #print "The command was issued from  " + str(i) + " with string as " + string
        #os.system("feh Workspace/Thumbnails/"+string+"/"+str(i)+".png")

    def playvideo(self, i, string):
        if string == "Music":
            t = self.list1
        elif string == "Speech":
            t = self.list2
        elif string == "Silence":
            t = self.list3
        elif string == "SpeechWithMusic":
            t = self.list4
        elif string == "SpeechWithNoise":
            t = self.list5
        cmd1 = "vlc Workspace/videocuts/" + string + "/" + t[i]
        print cmd1
        os.system(cmd1)
        print i, string
    def workspace(self ):
        print "This function creates a Workspace folder in the directory."
        os.sytem("mkdir Workspace")
    def fileopen(self ):
        os.system('rm -rvf Workspace/audiocuts/*')
        os.system('rm  -rvf Workspace/videocuts/*')

        self.fileopener = Toplevel()
        self.openingmsg = "Opening Video......"
        self.fileopener.title("Opening File")
        Label(self.fileopener, text=self.openingmsg).pack()
        try:
            self.openedfile = tkFileDialog.askopenfile(parent=self.fileopener, mode='rb', title="Choose a file",filetypes=[ ("Standard formats","*.avi *.mp4 *.flv"),("Open domain formats"," *.webm, *.mkv")])
            self.openedfilename = self.openedfile.name
            print self.openedfilename.split('.')[-1:][0]
            #self.typeofvideo = self.openedfilename.split('.')[-1:]
            if self.openedfile is not None:
                data = self.openedfile.read()
                self.openedfile.close()
            self.fileopener.destroy()
            fp = open('Workspace/video.'+self.openedfilename.split('.')[-1:][0], 'wb')
            self.openedfilename = 'video.'+self.openedfilename.split('.')[-1:][0]
            self.openedfilenametype =self.openedfilename.split('.')[-1:][0]
            fp.write(data)
            fp.close()
            self.isvideo = True
            self.fileaudioextract()
        except Exception as e:
            pass
            print "Opening File Failed"
    def fileaudioextract(self ):
        if self.isvideo:
            print "Extracting Audio"
            try:
                os.system("ffmpeg -y -i Workspace/video."+self.openedfilename.split('.')[-1:][0]+ " -ab 320k -ac 2 -ar 44100 -vn Workspace/audio.mp3")
            except Exception as e:
                print "Extraction Failed"
        else:
            self.fileopen()
    def showresults(self):
        self.fileopener1 = Toplevel()
        self.openingmsg1 = "Opening Cut list......"
        self.fileopener1.title("Opening File")
        Label(self.fileopener1, text=self.openingmsg1).pack()
        try:
            self.openedfile1 = tkFileDialog.askopenfile(parent=self.fileopener1, mode='rb', title="Choose a file",filetypes=[ ('Text file','*.txt')])
            #self.openedfilename1 = self.openedfile1.name
            #print self.openedfilename.split('.')[-1:][0]
            #self.typeofvideo = self.openedfilename.split('.')[-1:]
            if self.openedfile1 is not None:
                data = self.openedfile1.read()
                self.openedfile1.close()
            self.fileopener1.destroy()
            fp = open('Workspace/cutlist.ctlst', 'wb')
            fp.write(data)
            fp.close()
            self.islist = True
        except Exception as e:
            pass
            print "Opening Text file failed. Make sure that the file opened is in a text file."
        print self.islist
        print self.isvideo
        if self.islist and self.isvideo:
            print "Both Video and cut files are open"
            # Both video and cut lists exists so we can start cutting.
            fp = open('Workspace/cutlist.ctlst','rb')
            for j, string in enumerate(fp.readlines()):
                init1 = string.split('\n')[0]
                #print init1
                if '#' in init1:
                    os.system('mkdir Workspace/audiocuts/' + init1.split('#')[1])
                    print 'mkdir Workspace/audiocuts/' + init1.split('#')[1]
                    self.filetype=init1.split('#')[1]
                else:
                    init1 = init1.split('\n')[0]
                    init2 = init1.split('-')[1]
                    init1 = init1.split('-')[0]
                    #print "ffmpeg -i Workspace/"+ self.openedfilename +" -ss " + init1 + " -t " + init2 + " -async 1 " + "Workspace/videocuts/"+self.filetype +"/"+init1 + "-" +init2 + "."+self.openedfilenametype
                    print "ffmpeg  -i  Workspace/audio.mp3  -ss "+ "0"+init1+ " -to "  +"0"+init2  + " -ab 256k Workspace/audiocuts/"+self.filetype+ "/audiocut" + str(j) + ".mp3"
                    os.system( "ffmpeg  -i  Workspace/audio.mp3 -ss "+ init1+ " -to "  +init2  + " -ab 256k Workspace/audiocuts/audiocut" + str(j) + ".mp3")
                print "Show REsults"
            # At this point first cutting based on audio cuts is done.
            # The second part includes cutting of audio according to the second
            # cut list file which is going to cut the video accordance to cut
            # list provided.
            fp.close()
            self.fileopener2 = Toplevel()
            self.openingmsg2 = "Opening Cut list......"
            self.fileopener2.title("Opening File")
            Label(self.fileopener2, text=self.openingmsg1).pack()
            try:
                self.openedfile2 = tkFileDialog.askopenfile(parent=self.fileopener2, mode='rb', title="Choose a file",filetypes=[ ('Text file','*.txt')])
                #self.openedfilename1 = self.openedfile1.name
                #print self.openedfilename.split('.')[-1:][0]
                #self.typeofvideo = self.openedfilename.split('.')[-1:]
                if self.openedfile2 is not None:
                    data = self.openedfile2.read()
                    self.openedfile2.close()
                self.fileopener2.destroy()
                fp = open('Workspace/cutlist2.ctlst', 'wb')
                fp.write(data)
                fp.close()
                self.islist = True
            except Exception as e:
                pass
                print "Opening Text file failed. Make sure that the file opened is in a text file."

            fp = open('Workspace/cutlist2.ctlst','rb')
            for string in fp.readlines():
                init1 = string.split('\n')[0]
                #print init1
                if '#' in init1:
                    os.system('mkdir Workspace/videocuts/' + init1.split('#')[1])
                    print 'mkdir Workspace/videocuts/' + init1.split('#')[1]
                    self.filetype=init1.split('#')[1]
                    self.folderlist.append(self.filetype)
                else:
                    init1 = init1.split('\n')[0]
                    init2 = init1.split('-')[1]
                    init1 = init1.split('-')[0]
                    print "ffmpeg -i Workspace/"+ self.openedfilename +" -ss " + init1 + " -t " + init2 + " -async 1 " + "Workspace/videocuts/"+self.filetype +"/"+init1 + "-" +init2 + "."+self.openedfilenametype
                    os.system( "ffmpeg -i Workspace/"+ self.openedfilename +" -ss " + init1 + " -to " + init2 + " -async 1 " + "Workspace/videocuts/"+self.filetype +"/"+init1 + "-" +init2 + "."+self.openedfilenametype)
                    fp.close()
                    self.thumbnailer()
        print "Show REsults"

    def thumbnailer(self):
        self.folderlist =["Music","Speech","Silence", "SpeechWithMusic", "SpeechWithNoise"]
        for string in self.folderlist:
            lists = os.listdir('Workspace/videocuts/'+string)
            os.system('mkdir Workspace/Thumbnails/' + string)
            for string1 in lists:
                print "ffmpegthumbnailer -i Workspace/videocuts/"+string+"/"+string1 + " -t 30% -s 256 -o Workspace/Thumbnails/" + string +"/"+string1 +".png 2> /dev/null"
                os.system("ffmpegthumbnailer -i Workspace/videocuts/"+string+"/"+string1 + " -t 30% -s 256 -o Workspace/Thumbnails/" + string +"/"+string1 +".png 2> /dev/null")
        self.displaythumbnails()
    def about(self):
        print "About function"


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
