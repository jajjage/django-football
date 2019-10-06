#!/bin/bash
clear
echo "Checking ..."
echo
echo "PYLINT DISABLE"
grep -nr "pylint:\s*disable=" --color=always --include=\*.py .
echo
echo "PYLINT"
touch apps/__init__.py
python $(which pylint) --rcfile=.pylintrc apps/ 
rm apps/__init__.py
echo "TODO"
grep -nr "TODO" --color=always --include=\*.{py,html} .  | grep -v "[-][-]"
echo
echo "DEBUG STATEMENTS (IPDB)"
grep -nr "ipdb" --color=always --include=\*.py .
echo
echo "PIP OUTDATED"
pip list --outdated