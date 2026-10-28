#!/bin/sh
# usage: evidencias/run.sh <salida> <etiqueta>
cd "$(dirname "$0")/../laboratorio_seguridad" || exit 1
{
  echo "# $2"
  echo "# fecha: $(date -Iseconds)"
  echo "# python: $(python --version 2>&1)"
  echo "# base commit: $(git rev-parse --short HEAD 2>/dev/null)"
  echo "\$ python -m unittest discover -s tests -v"
  python -m unittest discover -s tests -v 2>&1
  echo "# exit code: $?"
} | sed -e 's#/c/Users/[^/]*#~#g' -e 's#C:\Users\[^\]*#~#g' > "../evidencias/$1"
