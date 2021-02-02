from flask import Flask, render_template,request
import pathlib
import sys
from redis import Redis
from rq import Queue
res=str(pathlib.Path(__file__).parent.absolute())+"/twitter_app"
res2=str(pathlib.Path(__file__).parent.absolute())

sys.path.append(res)
sys.path.append(res2)
import time
from twitter_app import api_web
from twitter_app import process_links




def create_app():

    app = Flask(__name__)
    #app.static_folder = 'static'
    @app.route('/')
    def homepage():
        return render_template('index.html')
    
    @app.route('/search',methods=['GET'])
    def get_data():
        global content
        content=""
        res,stringpd=api_web.search(request.args.get('data'),request.args.get('type'),request.args.get('liste'))
        
        
        content=stringpd
        return res

    @app.route('/getlinks',methods=['GET'])
    def get_links():
        q=Queue(connection=Redis())
        #res2=q.enqueue(process_links.get_links,content)
        while content=="":
            time.sleep(0.5)
        res2=process_links.get_links(content);
        return res2

    return app

