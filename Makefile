# Makefile
VIRTUALENV = venv/
PWD = `pwd`

install:
	make virtualenv

virtualenv:
	virtualenv venv --no-site-packages --distribute
	# Install pip packages
	. $(PWD)/.env; pip install -r requirements.txt --allow-all-external || . $(PWD)/.env; pip install -r requirements.txt

run:
	. $(PWD)/.env; python app.py