#!/bin/bash
set -e 

cd ../

FLASK_ENV=development FLASK_APP=app.py flask run
