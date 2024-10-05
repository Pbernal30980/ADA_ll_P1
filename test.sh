#!/bin/bash

cd "$(dirname "$0")"

if [ "$1" ]; then
    PYTHONPATH=. python3 -m unittest test."$1"
else

    PYTHONPATH=. python3 -m unittest discover -s test -p "*_test.py"
fi
