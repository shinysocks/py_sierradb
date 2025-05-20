all: run

run: setup
	printf "running"

setup:
	# python3 -m pip install venv
	rm -rf venv
	python3 -m venv venv
	source venv/bin/activate
	pip3 install psycopg2-binary
