.SILENT:

all: run

run: setup
	python3 SamplePythonScript.py

setup:
	python3 -m venv venv
	. venv/bin/activate
	pip3 install psycopg2-binary
	echo "successfully installed virtual environment"

clean:
	rm -rf venv
