def searchbox(file):
    res=""
    import pathlib
    res=str(pathlib.Path(__file__).parent.absolute())
    file_abs=res+"/"+file
    with open(file_abs,'r') as f:
        for elem in f.readlines():
            elem=elem.replace('\n',"")
            if res=="":
                res="("+elem+")"
            if elem[0]=="-":
                res+=elem
            else :
                res+=" OR " + "("+elem+")"
    return str(res)


