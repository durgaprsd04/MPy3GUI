def merge():
    """ This function reads the audio cuts and merges the smaller pieces of it chunks of atleast 5s"""
    t_threshold = 1
    fp = open('Workspace/classified.txt','r')
    fq = open('Workspace/tst2.txt','w')
    string = fp.readline()
    p_start = string.split('-')[0]
    p_length = float(string.split('-')[1])
    p_data = int(string.split('-')[2])
    for j, string in enumerate(fp.readlines()):
        c_start = string.split('-')[0]
        c_length = float(string.split('-')[1])
        c_data = int(string.split('-')[2])
        if c_data == p_data:
            p_length = p_length + c_length
        else:
            fq.write("%s-%f-%d\n" %(p_start,p_length,p_data))
            p_data = c_data
            p_start = c_start
            p_length = c_length
    if c_data == p_data:
        fq.write("%s-%f-%d\n" %(p_start,p_length,p_data))
    else:
        fq.write("%s-%f-%d\n" %(c_start,c_length,c_data))
    fp.close()
    fq.close()
    fr = open('Workspace/tst2.txt','r')
    fs = open('Workspace/tst3.txt','w')
    string = fr.readline()
    p_start = string.split('-')[0]
    p_length = float(string.split('-')[1])
    p_data = int(string.split('-')[2])
    string = fr.readline()
    c_start = string.split('-')[0]
    c_length = float(string.split('-')[1])
    c_data = int(string.split('-')[2])
    fs.write("%s-%f-%d\n" %(p_start,p_length,p_data))
    for j, string in enumerate(fr.readlines()):
        n_start = string.split('-')[0]
        n_length = float(string.split('-')[1])
        n_data = int(string.split('-')[2])
        if c_length < t_threshold:
            if p_data == n_data:
                c_data = p_data
            elif c_data == 1:
                c_data = p_data
            elif c_data == 2:
                if (p_data == 3) or (n_data == 3):
                    c_data = 3
                elif p_data == 1:
                    c_data = n_data
                elif n_data == 1:
                    c_data = p_data
                elif (p_data == 5) or (n_data == 5):
                    c_data = 5
            elif c_data == 3:
                if (p_data == 2) or (n_data == 2):
                    c_data = 2
                elif p_data == 1:
                    c_data = n_data
                elif n_data == 1:
                    c_data = p_data
                elif (p_data == 5) or (n_data == 5):
                    c_data =5
            elif c_data == 4:
                if (p_data == 5) or (n_data == 5):
                    c_data = 5
                elif p_data == 1:
                    c_data = n_data
                elif n_data == 1:
                    c_data = p_data
                elif (p_data == 3) or (n_data == 3):
                    c_data = 3
            else:
                if (p_data == 4) or (n_data == 4):
                    c_data = 4
                elif p_data == 1:
                    c_data = n_data
                elif n_data == 1:
                    c_data = p_data
                elif (p_data == 3) or (n_data == 3):
                    c_data = 3
        fs.write("%s-%f-%d\n" %(c_start,c_length,c_data))
        p_start = c_start
        p_length = c_length
        p_data = c_data
        c_start = n_start
        c_length = n_length
        c_data = n_data
    fs.write("%s-%f-%d\n" %(n_start,n_length,n_data))
    fr.close()
    fs.close()
    ft = open('Workspace/tst3.txt','r')
    fu = open('Workspace/merged.txt','w')
    string = ft.readline()
    p_start = string.split('-')[0]
    p_length = float(string.split('-')[1])
    p_data = int(string.split('-')[2])
    for j, string in enumerate(ft.readlines()):
        c_start = string.split('-')[0]
        c_length = float(string.split('-')[1])
        c_data = int(string.split('-')[2])
        if c_data == p_data:
            p_length = p_length + c_length
        else:
            fu.write("%s-%f-%d\n" %(p_start,p_length,p_data))
            p_data = c_data
            p_start = c_start
            p_length = c_length
    if c_data == p_data:
        fu.write("%s-%f-%d\n" %(p_start,p_length,p_data))
    else:
        fu.write("%s-%f-%d\n" %(c_start,c_length,c_data))
    ft.close()
    fu.close()
