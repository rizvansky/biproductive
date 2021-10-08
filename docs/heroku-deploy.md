## How to deploy to the Heroku
- Register on Heroku if you are not registered (https://signup.heroku.com/) 
- Install required packages with ```pip install -r requirements.txt```
- Install Heroku CLI (https://devcenter.heroku.com/articles/heroku-cli)
- Login to Heroku terminal by ```heroku login```
- Create heroku app by ```heroku create``` or ```heroku create <app_name>``` for custom name of the application
- Run ```heroku git:remote -a <app_name>```
- Open ```settings.py``` file and modify ```ALLOWED_HOSTS``` by adding ```<app_name.herokuapp.com>```
- Commit changes
- Create PostgreSQL database on Heroku by ```heroku addons:create heroku-postgresql:hobby-dev```
- Go to ```https://dashboard.heroku.com/apps/<app_name>/settings``` and click on the ```Reveal Config Vars``` and copy 
  the ```DATABASE URL```. It has the following structure: 
  ```postgres://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>```
- Set these variables as Heroku environment variables below ```DATABASE_URL``` with the keys ```DB_USER```,
  ```DB_PASSWORD```, ```DB_HOST```, ```DB_PORT```, ```DB_NAME``` and the values retrieved from the ```DATABASE_URL```
- Add the ```SECRET_KEY``` environment variable and set it to some value
- Add the ```DISABLE_COLLECTSTATIC``` environment variable and set it to 1
- Add the ```HEROKU``` environment variable and set it to 1
- if you are on a main branch then run ```git push heroku main```, otherwise run 
  ```git push heroku <branch_name>:main```