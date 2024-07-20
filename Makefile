install:
	#install commands
	# python.exe -m pip install --upgrade pip
	pip install --upgrade pip &&\
		pip install -r requirements.txt
post-install:
	python -m textblob.download_corpora
format:
	#format code
	# python -m black {source_file_or_directory}
	black *.py libs/*.py
lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py libs/*.py
test:
	#test
	python -m pytest -vv --cov=libs --cov=main test_*.py
build:
	# build container
	docker build -t deploy-fastapi .
run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 ae5459dd5b61
deploy:
	#deploy
	aws ecr get-login-password --region ap-southeast-2 | docker login --username AWS --password-stdin 419609558773.dkr.ecr.ap-southeast-2.amazonaws.com
	docker build -t fastapi_wiki .
	docker tag fastapi_wiki:latest 419609558773.dkr.ecr.ap-southeast-2.amazonaws.com/fastapi_wiki:latest
	docker push 419609558773.dkr.ecr.ap-southeast-2.amazonaws.com/fastapi_wiki:latest
all: install post-install lint test deploy