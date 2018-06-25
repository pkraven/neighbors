#!/usr/bin/env bash
set -e

./wait-for-it.sh neighbors-postgres:5432
./wait-for-it.sh neighbors:8080

pytest --tb short -vv .
