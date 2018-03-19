# docker-grafana-graphite makefile

# Environment Varibles
CONTAINER = data_manager

setup :
	docker-compose -f ./manage/runner/docker-compose.yml up --build
	bash -c "docker cp $(docker-compose -f ./manage/runner/docker-compose.yml ps -q data_manager):/tmp/structure/output/dir/reflections/ ./data"

down :
	docker-compose down

shell :
	docker exec -ti $(CONTAINER) /bin/bash

tail :
	docker logs -f $(CONTAINER)