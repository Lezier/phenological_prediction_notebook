# Notebook reproducible para Google Colab

Proyecto complementario del release candidate privado
`phenological_prediction` `0.1.0-rc.2`, commit
`96b4e94687e8ff0aa7f904509ec0c2cdb4f0751d`.

## Runtime requerido

El notebook exige **CPython 3.13** antes de instalar dependencias. La primera
celda se detiene con un mensaje explícito si Colab entrega otro intérprete.
Las versiones fijadas disponen de wheels compatibles con CPython 3.13; la
instalación usa `--only-binary=:all:` para evitar compilaciones locales y luego
comprueba que cada distribución quedó en la versión esperada. SciPy se fija de
forma explícita porque scikit-learn depende de ella; no se deja a la resolución
transitiva de `pip`.

La celda exige un único reinicio limpio por runtime, haya sido necesario
instalar paquetes o no. Registra un marcador temporal en `/content`, reinicia
deliberadamente el kernel y, tras la reconexión, comprueba versiones y binarios
antes de continuar. Esto evita mezclar en memoria módulos preinstalados por
Colab con archivos reemplazados. El marcador evita un ciclo de reinicios.

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
5. Si la primera ejecución instala paquetes, esperar el reinicio automático,
   reconectar y seleccionar **Ejecutar todo** nuevamente.
6. Confirmar que la celda informa `Python 3.13` y seis versiones aprobadas.
7. Autorizar el montaje de Drive cuando Google lo solicite.
8. Conservar la carpeta de ejecución indicada por la última celda.

### Error `_slice` de NumPy

Si se usó una versión anterior del notebook y aparece
`cannot import name '_slice' from numpy._core.umath`, reiniciar la sesión de
Colab, reemplazar el notebook por `0.1.0-notebook.5` y ejecutar todo. No se
soluciona reinstalando repetidamente dentro del mismo kernel dañado.

Antes de importar bibliotecas en el kernel principal, la celda ejecuta una
prueba de salud en un proceso Python separado que importa NumPy, SciPy,
scikit-learn, pandas, Matplotlib, joblib y TensorFlow. Si esa prueba falla,
reinstala el conjunto completo y reinicia el kernel.

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
