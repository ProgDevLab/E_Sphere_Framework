# project_name

[![License : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Icon](./icon.png)

## Table Of Contents

- [project_name](#project_name)
  - [Table Of Contents](#table-of-contents)
  - [Description](#description)
  - [Access](#access)
  - [Getting Started](#getting-started)
    - [Requirements](#requirements)
    - [Environment Variables](#environment-variables)
    - [Build](#build)
    - [Deploy](#deploy)
  - [Changelog](#changelog)
  - [Documentations](#documentations)
    - [Docsify](#docsify)
  - [Contributing](#contributing)
  - [Licence](#licence)

## Description

project_description

## Access

- **Development (Local)** :
  - [project_name Development](http://localhost)
  - [project_name Docs Development](http://localhost:6007)
- **Production (Local)** :
  - [project_name Production](http://localhost)
  - [project_name Docs Production](http://localhost:6007)
- **Production** :
  - [project_name Production](https://project_name_raw)
  - [project_name Docs Production](https://project_name_raw-docs)

## Getting Started

Here a sample of Docker Compose file : **docker-compose.yml**

```yaml
TODO
```

If you want you can **develop** this repository :

1) You need to install the [Requirements](#requirements)
2) Create the `.env` file with the `.env.sample` file by refering to the [Environment Variables](#environment-variables)
3) [Build](#build) the application
4) [Deploy](#deploy) your application

### Requirements

We use **Docker** :

- Docker
- Docker Compose

### Environment Variables

| Parameter | Value Example | Description |
|-|-|-|
| PARAM | TODO | TODO Description |
|  |  |  |

### Build

```bash
# Development
docker-compose -f docker-compose.dev.yml build

# Production
docker-compose build

# Buildx Production Build (for ARM and x86-64 Processors)
TODO
```

### Deploy

```bash
# Development
docker-compose -f docker-compose.dev.yml up

# Production
docker-compose up
```

## Changelog

See [CHANGELOG](./CHANGELOG.md) for more information.

## Documentations

- [Ideas](./docs/ideas.md)
- [Analysis](./docs/analysis.md)
- [Commands](./docs/commands.md)

### Docsify

```bash
cd docsify

# Development
docker-compose -f docker-compose.dev.yml up

# Production
docker-compose up --build
```

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE.md) for more information.
