SHELL = /bin/sh

develop:
	pip3 install -r requirements.txt

serve_app:
	cd ./app; yarn start

serve_ml:
	cd ./server; FLASK_ENV=development FLASK_APP=./src/app.py flask run

