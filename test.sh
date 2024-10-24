#!/bin/bash

cd "$(dirname "$0")"

if [ "$1" ]; then
    PYTHONPATH=. python test/$1.py $2
else

    PYTHONPATH=. python -m unittest discover -s test -p "*_test.py"
fi
