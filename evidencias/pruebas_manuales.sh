#!/bin/sh
# Requiere el servidor en ejecucion: cd laboratorio_seguridad && python servidor.py
B=http://127.0.0.1:8765
caso() { echo; echo "### $1"; shift; echo "\$ $*"; "$@" -s -w "\nHTTP %{http_code}\n"; }
caso "PM-01 salud" curl $B/health
caso "PM-02 estudiante lee su expediente (permitido)" curl -H "Authorization: Bearer lab-ana" $B/expedientes/101
caso "PM-03 estudiante lee expediente ajeno de otra sede (denegado)" curl -H "Authorization: Bearer lab-ana" $B/expedientes/202
caso "PM-04 docente Central cambia nota en Pacifico (denegado)" curl -X POST -H "Authorization: Bearer lab-maria" -H "Content-Type: application/json" -d '{"nota":10}' $B/expedientes/202/nota
caso "PM-05 nota fuera de rango 150 (entrada invalida)" curl -X POST -H "Authorization: Bearer lab-maria" -H "Content-Type: application/json" -d '{"nota":150}' $B/expedientes/101/nota
caso "PM-06 JSON malformado (entrada invalida)" curl -X POST -H "Authorization: Bearer lab-maria" -H "Content-Type: application/json" -d '{nota:' $B/expedientes/101/nota
caso "PM-07 administrador intenta cambiar nota (denegado)" curl -X POST -H "Authorization: Bearer lab-admin" -H "Content-Type: application/json" -d '{"nota":99}' $B/expedientes/101/nota
caso "PM-08 sesion vencida (rechazada)" curl -H "Authorization: Bearer lab-vencida" $B/expedientes/101
caso "PM-09 sin credenciales (rechazado)" curl $B/expedientes/101
caso "PM-10 docente Central actualiza nota propia sede (permitido)" curl -X POST -H "Authorization: Bearer lab-maria" -H "Content-Type: application/json" -d '{"nota":85}' $B/expedientes/101/nota
caso "PM-11 revocar sesion de Ana" curl -X POST -H "Authorization: Bearer lab-ana" $B/sesiones/revocar
caso "PM-12 lectura con sesion revocada (rechazada)" curl -H "Authorization: Bearer lab-ana" $B/expedientes/101
caso "PM-13 administrador lee expediente de Pacifico (permitido)" curl -H "Authorization: Bearer lab-admin" $B/expedientes/202
caso "PM-14 Content-Length negativo (rechazado)" curl -X POST -H "Authorization: Bearer lab-maria" -H "Content-Length: -1" $B/expedientes/101/nota
caso "PM-15 nota de Pacifico intacta tras los intentos rechazados" curl -H "Authorization: Bearer lab-pedro" $B/expedientes/202
