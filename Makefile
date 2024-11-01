include .env

up:
	docker-compose --env-file .env -f compose.yml -p $(PROJECT_NAME) up -d

down:
	docker-compose --env-file .env -f compose.yml -p $(PROJECT_NAME) down
