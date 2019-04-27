.PHONY: up
up: docker-compose.yml
	@echo "$@"
	docker-compose up

.PHONY: down
down: docker-compose.yml
	@echo "$@"
	docker-compose down

.PHONY: clean
clean:
	@echo "$@"
	docker kill $(shell docker ps -a -q) || true
	docker rm $(shell docker ps -a -q) || true

.PHONY: shell
shell:
	@echo "$@"
	docker exec -it authorization360 \
		/bin/bash

.PHONY: python_shell
python_shell:
	@echo "$@"
	docker exec -it authorization360 \
		flask shell