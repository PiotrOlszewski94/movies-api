# movies-api
## Movies API 
 
### To run project locally, use docker and docker-compose utility
1. Clone project: ```git clone <project_url>```
2. Build project: ```docker-compose build```
3. Run project: ```docker-compose up -d```

### To run tests
1. Run: ```docker-compose exec web python manage.py test tests```

### Edpoints: 
/accounts/register/
/accounts/login/
/account/logout/
/movies/  
/favoritemovies/ 

There is an Insomnia collection of request in the file examples.json