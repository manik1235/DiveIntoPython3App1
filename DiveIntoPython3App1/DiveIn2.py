import os, glob

def exampleAbove():
    os.chdir('c:/test/')
    filelist = glob.glob('*')
    # print(filelist)
    # print([os.path.realpath(f) for f in glob.glob('*')])
    # print([os.path.realpath(f) for f in filelist if])

    a_list = [0, 0, 0, 0]
    #print([elem * 2 for elem in a_list])
    #print([1 for elem in a_list])
    d_2d = [a_list for elem in a_list]
    # print(d_2d)
    d_3d = [d_2d for elem in d_2d]
    d_3d[0][0][0] = 1
    print(d_3d)

def exampleBelow():
    print("entered exampleBelow")
    print(__debug__)
    print ("Debug Mode: {0}".format()
    a_thing = [(os.stat(f), os.path.realpath(f)) for f in glob.glob("*.txt")]
    print (a_thing)




if __name__ == "__main__":
    print("entered __main__")
    exampleBelow()

