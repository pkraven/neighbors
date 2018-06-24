#!/usr/bin/env bash
set -e

./wait-for-it.sh neighbors-postgres:5432
export PYTHONPATH=/app/neighbors
alembic -c alembic/alembic.ini upgrade head

echo "$0"
echo "$1"

if [ "$1" = 'run' ]; then
    gunicorn
fi

if [ "$1" = 'debug' ]; then
    sleep infinity
fi

if [ "$1" = 'test' ]; then
    pytest
fi

exec "$@"
