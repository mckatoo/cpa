#!/bin/bash

case "$1" in
start)
  gunicorn cpa.wsgi -b 127.0.0.1:9000 -w3 -p /tmp/gunicorn_cpa.pid -D
  ;;
stop)
  kill `cat /tmp/gunicorn_cpa.pid`
  echo 'GUNICORN PARADO'
  ;;
restart)
  kill -HUP `cat /tmp/gunicorn_cpa.pid`
  echo 'GUNICORN REINICIADO'
  ;;
*)
  echo 'DIGITE START PARA INICIAR, STOP PARA FINALIZAR OU RESTART PARA REINICIAR'
esac
