# Makefile

VIRTUALENV = venv/
PWD = `pwd`


install:
	make virtualenv

virtualenv:
	virtualenv venv --no-site-packages --distribute
	# Install pip packages
	. $(VIRTUALENV)bin/activate; pip install -r requirements.txt --allow-all-external || . venv/bin/activate; pip install -r requirements.txt

run:
	. $(VIRTUALENV)bin/activate; python app.py