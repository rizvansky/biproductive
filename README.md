# BiProductive

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1b8fcfb3465a4f02ab9a2d6dc445dfed)](https://app.codacy.com/gh/rizvansky/biproductive?utm_source=github.com&utm_medium=referral&utm_content=rizvansky/biproductive&utm_campaign=Badge_Grade_Settings)
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Description
This repository created for application BiProductive, needed for analyzing habits of the person and listing most useful
habits, that makes human happy. Each day user enters which actions the user made today (sports activity, playing music, 
etc.), tests his brain activity, and the program analyzes it and makes a personal recommendation, based on weekly 
results.

BiProductive allows the user to analyze their performance together with habit usage to evaluate the effect of each
habit. Each day user enters which actions they performed today (sports activity, playing music, etc.), test his brain
activity, and the program analyzes it and make a personal recommendation, based on weekly results.
  - This project is deployed on Heroku: https://biproductive.herokuapp.com.

## How to deploy the application
- Locally
    - You should have Docker and Docker Compose installed.
    - Go to the project folder.
    - Rename .env.example to .env and fulfill the ```SECRET_KEY``` environment variable (for example. You can use 
      https://djecrety.ir) to generate the secret key.
    - Put .env file to ```./biproductive/biproductive``` directory.
    - Run ```docker-compose up --build```.
    - An application will be launched at ```0.0.0.0:8000``` address.
- Heroku
    - If you want to deploy this application on your own Heroku host, read [HEROKU.MD](docs/HEROKU.MD).

## Stack of technologies
- Django
- PostgreSQL
- JavaScript
- HTML
- Bootstrap

## RUP Artifact
[Here](https://docs.google.com/document/d/14AMeCV4WJotkQ8lvZcl2u_bB66lMKmu4/edit?usp=sharing&ouid=109541784549585358096&rtpof=true&sd=true) 
is the link to the RUP Artifact where you can find the list of stakeholders and their roles, functional and 
nonfunctional requirements, planned features, and other design specifications.

## Contributing
We appreciate all contributions. If you are planning to contribute back bug-fixes, please do so without any further 
discussion.

If you plan to contribute new features, utility functions, or extensions to the core, please first open an issue and 
discuss the feature with us. Sending a PR without discussion might end up resulting in a rejected PR because we might be
taking the core in a different direction than you might be aware of.

Check the [CONTRIBUTING.MD](./docs/CONTRIBUTING.MD) to learn more about making a contribution to our project.

## The BiProductive team
The original BiProductive code contributors can be found in [AUTHORS.MD](./docs/AUTHORS.MD).
### Special Thanks To  
[Rémy Beumier](https://github.com/beumsk) - developer of the 
[memory game for productivity check](https://github.com/beumsk/Memory)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[stars-shield]: https://img.shields.io/github/stars/rizvansky/biproductive.svg?style=flat&logo=appveyor
[stars-url]: https://github.com/rizvansky/biproductive/stargazers
[issues-shield]: https://img.shields.io/github/issues/rizvansky/biproductive.svg?style=flat&logo=appveyor
[issues-url]: https://github.com/rizvansky/biproductive/issues
[license-shield]: https://img.shields.io/github/license/rizvansky/biproductive.svg?style=flat&logo=appveyor
[license-url]: https://github.com/rizvansky/biproductive/blob/main/LICENSE
