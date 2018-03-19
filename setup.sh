docker-compose -f ./manage/runner/docker-compose.yml up --build
docker cp $(docker-compose -f ./manage/runner/docker-compose.yml ps -q data_manager):/tmp/structure/output/dict/reflections/ ./src/database/structure/dict/
docker cp $(docker-compose -f ./manage/runner/docker-compose.yml ps -q data_manager):/tmp/structure/output/dict/categories/ ./src/database/structure/dict/
