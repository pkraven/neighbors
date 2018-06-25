#!/usr/bin/env bash
set -e

./wait-for-it.sh neighbors-postgres:5432
export PYTHONPATH=/app/neighbors
alembic -c alembic/alembic.ini upgrade head

echo "$0"
echo "$1"

if [ "$1" = 'run' ]; then
    gunicorn app:api -b 0.0.0.0:$2
fi

if [ "$1" = 'sleep' ]; then
    sleep infinity
fi

exec "$@"
