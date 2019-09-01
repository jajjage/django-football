#!/bin/bash
clear
echo Checking ...
echo
echo FLAKE8
mv cmd/.flake8 .
python $(which flake8)
mv .flake8 cmd/.flake8
echo
echo PYLINT DISABLE
grep -nr "pylint:\s*disable=" --color=always --include=\*.py .
echo
echo PYLINT
touch apps/__init__.py
python $(which pylint) --rcfile=cmd/.pylintrc --load-plugins=pylint_django apps/ 

echo TODO
grep -nr "TODO" --color=always --include=\*.{py,html} .  | grep -v "[-][-]"
echo
echo "DEBUG STATEMENTS (IPDB)"
grep -nr "ipdb" --color=always --include=\*.py .
echo
echo GIT STATUS
git status
echo
echo COVERAGE
coverage run --source="apps/" ./manage.py test
coverage report | grep -v migrations
coverage html
echo
# echo UNITTESTS
# python manage.py test
echo
echo PIP OUTDATED
pip list --outdated --format=columns