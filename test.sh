#!/bin/bash

cd "$(dirname "$0")"

if [ "$1" ]; then
    PYTHONPATH=. python 3 test/$1.py $2
else

    PYTHONPATH=. python 3 -m unittest discover -s test -p "*_test.py"
fi
