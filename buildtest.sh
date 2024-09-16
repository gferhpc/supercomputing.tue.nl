#!/bin/bash

# This script creates a Python venv with the right dependencies (if such venv
# doesn't already exist) and then builds the website.

set -e

if [ ! -e pyvenv ]; then
	python3 -m venv --upgrade-deps pyvenv
	pip install --upgrade -r requirements.txt
	pip install -e .
else
	echo "Pyvenv already exists; not reinstalling it."
	echo "If packages changed, please remove venv dir, then rerun this script."
fi
. pyvenv/bin/activate

python3 -m mkdocs build --no-directory-urls --site-dir public
