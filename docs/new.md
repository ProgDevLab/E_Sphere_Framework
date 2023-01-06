# E Sphere Framework : New Framework

![Icon](../icon.png)

## Table Of Contents

- [E Sphere Framework : New Framework](#e-sphere-framework--new-framework)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Global Features](#global-features)
  - [Backend Features](#backend-features)
  - [Frontend Features](#frontend-features)
  - [Global Git Architecture](#global-git-architecture)
  - [Backend Git Architecture](#backend-git-architecture)
  - [Frontend Git Architecture](#frontend-git-architecture)
  - [Global Commands](#global-commands)
  - [Backend Commands](#backend-commands)
  - [Frontend Commands](#frontend-commands)

## Description

Each **Project** can use one or many **Framework**, these need to have some **functionality** by default, here is a lot of **feature** needed.

## Global Features

- **Language** : LTS (Long-Term Support) Version (fixed version).
- **Dependency Manager** : Dependencies management with backup of successful run.
- **Docker** : Container management.
  - **Docker Compose**
  - **Development** and **Production** environment.
  - **.env** Strategy (conserve global vars into **.env** file locally and **.env.sample** remotely).
  - **.dockerignore** Strategy (ignore some files or folder to build the image).
  - **Docker Secret** Strategy (secure password and credentials).
  - **Docker Buildx** System (**AMD64** and **ARM** Build).
- **Continuous Integration** : GitLab, GitHub, Drone.
- **Continuous Deployment** : AWS, GCP, Azure, Heroku, Netlify.
- **Code Quality** : Linter, Prettier, SonarQube.
- **Git Quality** : EditorConfig, Husky, CommitLint, Semantic Release.
- **Logging** : Winston.
- **Security** : Auth0, OAuth2, OpenID Connect.
- **Testing** :
  - **Unit** : Vitest, Pytest.
  - **Feature** : Cucumber.
  - **Mock** : Wiremock.

## Backend Features

- **REST API Framework** : Django, FastAPI, Express, NestJS.
- **Payload, Request and Response Validator** : Pydantic.
- **API Documentation** : Swagger, ReDoc.
- **API Client Lib** : OpenAPI Client Generator.
- **Database ORM** : SQLAlchemy, TypeORM.
- **Database** :
  - **SQL** : PostgreSQL, MariaDB, SQLite.
  - **NoSQL** : MongoDB.

## Frontend Features

- **Single Page Application Framework** : ReactJS, VueJS.
- **State Management** : Pinia.
- **CSS Framework** : Materialize, Material Design, MUI, Vuetify, Bootstrap.
- **Request Engine** : Axios, HTTPX.
- **Testing** : Cypress.

## Global Git Architecture

- **docs** : Documentation folder.
  - **commands.md** : Commands List documentation.
- **src** : Source code folder.
- **test** : Test source code folder.
  - **functional** : End To End Test source code folder.
  - **unit** : Unit Test source code folder.
  - **mock** : Wiremock source code folder.
- **tmp** : Temporary folder.
- **.dockerignore** : ignore some files or folder to build the image.
- **.gitignore** : ignore some files or folder to commit.
- **.env** : Local environment file.
- **.env.sample** : Sample environment file.
- **Dockerfile.dev** : Dockerfile file for development.
- **Dockerfile** : Dockerfile file for production.
- **docker-compose.dev.yml** : Docker Compose file for development.
- **docker-compose.yml** : Docker Compose file for production.

## Backend Git Architecture

- **docs** : Documentation folder.
  - **database.md** : Database documentation.
- **src** : Source code folder.
  - **config** : Configuration folder.
    - **config.?** : Environment variable management.
    - **db.?** : Database init.
    - **logger.?** : Logger init.
    - **server.?** : Server init.
  - **controllers / routers** : API endpoints (GET, POST, PUT, DELETE).
  - **migration** : Database migration script folder.
  - **models** : Models of each database entity.
  - **types** : Custom type of payload, request, response.
  - **services** : Data services (get, create, update, delete) and extra services (utils, security).
  - **main.?** : Application launch file.

## Frontend Git Architecture

- **docs** : Documentation folder.
  - **ui.md** : UI documentation.
- **nginx** : NGINX Config.
  - **entrypoint.sh** : Docker entrypoint to collect environment variables.
  - **nginx.conf** : NGINX config file.
- **public** : Public folder.
- **src** :
  - **components** : Components folder.
  - **models** : Models folder.
  - **router** : Router folder.
  - **services** : Services folder.
  - **store** : Store folder.
  - **views** : Views folder.
  - **main.?** : Main init.

## Global Commands

- **Build** : Development and Production Build.
- **Start** : Development and Production Start.
- **Lint** : Check source code syntax.
- **Format** : Format source code syntax.
- **Mock** : Launch Wiremock with API mocking.
- **Test (all test, unit test, functional test, watch, coverage)** : Launch Test.

## Backend Commands

- **DB Migrate** : Launch Database Migration.
- **Lib Generate** : Generate the client library for frontend.

## Frontend Commands

- Nothing.
