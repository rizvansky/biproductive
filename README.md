# BiProductive

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1b8fcfb3465a4f02ab9a2d6dc445dfed)](https://app.codacy.com/gh/rizvansky/biproductive?utm_source=github.com&utm_medium=referral&utm_content=rizvansky/biproductive&utm_campaign=Badge_Grade_Settings)
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

## Description

This repository contains the application BiProductive, which analyzes the habits of the person, tests his productivity,
and defines dependencies between habits and productivity. Each day user enters the actions they made today (sports
activity, meditation, smoking, etc.) and tests their brain performance. Then the application computes the correlation
between habits and user's performance, and makes personal recommendations.

-   This project is deployed on Heroku: https://biproductive.herokuapp.com.
    
-   The video with demo is available 
    [here](https://drive.google.com/file/d/1q6ioV4W50Un--JNKLv6IV0rFbHXYZwCy/view?usp=sharing).
  
![1](./docs/demo.gif)

## Functionality of our application

-   You can register to the website, providing any unused username, email, and password. You can log in using his username
    and password.
    
-   After login at the home page you can see the dashboard with weekly statistics of habits usage and his brain activity
    during the productivity testing.
    
-   Also, on request, you can request from the system weekly report with analysis of his habits (in future we will add
    sending report by email each week).
    
-   You can add as many habits as you want for tracking them.

-   During the day or at the end of the day you can mark habits you completed and not completed (e.x. Swimming - Yes,
   Smoking - No) only once a day (no refilling can be done).

-   Once a day (preferably in the evening) you can test how well your brain works after the day by playing a memory game.

-   So, data about the brain activity after the day and statistics of habit usage could provide personal recommendations
  about habits (which habits increase brain activity, which not).

## Main components of our application

We deployed our project or Heroku, so as a web server that handles client requests we used `gunicorn`.

We organized business logic of application into 4 main components/modules:

-   User habit tracker - django application that is responsible for tracking habits (user can start tracking his habit by
  adding it and each day at the special form mark the habit completed or not (e.x. did you read a book today or not).

-   Productivity testing tool - small django application with javascript game that aims to track everyday brain activity
  after completing (or not completing) habit activities.

-   Habit analyzer tool - ML application that calculates how well habits affects your brain.

-   Report generation tool - wraps data, received from habit analyzer, and prepares a small pdf report with charts &
  tables.

In the storage layer we have used 2 databased:

-   Habit history database, that stores user's tracking habits and their usage.

-   Productivity history database, that tracks user's everyday brain activity.

![](docs/dynamic-view-updated.png)
*Dynamic view, describing main components of our application (static/dynamic view can be found in our artifact)*

## How to deploy the application

- Locally
    - You should have Docker and Docker Compose installed.

    - Go to the project folder.

    - Rename .env.example to .env and fill the ```SECRET_KEY``` environment variable. For example, you can use
      https://djecrety.ir) to generate the secret key.
      
    -   Put .env file to ```./biproductive/biproductive``` directory.
        
    -   Run ```docker-compose up --build```.
        
    -   An application will be launched at ```0.0.0.0:8000``` address.
    
-   Heroku
    -   If you want to deploy this application on your own Heroku host, read [HEROKU.MD](docs/HEROKU.MD).

## Stack of technologies

-   Django
-   PostgreSQL
-   JavaScript
-   HTML
-   Bootstrap

## RUP Artifact

[Here](https://docs.google.com/document/d/14AMeCV4WJotkQ8lvZcl2u_bB66lMKmu4/edit?usp=sharing&ouid=109541784549585358096&rtpof=true&sd=true) 
is the link to the RUP Artifact where you can find the list of stakeholders and their roles, functional and 
non-functional requirements planned features, and other design specifications.

Also, you can see the design development history [here](./docs/DESIGN_DEVELOPMENT.MD).

## Contributing

We appreciate all contributions. If you are planning to contribute back bug-fixes, please do so without any further
discussion.

If you plan to contribute new features, utility functions, or extensions to the core, please first open an issue and
discuss the feature with us. Sending a PR without discussion might end up resulting in a rejected PR because we might be
taking the core in a different direction than you might be aware of.

Check the [CONTRIBUTING.MD](./docs/CONTRIBUTING.MD) to learn more about making a contribution to our project.

## Used linters in our project

During the development of our project we have configured git pre-commit checks, defined in `.pre-commit-config.yaml`:

-   `isort` for sorting names of imported libraries
-   `black` - Python code formatter
-   `flake8` - combination of various code refactor tools like `pyflakes`, `pycodestyle`, checks for code styles.

## Code coverage

Code coverage of our web-application - 86%. The application was tested locally with python package - `coverage`.
Generated report and instruction how to test are described in [COVERAGE.md](docs/COVERAGE.md).

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
[license-shield]: https://img.shields.io/github/license/rizvansky/biproductive.svg?style=flat
[license-url]: https://github.com/rizvansky/biproductive/blob/main/LICENSE
