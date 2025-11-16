#!/bin/sh
set -e

host="$1"
shift
cmd="$@"

until pg_isready -h "$host" -p 5432; do
  echo "⏳ Aguardando PostgreSQL em $host..."
  sleep 1
done

echo "✅ PostgreSQL disponível! Executando aplicação..."
exec $cmd
