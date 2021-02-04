import re
def form_search(string):
    string=re.sub(r"\s+"," ",string)
    string=re.sub(r"\s*-\s*","-",string)
    print(string)
    l_str = string.split("-")
    print(l_str)
    fin=[]
    for part in l_str :
        part=part.split(" ")
        res=" AND ".join(part)
        fin.append(res)

    if len(fin)>1:
        total="("+") OR (".join(fin)+")"
        
    else :
        total=fin[0]
    return total


print(form_search("test   ici - here"))



