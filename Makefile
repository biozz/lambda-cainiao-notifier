install:
	python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -r requirements.txt

requirements:
	 poetry export -f requirements.txt -o requirements.txt
