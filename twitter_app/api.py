import tweepy
import json
import datetime

class Api():
    def __init__(self,consumerkey,consumersecret,accesstoken,accesstokensecret):
        #Clefs
        self.consumerkey=consumerkey
        self.consumersecret=consumersecret
        self.accesstoken=accesstoken
        self.accesstokensecret=accesstokensecret

        #Création de l'app
        self.auth = tweepy.OAuthHandler(self.consumerkey, self.consumersecret)
        self.auth.set_access_token(self.accesstoken, self.accesstokensecret)
        self.api = tweepy.API(self.auth)

    def search_string_no_RT(self,string,n):
        l=[]
        res=tweepy.Cursor(self.api.search,q=string+" -filter:retweets",tweet_mode='extended').items(n)
        for tweet in res:
            l.append(tweet)
        return l
    
    def search_string(self,string,letype,liste,n,rt_enabled=True):
        # vire les doublons
        l=[]
        status=[]
        c=0
        print("[+] letype est ", letype)
        print("[+] la liste est ", liste)
        if letype=="live":
            result_type="recent"
        elif letype=="popular":
            result_type="popular"
        elif letype=="target" :
            result_type="recent"
        elif liste!="":
            result_type="recent"
        else :
            result_type="mixed"
        print("[+] Mode chosen ", result_type)
        if liste != "":
            print("[+] Cas étudié : liste !")
            if liste=="geopolitique":
                print("[+] Cas précis : géopolitique !")
                res = self.api.list_timeline(list_id=1067720416607784960,tweet_mode='extended',result_type=result_type)[:n]
            if liste=="alerte-info":
                print("[+] Cas précis : alerte-info !")
                res = self.api.list_timeline(list_id=1212002219895218176,tweet_mode='extended',result_type=result_type)[:n]
            if liste=="osint":
                print("[+] Cas précis : osint !")
                res = self.api.list_timeline(list_id=1332407278687936512,tweet_mode='extended',result_type=result_type)[:n]
        else :
            if rt_enabled :
                res=tweepy.Cursor(self.api.search,q=string,tweet_mode='extended',result_type=result_type).items(n)
            else :
                res=tweepy.Cursor(self.api.search,q=string+" -filter:retweets",tweet_mode='extended',result_type=result_type).items(n)
        for tweet in res:
            if hasattr(tweet, 'retweeted_status'):
                if tweet.retweeted_status.full_text not in status :
                        #print(tweet.retweeted_status.full_text)
                    l.append(tweet)
                    c+=1
                    status.append(tweet.retweeted_status.full_text)
            elif tweet.full_text not in status :
                c+=1
                l.append(tweet)
                status.append(tweet.full_text)
        return l
        

    
