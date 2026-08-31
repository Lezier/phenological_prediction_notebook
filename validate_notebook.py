"""Validación estructural CP14 sin entrenamiento ni acceso a red."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path


RAIZ = Path(__file__).resolve().parent
RUTA_NOTEBOOK = RAIZ / "phenological_prediction_colab.ipynb"
COMMIT_RC3 = "253358e75ac6bf72333d358251613473f59961ee"


def sha256_texto_lf(ruta: Path) -> str:
    return hashlib.sha256(ruta.read_bytes().replace(b"\r\n", b"\n")).hexdigest().upper()


def main() -> None:
    notebook = json.loads(RUTA_NOTEBOOK.read_text(encoding="utf-8"))
    fuente_rc = json.loads((RAIZ / "SOURCE_RC.json").read_text(encoding="utf-8"))
    datos = json.loads((RAIZ / "DATA_MANIFEST.json").read_text(encoding="utf-8"))
    version = (RAIZ / "VERSION").read_text(encoding="utf-8").strip()

    assert notebook["nbformat"] == 4
    assert len(notebook["cells"]) == 16
    assert version == "0.1.0-notebook.6"
    assert fuente_rc["version"] == "0.1.0-rc.3"
    assert fuente_rc["commit"] == COMMIT_RC3
    assert datos["commit_fuente"] == COMMIT_RC3

    codigo, todo = [], []
    for indice, celda in enumerate(notebook["cells"], start=1):
        fuente = "".join(celda["source"])
        todo.append(fuente)
        if celda["cell_type"] == "code":
            ast.parse(fuente, filename=f"celda_{indice}")
            assert celda.get("execution_count") is None
            assert celda.get("outputs", []) == []
            codigo.append(fuente)
    contenido = "\n".join(todo)
    contenido_codigo = "\n".join(codigo)

    requeridos = [
        "urlretrieve", "sha256_texto_lf", "StratifiedGroupKFold",
        "identificador_fold", "fold_id", "balanced_explicito",
        "asignacion_folds.csv", "pesos_clase_por_fold.csv",
        "tiempos_por_fold.csv", "perf_counter", "RandomForestClassifier",
        "comparacion_consolidada.csv", "random_forest_a_colab.joblib",
        "probabilidades_calibradas", COMMIT_RC3,
    ]
    faltantes = [texto for texto in requeridos if texto not in contenido_codigo]
    assert not faltantes, f"Faltan componentes RC3: {faltantes}"

    prohibidos = ["drive.mount", "MyDrive", "DRIVE_PROJECT_ROOT", "C:\\Users\\", "C:\\dev\\"]
    encontrados = [texto for texto in prohibidos if texto.lower() in contenido.lower()]
    assert not encontrados, f"Persisten rutas o dependencias privadas: {encontrados}"
    patrones_secretos = [r"ghp_[A-Za-z0-9]{20,}", r"AIza[0-9A-Za-z_-]{20,}", r"-----BEGIN .*PRIVATE KEY-----"]
    assert not any(re.search(patron, contenido) for patron in patrones_secretos)

    for item in datos["archivos"]:
        ruta = RAIZ / item["ruta"]
        assert ruta.exists(), f"Falta {ruta}"
        assert sha256_texto_lf(ruta) == item["sha256"]

    print(
        f"Notebook CP14 válido: {len(notebook['cells'])} celdas, "
        f"{len(codigo)} de código, 2 CSV verificados."
    )


if __name__ == "__main__":
    main()
