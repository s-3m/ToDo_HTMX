#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift

until PGPASSWORD="postgres" psql -h "$host" -d "todo" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 40
  break
done


>&2 echo "Postgres is up - executing command"
exec "$@"