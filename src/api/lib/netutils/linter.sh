#!/usr/bin/env bash

echo "-> mypy started"
if ! /usr/local/bin/mypy netutils; then
    echo "-> mypy failed"
    exit 1
else
    echo "-> mypy passed"
fi
echo

echo "-> flake8 started"
if ! /usr/local/bin/flake8 netutils; then
    echo "-> flake8 failed"
    exit 1
else
    echo "-> flake8 passed"
fi
echo

echo "-> pylint started"
if ! /usr/local/bin/pylint --rcfile=./setup.cfg -f colorized netutils; then
    echo "-> pylint failed"
    exit 1
else
    echo "-> pylint passed"
fi
echo
