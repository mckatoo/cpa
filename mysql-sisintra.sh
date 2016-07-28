#!/bin/bash

case "$1" in
start)
  read -p "Digite l para acessar em rede local ou i para acessar pela internet: " LOCAL
esac

case "$LOCAL" in
l)
  ENDERECO='172.16.111.91'
  ;;
i)
  ENDERECO='campus1-iesi.ddns.net'
esac

case "$1" in
start)
  ssh -fN -L 3306:localhost:3306 cpd@$ENDERECO -p722
  ;;
stop)
  killall ssh
  ;;
*)
  echo 'DIGITE START PARA INICIAR OU STOP PARA FINALIZAR'
esac
