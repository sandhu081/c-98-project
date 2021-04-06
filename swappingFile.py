def swapFileData():
    fileone =input("enter file name ")
    filetwo =input("enter file name ")
    with open(fileone,"r" )as a:
        data_a = a.read()
    with open(filetwo,"r")as b:
        data_b = b.read()
    with open(fileone,"w")as a:
        a.write(data_b)
    with open(filetwo,"w")as b:
        b.write(data_a)
swapFileData()