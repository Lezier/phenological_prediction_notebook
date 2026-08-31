# Predicción fenológica reproducible en Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Lezier/phenological_prediction_notebook/blob/main/phenological_prediction_colab.ipynb)

Port público del proyecto Python `phenological_prediction` **0.1.0-rc.3**,
commit `253358e75ac6bf72333d358251613473f59961ee`.

## Alcance

El notebook ejecuta un único flujo reproducible:

1. verifica Python 3.13 y las dependencias fijadas;
2. descarga desde este repositorio los dos CSV y valida sus SHA-256;
3. prepara A, A′ y B;
4. compara red densa y Random Forest con los mismos folds y pesos;
5. exporta métricas por fold, dispersión, tiempos, asignaciones, pesos y matrices;
6. entrena Random Forest A con 1.091 filas;
7. demuestra inferencia mediante siete variables climáticas;
8. genera un manifiesto de la ejecución.

No reproduce la adquisición original desde PEP725, NASA POWER o Sentinel-2.

## Ejecución

1. Abra el notebook con el botón **Open in Colab**.
2. Seleccione un runtime CPU con **Python 3.13**.
3. Ejecute todas las celdas.
4. Si la primera celda reinicia el kernel, reconecte y use **Ejecutar todo** otra vez.
5. Compruebe que la última celda muestre `CONTROLES APROBADOS`.

No se requiere Google Drive, token, credencial ni servicio de pago. Los
resultados se escriben temporalmente en `/content/phenological_prediction_run_*`.
CP15 incorporará su empaquetado y descarga directa como ZIP.

La comparación completa incluye TensorFlow y puede tardar. Cambiar
`EJECUTAR_COMPARACION_COMPLETA` a `False` permite probar el resto del flujo,
pero ese modo no reproduce las métricas oficiales.

La inferencia de la red se realiza invocando directamente el modelo con
`training=False`, en vez de crear repetidamente funciones de `predict()` dentro
del bucle. Esto reduce las advertencias de *retracing* observadas en la versión
anterior; si TensorFlow emite alguna advertencia residual, corresponde a coste
de compilación y no cambia el protocolo ni las métricas calculadas.

## Contrato RC3

- Fuente Python: `SOURCE_RC.json`.
- Identidad de los CSV: `DATA_MANIFEST.json`.
- Datos públicos: `data/`.
- Versión del notebook: `0.1.0-notebook.6`.
- Configuración: 5 folds, semilla 42, Random Forest de 400 árboles y baseline
  neuronal heredado.
- Evidencia principal: validación `StratifiedGroupKFold` por `s_id`.
- Modelo del prototipo: Random Forest A.
- Probabilidades: puntajes no calibrados.

## Validación sin entrenamiento

```powershell
python validate_notebook.py
```

La validación comprueba JSON, sintaxis de celdas, versión, commit fuente,
hashes de datos, ausencia de salidas históricas, rutas personales, Drive y
patrones básicos de secretos.

## Licencias y procedencia

- `DATA_LICENSE.md`: CC BY-NC 4.0, atribuciones y restricciones.
- `DATA_PROVENANCE.md`: linaje y límite de reproducción.
- `CODE_LICENSE.md`: situación del código; no existe licencia abierta concedida.

Uso experimental con datos europeos; no validado para operación en Chile y no
sustituye evaluación agronómica.
