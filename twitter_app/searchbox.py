def searchbox(file):
    res=""
    import pathlib
    path=str(pathlib.Path(__file__).parent.absolute())
    file_abs=path+"/"+file
    with open(file_abs,'r') as f:
        for elem in f.readlines():
            elem=elem.replace('\n',"")
            if res=="":
                res="("+elem+")"
            if elem[0]=="-":
                res+=elem
            else :
                res+=" OR " + "("+elem+")"
    print("[+] résultat searchbox : ", str(res))
    return str(res)


