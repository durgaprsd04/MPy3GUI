import os
def thumbnailer():
    string = ["MUSIC", "SPEECH", "SILENCE", "SPEECHWMUSIC","SPEECHWNOISE"]
    for j in string:
        cmd0 = "ls  Workspace/"+j+ "/ > Workspace/lists/msclst.txt"
        print cmd0
        os.system(cmd0)
        fp = open("Workspace/lists/msclst.txt")
        for i,line in enumerate(fp.readlines()):
            cmd = "mencoder -ss 2 -endpos 0.001 -ovc copy -nosound  Workspace/"+ j+"/" + line.split('\n')[0]+ " -o Workspace/lists/tmp"
            print cmd
            os.system(cmd)
            cmd1 = " mplayer -nosound -vo png Workspace/lists/tmp"
            print cmd1
            os.system(cmd1)
            cmd2 = "mv 00000001.png Workspace/lists/"+j+"image"+str(i)+".png"
            os.system(cmd2)
            print cmd2
    fp.close()
    os.system("ls Workspace/lists/*.png > Workspace/lists/msclst.txt")
    fp = open("Workspace/lists/msclst.txt")
    for line in fp.readlines():
        print line
        cmd3 = "convert " + line.split('\n')[0]+ " -resize '256x144^' "+ line.split('\n')[0]
        print cmd3
        os.system(cmd3)
thumbnailer()
