start-venv:
	source .venv/bin/activate

start-app:
	uvicorn main:app --reload

run-formater:
	flake8

build-test-image:
	cd core/tests/mock_services/joke_api && \
	docker build -t fake-joke-api . && \
	docker stop fake-joke-api-container || true && \
	docker rm fake-joke-api-container || true && \
	docker run --name fake-joke-api-container -d -p 8000:80 fake-joke-api
