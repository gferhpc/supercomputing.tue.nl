#!/bin/bash

# This script creates a Python venv with the right dependencies (if such venv
# doesn't already exist) and then builds the website.

set -e

venvdir="$(dirname $0)/pyvenv"
python="${PYTHON:-python3}"

if [ ! -e "$venvdir" ]; then
  "$python" -m venv --upgrade-deps "$venvdir"
  . "$venvdir"/bin/activate
  pip install --upgrade -e .
else
  echo "Pyvenv already exists; not reinstalling it."
  echo "If packages changed, please remove venv dir, then rerun this script."
  . "$venvdir"/bin/activate
fi

"$python" -m mkdocs build --no-directory-urls --site-dir public
echo "Listening on http://localhost:8000."
echo "Hit ctrl-C to quit."
"$python" -m mkdocs serve -q
