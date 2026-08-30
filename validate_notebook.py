"""Validación estructural que no ejecuta entrenamiento ni accede a Drive."""

from __future__ import annotations

import ast
import json
from pathlib import Path


RAIZ = Path(__file__).resolve().parent
RUTA_NOTEBOOK = RAIZ / "phenological_prediction_colab.ipynb"


def main() -> None:
    notebook = json.loads(RUTA_NOTEBOOK.read_text(encoding="utf-8"))
    assert notebook["nbformat"] == 4
    assert len(notebook["cells"]) >= 8

    codigo = []
    for indice, celda in enumerate(notebook["cells"], start=1):
        if celda["cell_type"] != "code":
            continue
        fuente = "".join(celda["source"])
        ast.parse(fuente, filename=f"celda_{indice}")
        codigo.append(fuente)

    contenido = "\n".join(codigo)
    requeridos = [
        "drive.mount",
        "sha256_texto_lf",
        "StratifiedGroupKFold",
        "RandomForestClassifier",
        "'scipy': '1.18.1'",
        "prueba_stack",
        "MARCADOR_REINICIO",
        "EJECUTAR_COMPARACION_COMPLETA",
        "comparacion_consolidada.csv",
        "random_forest_a_colab.joblib",
        "Probabilidades estimadas (no calibradas)",
    ]
    faltantes = [texto for texto in requeridos if texto not in contenido]
    assert not faltantes, f"Faltan componentes: {faltantes}"
    print(f"Notebook válido: {len(notebook['cells'])} celdas; {len(codigo)} de código.")


if __name__ == "__main__":
    main()
