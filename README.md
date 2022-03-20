# Lab: Django REST Framework, Docker, Postgres
## Overview
Use Django REST Framework to create an API, then “containerize” it with Docker and implement Postgres

## Implementation Notes
- You should NOT be running Postgres directly on host machine.
  - This means that operations like createsuperuser and migrate will need to happen inside the container.
  - For example…
      - docker-compose run web python manage.py migrate

## Features - Django REST Framework
- Make your site a DRF powered API as you did in previous lab.
- Adjust project’s permissions so that only authenticated user’s have access to API.
- Add a custom permission so that only author of blog post can update or delete it.
- Add ability to switch user’s directly from browsable API.
## Features - Docker
- NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
- create Dockerfile based off python:3.8-slim
- create docker-compose.yml to run Django app as a web service.
- enter docker-compose up --build to start your site.
- add postgres 11 as a service
  - Note: It is not required to include a volume so that data can persist when container is shut down.
- Go to browsable api and confirm site properly restricts users based on their permissions.
