# Prueba de reproducibilidad: ejecucion de la suite siguiendo solo el README
# fecha: 2026-10-30T19:46:22-06:00
# ejecutor: Javier Alejandro Mendoza Gonzalez (companero distinto del autor, Andrey Alonso Hernandez Salazar)
# entorno: Linux 7.0.0-42-generic, Python 3.14.4, curl 8.18.0
# clon limpio de https://github.com/andreyhnzzz/QA-Lab1 en commit 216e80c
# nota: comandos ejecutados mediante un asistente de IA (Claude Code) en la maquina del ejecutor

## Paso 1 del README tal como esta escrito (python)
$ python -m unittest discover -s tests -v
bash: python: command not found
(dificultad D-1: 'python' no existe en este Linux; se usa python3)

## Ejecucion limpia 1 (sin __pycache__)
$ python3 -m unittest discover -s tests -v
test_ruta_inexistente_devuelve_404 (test_api.ApiExpedientes.test_ruta_inexistente_devuelve_404) ... ok
test_salud_responde_sin_credenciales (test_api.ApiExpedientes.test_salud_responde_sin_credenciales) ... ok
test_tc01_api_estudiante_lee_expediente_propio (test_api.ApiExpedientes.test_tc01_api_estudiante_lee_expediente_propio) ... ok
test_tc04_api_estudiante_no_lee_expediente_ajeno (test_api.ApiExpedientes.test_tc04_api_estudiante_no_lee_expediente_ajeno) ... ok
test_tc05_api_docente_no_modifica_nota_de_otra_sede (test_api.ApiExpedientes.test_tc05_api_docente_no_modifica_nota_de_otra_sede) ... ok
test_tc06_api_sesion_revocada_pierde_acceso (test_api.ApiExpedientes.test_tc06_api_sesion_revocada_pierde_acceso) ... ok
test_tc07_api_sesion_vencida_o_ausente_es_rechazada (test_api.ApiExpedientes.test_tc07_api_sesion_vencida_o_ausente_es_rechazada) ... ok
test_tc09_api_entrada_invalida_devuelve_400_sin_cambios (test_api.ApiExpedientes.test_tc09_api_entrada_invalida_devuelve_400_sin_cambios) ... ok
test_tc11_api_nota_fuera_de_rango_no_se_persiste (test_api.ApiExpedientes.test_tc11_api_nota_fuera_de_rango_no_se_persiste) ... ok
test_tc12_api_limite_de_tamano_del_cuerpo (test_api.ApiExpedientes.test_tc12_api_limite_de_tamano_del_cuerpo) ... ok
test_tc12b_api_content_length_negativo_se_rechaza (test_api.ApiExpedientes.test_tc12b_api_content_length_negativo_se_rechaza) ... ok
test_sec07_auditoria_registra_usuario_y_no_guarda_tokens (test_unidad.Auditoria.test_sec07_auditoria_registra_usuario_y_no_guarda_tokens) ... ok
test_docente_lee_expediente_de_su_sede (test_unidad.LecturaExpedientes.test_docente_lee_expediente_de_su_sede) ... ok
test_tc01_estudiante_lee_expediente_propio (test_unidad.LecturaExpedientes.test_tc01_estudiante_lee_expediente_propio) ... ok
test_tc03_admin_lee_expedientes_de_ambas_sedes (test_unidad.LecturaExpedientes.test_tc03_admin_lee_expedientes_de_ambas_sedes) ... ok
test_tc04a_estudiante_no_lee_expediente_ajeno (test_unidad.LecturaExpedientes.test_tc04a_estudiante_no_lee_expediente_ajeno) ... ok
test_tc04b_docente_no_lee_expediente_de_otra_sede (test_unidad.LecturaExpedientes.test_tc04b_docente_no_lee_expediente_de_otra_sede) ... ok
test_tc02_docente_actualiza_nota_en_su_sede (test_unidad.ModificacionNotas.test_tc02_docente_actualiza_nota_en_su_sede) ... ok
test_tc05_docente_no_modifica_nota_de_otra_sede (test_unidad.ModificacionNotas.test_tc05_docente_no_modifica_nota_de_otra_sede) ... ok
test_tc08_estudiante_y_admin_no_modifican_notas (test_unidad.ModificacionNotas.test_tc08_estudiante_y_admin_no_modifican_notas) ... ok
test_tc06_sesion_revocada_no_lee_ni_modifica (test_unidad.Sesiones.test_tc06_sesion_revocada_no_lee_ni_modifica) ... ok
test_tc07_sesion_vencida_no_lee_ni_modifica (test_unidad.Sesiones.test_tc07_sesion_vencida_no_lee_ni_modifica) ... ok
test_token_desconocido_o_vacio_es_rechazado (test_unidad.Sesiones.test_token_desconocido_o_vacio_es_rechazado) ... ok
test_tc10_limites_0_y_100_son_aceptados (test_unidad.ValidacionNota.test_tc10_limites_0_y_100_son_aceptados) ... ok
test_tc11_valores_fuera_de_rango_o_no_numericos_se_rechazan (test_unidad.ValidacionNota.test_tc11_valores_fuera_de_rango_o_no_numericos_se_rechazan) ... ok

----------------------------------------------------------------------
Ran 25 tests in 0.133s

OK

## Ejecucion limpia 2 (sin __pycache__)
$ python3 -m unittest discover -s tests -v
test_ruta_inexistente_devuelve_404 (test_api.ApiExpedientes.test_ruta_inexistente_devuelve_404) ... ok
test_salud_responde_sin_credenciales (test_api.ApiExpedientes.test_salud_responde_sin_credenciales) ... ok
test_tc01_api_estudiante_lee_expediente_propio (test_api.ApiExpedientes.test_tc01_api_estudiante_lee_expediente_propio) ... ok
test_tc04_api_estudiante_no_lee_expediente_ajeno (test_api.ApiExpedientes.test_tc04_api_estudiante_no_lee_expediente_ajeno) ... ok
test_tc05_api_docente_no_modifica_nota_de_otra_sede (test_api.ApiExpedientes.test_tc05_api_docente_no_modifica_nota_de_otra_sede) ... ok
test_tc06_api_sesion_revocada_pierde_acceso (test_api.ApiExpedientes.test_tc06_api_sesion_revocada_pierde_acceso) ... ok
test_tc07_api_sesion_vencida_o_ausente_es_rechazada (test_api.ApiExpedientes.test_tc07_api_sesion_vencida_o_ausente_es_rechazada) ... ok
test_tc09_api_entrada_invalida_devuelve_400_sin_cambios (test_api.ApiExpedientes.test_tc09_api_entrada_invalida_devuelve_400_sin_cambios) ... ok
test_tc11_api_nota_fuera_de_rango_no_se_persiste (test_api.ApiExpedientes.test_tc11_api_nota_fuera_de_rango_no_se_persiste) ... ok
test_tc12_api_limite_de_tamano_del_cuerpo (test_api.ApiExpedientes.test_tc12_api_limite_de_tamano_del_cuerpo) ... ok
test_tc12b_api_content_length_negativo_se_rechaza (test_api.ApiExpedientes.test_tc12b_api_content_length_negativo_se_rechaza) ... ok
test_sec07_auditoria_registra_usuario_y_no_guarda_tokens (test_unidad.Auditoria.test_sec07_auditoria_registra_usuario_y_no_guarda_tokens) ... ok
test_docente_lee_expediente_de_su_sede (test_unidad.LecturaExpedientes.test_docente_lee_expediente_de_su_sede) ... ok
test_tc01_estudiante_lee_expediente_propio (test_unidad.LecturaExpedientes.test_tc01_estudiante_lee_expediente_propio) ... ok
test_tc03_admin_lee_expedientes_de_ambas_sedes (test_unidad.LecturaExpedientes.test_tc03_admin_lee_expedientes_de_ambas_sedes) ... ok
test_tc04a_estudiante_no_lee_expediente_ajeno (test_unidad.LecturaExpedientes.test_tc04a_estudiante_no_lee_expediente_ajeno) ... ok
test_tc04b_docente_no_lee_expediente_de_otra_sede (test_unidad.LecturaExpedientes.test_tc04b_docente_no_lee_expediente_de_otra_sede) ... ok
test_tc02_docente_actualiza_nota_en_su_sede (test_unidad.ModificacionNotas.test_tc02_docente_actualiza_nota_en_su_sede) ... ok
test_tc05_docente_no_modifica_nota_de_otra_sede (test_unidad.ModificacionNotas.test_tc05_docente_no_modifica_nota_de_otra_sede) ... ok
test_tc08_estudiante_y_admin_no_modifican_notas (test_unidad.ModificacionNotas.test_tc08_estudiante_y_admin_no_modifican_notas) ... ok
test_tc06_sesion_revocada_no_lee_ni_modifica (test_unidad.Sesiones.test_tc06_sesion_revocada_no_lee_ni_modifica) ... ok
test_tc07_sesion_vencida_no_lee_ni_modifica (test_unidad.Sesiones.test_tc07_sesion_vencida_no_lee_ni_modifica) ... ok
test_token_desconocido_o_vacio_es_rechazado (test_unidad.Sesiones.test_token_desconocido_o_vacio_es_rechazado) ... ok
test_tc10_limites_0_y_100_son_aceptados (test_unidad.ValidacionNota.test_tc10_limites_0_y_100_son_aceptados) ... ok
test_tc11_valores_fuera_de_rango_o_no_numericos_se_rechazan (test_unidad.ValidacionNota.test_tc11_valores_fuera_de_rango_o_no_numericos_se_rechazan) ... ok

----------------------------------------------------------------------
Ran 25 tests in 0.132s

OK

## Servidor y pruebas manuales (README, seccion Ejecutar el servidor)
$ python3 servidor.py &
$ curl.exe http://127.0.0.1:8765/health   (como esta en el README)
bash: curl.exe: command not found
(dificultad D-2: 'curl.exe' no existe en Linux; se usa curl)
$ sh ../evidencias/pruebas_manuales.sh

### PM-01 salud
$ curl http://127.0.0.1:8765/health
{"estado": "laboratorio"}
HTTP 200

### PM-02 estudiante lee su expediente (permitido)
$ curl -H Authorization: Bearer lab-ana http://127.0.0.1:8765/expedientes/101
{"id": "101", "estudiante": "ana", "sede": "Central", "nota": 82}
HTTP 200

### PM-03 estudiante lee expediente ajeno de otra sede (denegado)
$ curl -H Authorization: Bearer lab-ana http://127.0.0.1:8765/expedientes/202
{"error": "Acceso denegado"}
HTTP 403

### PM-04 docente Central cambia nota en Pacifico (denegado)
$ curl -X POST -H Authorization: Bearer lab-maria -H Content-Type: application/json -d {"nota":10} http://127.0.0.1:8765/expedientes/202/nota
{"error": "Acceso denegado"}
HTTP 403

### PM-05 nota fuera de rango 150 (entrada invalida)
$ curl -X POST -H Authorization: Bearer lab-maria -H Content-Type: application/json -d {"nota":150} http://127.0.0.1:8765/expedientes/101/nota
{"error": "Nota inválida"}
HTTP 400

### PM-06 JSON malformado (entrada invalida)
$ curl -X POST -H Authorization: Bearer lab-maria -H Content-Type: application/json -d {nota: http://127.0.0.1:8765/expedientes/101/nota
{"error": "JSON inválido"}
HTTP 400

### PM-07 administrador intenta cambiar nota (denegado)
$ curl -X POST -H Authorization: Bearer lab-admin -H Content-Type: application/json -d {"nota":99} http://127.0.0.1:8765/expedientes/101/nota
{"error": "Acceso denegado"}
HTTP 403

### PM-08 sesion vencida (rechazada)
$ curl -H Authorization: Bearer lab-vencida http://127.0.0.1:8765/expedientes/101
{"error": "No autenticado"}
HTTP 401

### PM-09 sin credenciales (rechazado)
$ curl http://127.0.0.1:8765/expedientes/101
{"error": "No autenticado"}
HTTP 401

### PM-10 docente Central actualiza nota propia sede (permitido)
$ curl -X POST -H Authorization: Bearer lab-maria -H Content-Type: application/json -d {"nota":85} http://127.0.0.1:8765/expedientes/101/nota
{"id": "101", "estudiante": "ana", "sede": "Central", "nota": 85}
HTTP 200

### PM-11 revocar sesion de Ana
$ curl -X POST -H Authorization: Bearer lab-ana http://127.0.0.1:8765/sesiones/revocar
{"mensaje": "Sesión revocada"}
HTTP 200

### PM-12 lectura con sesion revocada (rechazada)
$ curl -H Authorization: Bearer lab-ana http://127.0.0.1:8765/expedientes/101
{"error": "No autenticado"}
HTTP 401

### PM-13 administrador lee expediente de Pacifico (permitido)
$ curl -H Authorization: Bearer lab-admin http://127.0.0.1:8765/expedientes/202
{"id": "202", "estudiante": "luis", "sede": "Pacifico", "nota": 91}
HTTP 200

### PM-14 Content-Length negativo (rechazado)
$ curl -X POST -H Authorization: Bearer lab-maria -H Content-Length: -1 http://127.0.0.1:8765/expedientes/101/nota
{"error": "Longitud inválida"}
HTTP 400

### PM-15 nota de Pacifico intacta tras los intentos rechazados
$ curl -H Authorization: Bearer lab-pedro http://127.0.0.1:8765/expedientes/202
{"id": "202", "estudiante": "luis", "sede": "Pacifico", "nota": 91}
HTTP 200

# servidor detenido
