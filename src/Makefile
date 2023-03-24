# Production
build:
	docker compose -f ./docker/docker-compose.yml build

start:
	docker compose -f ./docker/docker-compose.yml up

start-detach:
	docker compose -f ./docker/docker-compose.yml up -d

stop:
	docker compose -f ./docker/docker-compose.yml down


start-docs:
	docker compose -f ./docsify/docker-compose.yml up --build

stop-docs:
	docker compose -f ./docsify/docker-compose.yml down


# Development
build-dev:
	docker compose -f ./docker/docker-compose.dev.yml build

start-dev:
	docker compose -f ./docker/docker-compose.dev.yml up

start-detach-dev:
	docker compose -f ./docker/docker-compose.dev.yml up -d

stop-dev:
	docker compose -f ./docker/docker-compose.dev.yml down


start-docs-dev:
	docker compose -f ./docsify/docker-compose.dev.yml up

stop-docs-dev:
	docker compose -f ./docsify/docker-compose.dev.yml down
