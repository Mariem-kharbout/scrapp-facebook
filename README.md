# scrapp-facebook


The goal of this project is to build a scrapping service using fastAPI, save scrapping data in Mongo database and dockerize the service as well as the database.

### 1) Test the application
      install the requirement: 
          pip install requirements.txt
      then run this command: 
          uvicorn app:app --reload
      
      You can test with any public FB page by adding the name of the page:"http://127.0.0.1:8000/google"
      
### 2) Dockerization:
        run this command:
          docker-compose up
     
