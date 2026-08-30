# Notebook reproducible para Google Colab

Proyecto complementario del release candidate privado
`phenological_prediction` `0.1.0-rc.2`, commit
`96b4e94687e8ff0aa7f904509ec0c2cdb4f0751d`.

El notebook reproduce, desde los dos CSV consolidados, la preparación de A,
A' y B, la comparación entre red densa y Random Forest, el entrenamiento de
Random Forest A y una inferencia demostrativa. No reproduce la adquisición
original desde PEP725, NASA POWER o Sentinel-2.

## Privacidad y almacenamiento

Los datos no se incluyen en este proyecto. Antes de ejecutar, crear en Google
Drive la estructura:

```text
MyDrive/
`-- phenological_prediction_private/
    |-- data/
    |   |-- base_fenologia_clima.csv
    |   `-- base_fenologia_clima_satelite.csv
    `-- ejecuciones/
```

El notebook monta Drive, comprueba los hashes SHA-256 canónicos de ambos CSV,
copia los datos al almacenamiento temporal de Colab y crea una carpeta nueva
por ejecución. No sobrescribe corridas anteriores.

## Uso en Colab

1. Subir `phenological_prediction_colab.ipynb` a Google Drive.
2. Abrirlo con Google Colab usando la cuenta autorizada para los datos.
3. Revisar la celda **Configuración privada de Drive**. Solo modificar
   `DRIVE_PROJECT_ROOT` si se eligió otra ubicación.
4. Seleccionar **Entorno de ejecución > Ejecutar todo**.
5. Autorizar el montaje de Drive cuando Google lo solicite.
6. Conservar la carpeta de ejecución indicada por la última celda.

La comparación completa incluye TensorFlow y puede tardar. Para ensayar solo
la inferencia se puede cambiar `EJECUTAR_COMPARACION_COMPLETA` a `False`, pero
ese modo no constituye una reproducción de las métricas.

## Fuente técnica

`SOURCE_RC.json` identifica la versión, commit y hashes de los datos del RC.
El notebook no modifica ni sustituye la evidencia congelada. Una ejecución en
Colab es evidencia complementaria y debe registrar sus propias versiones,
fecha, parámetros, métricas y hashes.

## Archivos excluidos

`.gitignore` impide incorporar por accidente datos, modelos, resultados,
entornos virtuales y secretos. No escribir contraseñas ni tokens en el
notebook.

