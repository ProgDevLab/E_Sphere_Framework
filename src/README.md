# project-name

[![License : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Icon](./icon.png)

## Table Of Contents

- [project-name](#project-name)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Access](#access)
  - [Getting Started](#getting-started)
    - [Environment Variables](#environment-variables)
    - [Build and Deploy](#build-and-deploy)
  - [Changelog](#changelog)
  - [Documentations](#documentations)
  - [Contributing](#contributing)
  - [Licence](#licence)

## Description

project-description

## Access

- **Development (Local)** :
  - [project-name Development](http://localhost)
  - [project-name Docs Development](http://localhost:3000)
- **Production (Local)** :
  - [project-name Production](http://localhost)
  - [project-name Docs Production](http://localhost:3000)
- **Production** :
  - [project-name Production](https://project-name_raw)
  - [project-name Docs Production](https://project-name_raw-docs)

## Getting Started

Here a sample of Docker Compose file : **docker-compose.yml**

```yaml
TODO
```

If you want you can **develop** this repository :

1) You need to install **[Docker](https://docs.docker.com/get-docker/)** and **[Make](https://progdevlab.gitlab.io/dyntools/#/docs/global/makefile)**
2) Create the `.env` file with the `.env.sample` file by refering to the [Environment Variables](#environment-variables)
3) [Build](#build) the application
4) [Deploy](#deploy) your application

### Environment Variables

| Parameter | Value Example | Description |
|-|-|-|
| PARAM | TODO | TODO Description |
|  |  |  |

### Build and Deploy

- **Production** :
  - `make build` : Build
  - `make start` : Start
  - `make start-detach` : Start in detach mode
  - `make stop` : Stop
  - `make start-docs` : Start Documentation Website
  - `make stop-docs` : Stop Documentation Website
- **Development** :
  - `make build-dev` : Build
  - `make start-dev` : Start
  - `make start-detach-dev` : Start in detach mode
  - `make stop-dev` : Stop
  - `make start-docs-dev` : Start Documentation Website
  - `make stop-docs-dev` : Stop Documentation Website

If you want to use Docker Buildx :

```bash
# Buildx Production Build (for ARM and x86-64 Processors)
docker buildx create --name mainBuilder
docker buildx use mainBuilder
docker buildx build --platform linux/amd64,linux/arm64 -t project-name-raw:latest --load .
```

## Changelog

See [CHANGELOG](./CHANGELOG.md) for more information.

## Documentations

- [Ideas](./docs/ideas.md)
- [Analysis](./docs/analysis.md)
- [Commands](./docs/commands.md)

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE.md) for more information.
