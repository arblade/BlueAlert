import requests
import re
import json
import bs4

def get_links(links):
    target=[]
    final=[]
    liste_links=[]
    rapport={}
    for link in links :

        res=requests.get(link,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        #Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0
        url=res.url
        http_return=res.text
        html=bs4.BeautifulSoup(http_return,features="lxml")
        if (html!=None) and (url not in liste_links) and url[:20]!='https://twitter.com':
            rapport={}
            liste_links.append(url)
            print("url ",url)
            print("liste links ",liste_links)
            print("[[++]] ",target)
            if html.find("meta",  property="og:title")!=None:
                title = html.find("meta",  property="og:title")["content"]
            if html.find("meta",  property="og:image")!=None:
                image = html.find("meta",  property="og:image")["content"]
            if html.find("meta",  property="og:description")!=None:
                description = html.find("meta",  property="og:description")["content"]
                rapport={"type":"ext", "link":url, "title":title, "image":image, "description":description}
            if rapport!={}:
                target.append(rapport)
            #,lambda x : requests.get(x.group()).url,
        
    print("[+]",target)
    return json.dumps({"links" : target})


