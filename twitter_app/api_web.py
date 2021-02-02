from api import Api
from form import *
from datetime import datetime
from form_search import form_search
from searchbox import searchbox
import json
import re
import requests
import sys
import pathlib
res=str(pathlib.Path(__file__).parent.absolute())
sys.path.append(res)

def search(data,letype,liste):
    # détection du paramètre target
    if letype=="target":
        string=searchbox("keywords.txt")
    else :
        string=form_search(data)
    # init api twitter
    key1, key2, key3, key4 = get_keys()
    app=Api(key1, key2, key3, key4)
    num_res=25
    rt_enabled=False
    #recehrche twitter
    tweets=app.search_string(string,letype,liste,num_res,rt_enabled)
    #resultats
    res,details,stats_time,stats_words,list_media=get_pd(tweets)
    #print("[+] String here > ",res['tweetText'].to_list())
    stringpd= res['tweetText'].to_list()
    res=pd.DataFrame.to_json(res)[:-1]+",\"stats_time\":\""+str(stats_time)+"\","+json.dumps({"stats_words" : stats_words})[1:-1]+","+json.dumps({"medias":list_media})[1:]
    #df=pd.DataFrame()
    #res['stats_time']=stats_time
    
    # ancienne version dessous
    #res="<br>".join(res.tweetText.tolist())
    return res,stringpd

def get_keys():
    resultat=[]
    with open(res+"/keys.txt","r") as f:
        lines=f.readlines()
        for line in lines :
            resultat+=[re.sub(r"\s+","",line)]
    return resultat