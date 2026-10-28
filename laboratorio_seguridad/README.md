# Laboratorio local: seguridad de expedientes académicos (v1.0.0)

Material didáctico, **no apto para producción**. Ejecutar solo en `127.0.0.1` con datos y tokens ficticios. La autenticación por token es simulada.

## Entorno

- Python 3.10 o superior (probado con 3.14.0) y biblioteca estándar. No hay que instalar paquetes.
- `curl` o PowerShell para las pruebas manuales (opcional).

## Ejecutar las pruebas

Desde la carpeta `laboratorio_seguridad`:

```
python -m unittest discover -s tests -v
```

Resultado esperado: `Ran 25 tests ... OK` (14 de unidad en `tests/test_unidad.py` y 11 de integración con la API en `tests/test_api.py`). Cada prueba crea su propio estado sintético, por lo que no hay que restablecer nada entre ejecuciones.

## Ejecutar el servidor y probar la API

```
python servidor.py
curl.exe http://127.0.0.1:8765/health
curl.exe -H "Authorization: Bearer lab-ana" http://127.0.0.1:8765/expedientes/101
curl.exe -H "Authorization: Bearer lab-ana" http://127.0.0.1:8765/expedientes/202
curl.exe -X POST -H "Authorization: Bearer lab-maria" -H "Content-Type: application/json" -d "{\"nota\":85}" http://127.0.0.1:8765/expedientes/101/nota
curl.exe -X POST -H "Authorization: Bearer lab-ana" http://127.0.0.1:8765/sesiones/revocar
```

Detener con CTRL+C. Para restablecer los datos y sesiones sintéticos, detener el servidor y volver a ejecutarlo. La secuencia completa de pruebas manuales está en `../evidencias/pruebas_manuales.sh` (requiere el servidor activo; usar `sh` o Git Bash).

## Actores sintéticos

| Actor | Token | Sede | Lectura | Cambio de nota |
| --- | --- | --- | --- | --- |
| Ana, estudiante | `lab-ana` | Central | Solo expediente 101 | No |
| Luis, estudiante | `lab-luis` | Pacifico | Solo expediente 202 | No |
| María, docente | `lab-maria` | Central | Su sede | Su sede |
| Pedro, docente | `lab-pedro` | Pacifico | Su sede | Su sede |
| Admin | `lab-admin` | Global | Ambas sedes | No |
| Sesión vencida | `lab-vencida` | Central | No | No |

Códigos: `200` permitido, `400` entrada inválida, `401` sesión ausente, revocada o vencida, `403` acceso denegado, `404` recurso inexistente, `413` cuerpo mayor a 1024 bytes.

## Estructura del repositorio

- `laboratorio_seguridad/src/lab.py`: lógica de negocio y políticas de acceso.
- `laboratorio_seguridad/servidor.py`: API HTTP local.
- `laboratorio_seguridad/tests/`: pruebas de unidad e integración.
- `evidencias/`: registros rojo-verde-refactor, ejecuciones limpias, pruebas manuales y SAST. `evidencias/run.sh <archivo> <etiqueta>` ejecuta la suite y guarda el registro.
- `matriz_trazabilidad.csv`, `casos_prueba.csv`, `hallazgos.csv`: anexos del informe.
- `informe_seguridad.pdf`: informe técnico.
