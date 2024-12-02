#!/bin/bash

# This script creates a Python venv with the right dependencies (if such venv
# doesn't already exist) and then builds the website.

set -e

if [ ! -e pyvenv ]; then
  python3 -m venv --upgrade-deps pyvenv
  . pyvenv/bin/activate
  pip install --user --upgrade -e .
else
  echo "Pyvenv already exists; not reinstalling it."
  echo "If packages changed, please remove venv dir, then rerun this script."
  . pyvenv/bin/activate
fi

python3 -m mkdocs build --no-directory-urls --site-dir public
