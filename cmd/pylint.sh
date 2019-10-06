#!/bin/bash
clear
echo "PYLINT"
touch apps/__init__.py
python $(which pylint) --rcfile=.pylintrc apps/ 
rm apps/__init__.py
