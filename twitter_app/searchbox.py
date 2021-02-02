def searchbox(file):
    res=""
    import os
    cwd = os.getcwd()
    print(">>>> ",cwd)
    file_abs=os.path.join(cwd, "public/twitter_app/"+file)
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


