.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo -e "Installing pipenv...."
	@pip3.7 install pipenv
	@pipenv --python 3.7
	@pipenv install requests
	@pipenv install pytest
test:
	@echo -e "\n\n\n"
	@echo -e "Testing..."
	@pipenv run pytest tests/tests.py | tee results.txt
run:
	@echo -e "\n\n\n"
	@echo -e "Starting program..."
	@pipenv run python app.py | tee -a results.txt
deploy:
	@echo -e "\n\n\n"
	@echo -e "Doing git work..."
	@git add results.txt
	@git commit -m "Pushing results"
	@git push origin master
