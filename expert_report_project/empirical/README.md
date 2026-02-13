Plan empírico — Tareas iniciales

Objetivo: probar identificabilidad y desempeño de estimadores (IPTW, TMLE, DML, estimadores proximales) en datasets públicos usados en literatura causal.

Datasets propuestos:
- IHDP (infant health development program) — ampliamente usado en benchmarks de causal inference.
- LaLonde (NSW vs observational) — clásico para evaluación de métodos de emparejamiento/PS.
- Twins (semi-synthetic) — para evaluación con contrafactuales observadas en pares idénticos.
- ACIC / Atlantic Causal Inference Conference datasets (simulados y semisimulados) — para competencias.

Scripts:
- `data_prep.py` descarga/normaliza datasets y produce CSVs listos para análisis.

Siguientes pasos:
1. Ejecutar `data_prep.py` y verificar acceso a URLs de los datasets.
2. Implementar notebooks de análisis con `econml`, `causalml`, `DoubleML`, `zEpid` o `DoWhy` según necesidad.
