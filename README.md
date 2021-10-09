# BiProductive

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1b8fcfb3465a4f02ab9a2d6dc445dfed)](https://app.codacy.com/gh/rizvansky/biproductive?utm_source=github.com&utm_medium=referral&utm_content=rizvansky/biproductive&utm_campaign=Badge_Grade_Settings)
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Description
This repository created for application BiProductive, needed for analysing habits of person and listing most useful
habits, that makes human happy. Each day user enters which actions user made today (sport activity, playing music, etc.)
, test his brain activity, and program analyses it and make personal recommendation, based on weekly results.

BiProductive allows the user to analyze their performance together with habit usage to evaluate the effect of each
habit. Each day user enters which actions they performed today (sport activity, playing music, etc.), test his brain
activity, and program analyzes it and make personal recommendation, based on weekly results.

## How to launch the application
- Locally
    - You should have Docker and Docker Compose installed
    - Go to the project folder
    - Rename .env.example to .env and fulfill the environment variables
    - Put .env file to ```./biproductive/biproductive``` directory
    - Run ```docker-compose up --build```
    - An application will be launched at ```0.0.0.0:8000``` address
- Heroku
    - If you want to deploy this application on your own Heroku host, read these [instructions](./docs/heroku-deploy.md)

## Stack of technologies
- Django (backend of application)
- PostgreSQL (database)
- psycopg2 (tool to manage this database with Python)
- whitenoise (static file serving for Django backend)
- gunicorn (WSGI HTTP Server)
- temppathlib
- seaborn
- tabulate
- md2pdf
- matplotlib
- Brighton (backend of productivity checker game)
- HTML, CSS (frontend of web-application)

## Prototypes and diagrams 
In this folder you can find the low-fidelity and high-fidelity prototypes and the use-case diagram: `./docs`

## RUP Artifact
Here you can find our RUP Artifact: 
[link](https://docs.google.com/document/d/14AMeCV4WJotkQ8lvZcl2u_bB66lMKmu4/edit?usp=sharing&ouid=109541784549585358096&rtpof=true&sd=true)

## How to contribute
- Create the fork of this repository
- Clone your fork by ```git clone <your_fork_url>```
- Go to the cloned repository directory
- Check that your fork is the ```origin``` remote by running ```git remote -v``` and checking that the URL of your fork is next to the word ```origin```
- Add this project repository to the ```upstream``` remote by ```git remote add upstream https://github.com/rizvansky/biproductive.git```
- Create a new branch from ```dev``` branch
- Fix or create and implement a new feature in your branch
- Follow the code style of the project anc comment the code you write
- Modify the documentation as needed
- Commit your changes. Write meaningful commit message
- Push your branch to your fork on GitHub (to the ```origin```)
- Go to your fork's GitHub page and open the pull request to the ```dev``` branch

## Authors
Rizvan Iskaliev, Shamil Arslanov, Maxim Faleev

## Acknowledgments
- [Memory game](https://github.com/beumsk/Memory)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/rizvansky/biproductive.svg?style=flat&logo=appveyor
[contributors-url]: https://github.com/rizvansky/biproductive/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/rizvansky/biproductive.svg?style=flat&logo=appveyor
[forks-url]: https://github.com/rizvansky/biproductive/network/members
[stars-shield]: https://img.shields.io/github/stars/rizvansky/biproductive.svg?style=flat&logo=appveyor
[stars-url]: https://github.com/rizvansky/biproductive/stargazers
[issues-shield]: https://img.shields.io/github/issues/rizvansky/biproductive.svg?style=flat&logo=appveyor
[issues-url]: https://github.com/rizvansky/biproductive/issues
[license-shield]: https://img.shields.io/github/license/rizvansky/biproductive.svg?style=flat&logo=appveyor
[license-url]: https://github.com/rizvansky/biproductive/blob/main/LICENSE
