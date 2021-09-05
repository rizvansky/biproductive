Launching project: ``` python manage.py runserver```

Setting environment variables in
django: [link](https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f)

Installing docker compose utility for database:

- ```sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose```
- ```sudo chmod +x /usr/local/bin/docker-compose```
- ```docker-compose --version```

Run docker with database: ```cd biproductive/postgres_docker/docker-compose.yml && sudo docker-compose up --build -d```

Grant sudo to docker: ```sudo usermod -aG docker $USER```
Not forger to enable and start docker (using systemctl).

Check before pushing: ```python manage.py check --deploy```