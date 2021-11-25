from fastapi import FastAPI
from scraper import Scraper
import uvicorn

app = FastAPI()
posts = Scraper()

@app.get("/")
async def index():
    
    return "Welcome to  Facebook scrapping service using fastAPI"

@app.get("/{page}")
async def scrapping(page):
    data=posts.scrapedata(page)
    return data
