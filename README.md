# biproductive

Authors: Shamil Arslanov, Rizvan Iskaliev, Maxim Faleev

Description: this repository created for application BiProductive, needed for analysing habits of person and listing
most useful habits, that makes human happy. Each day user enters which actions user made today (sport activity, playing
music, etc.)
, test his brain activity, and program analyses it and make personal recommendation, based on weekly results.

Link to
artifact: [link](https://docs.google.com/document/d/14AMeCV4WJotkQ8lvZcl2u_bB66lMKmu4/edit?usp=sharing&ouid=109541784549585358096&rtpof=true&sd=true)

Stack of technology:

- Django as a backend of application (can be easily deployed and most team members are in touch with this framework)
- PostgreSQL as a database (it is fast and all team members have experience with this database)
- Brighton as a backend for productivity checker game
- html, css as a front-end for web-application

How to launch the application:

- rename .env.example to .env and fulfill the variables.
- put .env file to ```biproductive/biproductive/biproductive/.env``` path
- run ```docker-compose up --build -d```
- run ```python biproductive/manage.py runserver```

