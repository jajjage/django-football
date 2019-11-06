#!/bin/bash
clear
echo "PYLINT"
touch apps/__init__.py
python $(which pylint) --rcfile=.pylintrc apps/
exit_code=$? 
rm apps/__init__.py
exit $exit_code