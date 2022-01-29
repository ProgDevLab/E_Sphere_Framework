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
    - [Build](#build)
    - [Environment Variables](#environment-variables)
    - [Deploy](#deploy)
  - [Changelog](#changelog)
  - [Documentations](#documentations)
    - [Docsify : Development](#docsify--development)
    - [Docsify : Production](#docsify--production)
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

If you use the **classic** way, just clone this repository, build it and deploy it.

If you use the **Docker** way, here a sample of Docker Compose file : **docker-compose.yml**

```yaml
TODO
```

### Requirements

If you use the **classic** way :

- TODO

If you use the **Docker** way :

- Docker
- Docker Compose

### Build

If you use the **classic** way :

```bash
TODO
```

If you use the **Docker** way :

```bash
# Development
docker-compose -f docker-compose.dev.yml build

# Production
docker-compose build
```

### Environment Variables

| Parameter | Value Example | Description |
|-|-|-|
| PARAM | TODO | TODO Description |
|  |  |  |

### Deploy

If you use the **classic** way :

```bash
TODO
```

If you use the **Docker** way :

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

### Docsify : Development

```bash
cd docsify
docker-compose -f docker-compose.dev.yml up
```

### Docsify : Production

```bash
cd docsify
docker-compose up --build
```

## Contributing

See [CONTRIBUTING](./CONTRIBUTING.md) for more information.

## Licence

This project is licensed under the terms of the MIT license.

See [LICENSE](./LICENCE.md) for more information.