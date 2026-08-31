# Procedencia de los datos

## Archivos publicados

| Archivo | Filas | Contenido |
|---|---:|---|
| `data/base_fenologia_clima.csv` | 1.130 | Fenología y siete variables climáticas |
| `data/base_fenologia_clima_satelite.csv` | 1.130 | Base anterior más NDVI y metadatos satelitales |

Ambos archivos son copias verificadas del proyecto Python RC3, commit
`253358e75ac6bf72333d358251613473f59961ee`. Sus hashes están en
`DATA_MANIFEST.json` y se comprueban antes de cada ejecución en Colab.

## Linaje

1. Observaciones fenológicas de PEP725, exportación
   `PEP725_FranciscoLopezBrombley_20260817`.
2. Enriquecimiento climático derivado de NASA POWER.
3. Enriquecimiento satelital derivado de Copernicus Sentinel-2.
4. Construcción de dos snapshots consolidados.
5. Preparación reproducible de A (1.091 filas), A′ y B (657 filas) dentro del
   notebook, sin sobrescribir los CSV.

## Límite de reproducibilidad

El repositorio reproduce desde los snapshots consolidados. No reproduce bit a
bit la adquisición externa original porque el material heredado no conserva
todos los endpoints, versiones, fechas exactas e identificadores de producto.
