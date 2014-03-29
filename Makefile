# Makefile
VIRTUALENV = venv/
PWD = `pwd`

install:
	make virtualenv
	make pip

virtualenv:
	virtualenv venv --no-site-packages --distribute

pip:
	. $(PWD)/.env; pip install -r requirements.txt --allow-all-external || . $(PWD)/.env; pip install -r requirements.txt

run:
	. $(PWD)/.env; python app.py