#!/bin/bash
RED='\033[0;31m'
GREEN='\033[0;32m'
NOCOLOR='\033[0m'

clear
touch apps/__init__.py
python $(which pylint) --rcfile=.pylintrc apps/
exit_code=$? 
rm apps/__init__.py

if [[ exit_code -ne 0 ]] ; then
    echo -e "${RED}Pylint: errors${NOCOLOR}";
    exit $exit_code;
fi

echo -e "${GREEN}Pylint: passed${NOCOLOR}"

exit $exit_code