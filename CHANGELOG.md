# Changelog

## 0.1.0-notebook.7 - 2026-08-31

- Genera `manifest_ejecucion.json` con ruta, tamaño y SHA-256 de cada archivo.
- Verifica nuevamente todos los artefactos antes de comprimirlos.
- Empaqueta datos, resultados y modelo en un ZIP por ejecución.
- Muestra hash y tamaño del ZIP e inicia su descarga mediante
  `google.colab.files.download()` sin depender de Google Drive.

## 0.1.0-notebook.6 - 2026-08-31

- Migra la fuente técnica a Python RC3, commit
  `253358e75ac6bf72333d358251613473f59961ee`.
- Incluye los dos CSV públicos bajo CC BY-NC 4.0 y verifica sus hashes antes
  de procesarlos.
- Elimina Google Drive como dependencia obligatoria y cualquier ruta personal.
- Alinea folds compartidos, pesos calculados solo con train, medición de
  tiempos, dispersión, parámetros y procedencia con RC3.
- Actualiza el paquete Random Forest A al esquema 2 y declara probabilidades
  no calibradas.
- Limpia todas las salidas históricas del notebook.
- Añade licencia, procedencia, manifiesto de datos y validación estructural.

## 0.1.0-notebook.5 - 2026-08-30

- Línea base ejecutada en Colab con almacenamiento privado en Google Drive.
