# API

## Specification

> Build a RESTFul API Boiler Plater include common modules

> Target Framework : Flask lastest version
> Target DB Engines : PostgreSQL, MongoDB

**Features**:

1. Base : Log, DAL(Data Access Layer), Mailer 
2. User : Auth, Users, RBAC ( Postgres )
3. Examples: Categories, Items, All kind of fields (Postgres)
4. User Access Logs, Audit Logs ( Mongo )
5. Session, Strictly Token Auth, Queue ( Redis )
6. Scheduler : https://apscheduler.readthedocs.io/en/latest/ ( Redis )

**Testing**:

1. Unit Test ( required )
2. Integration Test (optional)
3. E2E test ( optional )

**CI & CD**:

1. DB Engine config: PostgreSQL, MongoDB
2. DB Migration: migrations, seeds
3. Gitlab CI
4. Heroku Pipelines
5. Web Server : Nginx + [WSGI](https://www.fullstackpython.com/web-development.html) - [Gunicorn](https://gunicorn.org/#quickstart)