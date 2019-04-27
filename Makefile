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

.PHONY: alembic
alembic:
	@echo "$@"
	docker exec -it -e PYTHONPATH=. authorization360 \
		alembic -c alembic/alembic.ini $(ARGS)

.PHONY: pip_compile
pip_compile:
	@echo "$@"
	docker exec -it authorization360 \
		pip-compile --output-file requirements.txt requirements.in