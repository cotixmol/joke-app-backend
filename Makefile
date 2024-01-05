start-venv:
	source .venv/bin/activate

start-app:
	uvicorn main:app --reload

run-formater:
	flake8
