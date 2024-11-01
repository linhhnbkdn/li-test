include .env

up:
	docker-compose -f compose.yml -p $(PROJECT_NAME) up --force-recreate -d

down:
	docker-compose -f compose.yml -p $(PROJECT_NAME) down

build:
	cd ./backend && docker build  --target production -t backend:production .

remove:
	docker rmi backend:production

start: build up
clean: down remove
