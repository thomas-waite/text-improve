SHELL = /bin/sh

develop:
	pip3 install -r requirements.txt

serve_app:
	cd ./app; yarn start

serve_ml:
	cd ./server; FLASK_ENV=development FLASK_APP=app.py flask run -h 0.0.0.0 -p 80

docker:
	cd ./model; \
	docker build -t model .; \
	docker tag model:latest 873668083085.dkr.ecr.eu-west-2.amazonaws.com/text-improve:model; \
	cd ../server; \
	docker build -t server . \
	docker tag server:latest 873668083085.dkr.ecr.eu-west-2.amazonaws.com/text-improve:server; \

push_docker:
	docker push 873668083085.dkr.ecr.eu-west-2.amazonaws.com/text-improve:server; \
	docker push 873668083085.dkr.ecr.eu-west-2.amazonaws.com/text-improve:model; \


