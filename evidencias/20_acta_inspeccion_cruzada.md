# Acta de inspección cruzada

| Campo | Registro |
| --- | --- |
| Autor del código y de las pruebas | Andrey Alonso Hernández Salazar |
| Revisor (persona distinta del autor) | Javier Alejandro Mendoza Gonzalez |
| Fecha | 2026-10-30 |
| Versión inspeccionada | v1.0.0, commit `216e80c` (clon limpio de `main`) |
| Objetos inspeccionados | (1) Política de acceso: `puede_leer` y `puede_modificar` en `src/lab.py` y su aplicación en `servidor.py`. (2) Caso TC-05 (docente no modifica nota de otra sede) en `tests/test_unidad.py` y `tests/test_api.py`. (3) Caso TC-11 (notas inválidas y de frontera) en `tests/test_unidad.py` y `tests/test_api.py`. |
| Método | Lectura del código sin ejecutarlo (SAST manual), sondeos HTTP dinámicos y mutaciones manuales de `src/lab.py`. Los comandos se ejecutaron mediante un asistente de IA (Claude Code) en la máquina del revisor; el revisor valida los resultados. |
| Evidencia | `18_pruebas_mutacion.txt`, `19_sondeos_inspeccion.txt` |

## Política de acceso

Resultado: la política es de denegación por defecto y coincide con la tabla de roles del enunciado.

- `puede_leer`: administrador siempre; docente solo si `expediente["sede"] == usuario["sede"]`; estudiante solo si `expediente["estudiante"] == usuario["id"]`; cualquier otro rol devuelve `False`.
- `puede_modificar`: solo `docente` con la misma sede; estudiante, administrador y roles desconocidos devuelven `False`.
- `actualizar_nota` comprueba la autorización antes de validar la nota, por lo que un usuario no autorizado recibe 403 aunque envíe un valor inválido y no obtiene información sobre la validación.
- La respuesta 403 se construye con una función aparte y no incluye datos del expediente.

## Revisión de las pruebas (TC-05 y TC-11)

| Pregunta | TC-05 | TC-11 |
| --- | --- | --- |
| ¿Comprueba el efecto sobre los datos? | Sí: verifica que la nota 91 de 202 sigue intacta y que el cuerpo no contiene `nota` | Sí: verifica 400, que el cuerpo no contiene `nota` y que la nota 82 sigue intacta |
| ¿Es independiente? | Sí en unidad (`estado_inicial()` en `setUp`). En API reasigna el atributo de clase `ManejadorSilencioso.estado` en cada prueba (ver OB-5) | Sí: cada subprueba reinicia `estado_inicial()` (corrección de F-01) |
| ¿Puede fallar cuando el control falla? | Sí: las mutaciones M1 y M7 la hacen fallar en unidad y en API | Sí: M3 y M4 la hacen fallar; M4 solo en unidad (ver OB-6) |

Resumen de mutaciones (`18_pruebas_mutacion.txt`): 8 de 8 mutaciones detectadas; la línea base y la ejecución tras restaurar el código aprueban 25 de 25 pruebas.

## Observaciones

| ID | Severidad | Observación | Acción tomada | Registro |
| --- | --- | --- | --- | --- |
| OB-1 | Baja | 404 (no existe) frente a 403 (existe, sin permiso) permite enumerar ids. Reproducido con lab-ana en 999 y 202. | Se confirma el riesgo residual aceptado | O-01 |
| OB-2 | Baja | `POST /expedientes/101/x/nota` se procesa como actualización de 101 (la nota pasó de 82 a 55). | Registrada; mejora recomendada: comparar segmentos de forma exacta | O-04 |
| OB-3 | Baja | Sin token y con JSON malformado, el servidor responde 400 en lugar de 401: el cuerpo se procesa antes de autenticar. | Registrada; mejora recomendada: autenticar antes de leer el cuerpo | O-05 |
| OB-4 | Baja | La bitácora no registra intentos con sesión inválida ni revocaciones; SEC-07 solo exige las lecturas y modificaciones autenticadas, por lo que se cumple. | Registrada; mejora recomendada | O-06 |
| OB-5 | Baja | Las pruebas de API comparten el atributo de clase `ManejadorSilencioso.estado` y TC-12b depende de un tiempo máximo de 3 s. | Riesgo residual aceptado: la suite es secuencial | O-08 |
| OB-6 | Baja | A nivel de API, TC-11 solo envía -1 y 101; booleanos y 100.01 solo se verifican en la prueba de unidad. | Registrada; mejora recomendada: ampliar los valores en `test_api` | O-07 |

No se encontraron vulnerabilidades de severidad media, alta o crítica en la política de acceso inspeccionada. Los ajustes de código quedan fuera de esta acta; no se modificó ninguna aserción.
