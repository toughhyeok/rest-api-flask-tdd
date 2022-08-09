#!/bin/sh
# wait-for-postgres.sh

set -e
  
POSTGRES_HOST="$DB_HOST"
POSTGRES_PASSWORD="$DB_PASS"
POSTGRES_USER="$DB_USER"
POSTGRES_DBNAME="$DB_NAME"
shift
  
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST" -U $POSTGRES_USER -d $POSTGRES_DBNAME -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
  
>&2 echo "Postgres is up - executing command"
exec "$@"