from facebook_scraper import get_posts
import pymongo
from pymongo import MongoClient
###################### Connection to DB##############################
CONNECTION_STRING ="mongodb://mariem:mk122597@mongodb:27017/myFirstDatabase?authSource=admin"
client = pymongo.MongoClient(CONNECTION_STRING,  tlsAllowInvalidCertificates=True)
db = client.get_database('test1')

scrapp = pymongo.collection.Collection(db, 'scrap_fb')

class Scraper():
    def scrapedata(self,page):
        posts = get_posts(page, pages=3)
        data = []
        for post in posts:
            scrapp.insert({'post_id' : post['post_id'],'comments' : post['comments'],'likes' : post['likes'] ,'text' : post['text']})
            item={'post_id' : post['post_id'],'comments' : post['comments'],'likes' : post['likes'] ,'text' : post['text']}
            data.append(item)
        return(data)
        
        
        

