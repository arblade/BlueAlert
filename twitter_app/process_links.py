import requests
import re
import json
import bs4

def get_links(stringpd):
    target=[]
    final=[]
    
    for tweet in stringpd :
        print("le tweet évalué est ",tweet)
        res=re.findall(r'(http[^\s]*)',tweet)
        if res!=[]:
            final+=res
    liste_links=[]
    print("final -->",final)
    for link in final:
        flag=True
        rapport={}
        print("le lien évalué est : ",link)
        try :
            res=requests.get(link,headers={'User-agent': 'Twitterbot'})
            url=res.url
        except :
            print("ERROR")
            flag=False
        if flag and url not in liste_links :
            liste_links.append(url)
       
            print("[+] lien result ",url)
            parts=url.split("/")
            if parts[2]=="twitter.com" and (parts[-2]=="video" or parts[-2]=="photo"):
                    # je suis donc sur une photo ou video twitter
                final_link="https://twitter.com/i/status/"+parts[-3]
                rapport={"type":"media", "link":final_link}
            elif parts[2]=="twitter.com":
                rapport={"type":"tweet", "link":url}
            else :
                print(">>> all non ok2")
                http_return=res.text
                html=bs4.BeautifulSoup(http_return)
                if html!=None :
                    print(">>> all non ok")
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
    print("[+] result final ",target)
    
    return json.dumps({"links" : target})