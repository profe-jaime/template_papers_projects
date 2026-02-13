# Log de Procesamiento - Expertos en Causalidad
**Fecha:** $(date +%Y-%m-%d)

Este log resume la creación inicial de perfiles de expertos en causalidad a partir de causal.json.

## Investigadores incluidos (20 perfiles)

1. Judea Pearl – Inteligencia Artificial Causal
2. Peter Spirtes – IA / ML Causal (descubrimiento)
3. Clark Glymour – IA / ML Causal (descubrimiento)
4. Richard Scheines – IA / ML Causal (descubrimiento)
5. Michael E. West – Experimentación causal (alternativas a RCT)
6. John P. A. Ioannidis – Experimentación causal (comparación RCT vs no RCT)
7. Eric J. Tchetgen Tchetgen Bang – Inferencia causal (doble robustez)
8. James M. Robins – Inferencia causal (datos faltantes y doble robustez)
9. Stephen M. Marcus – Experimentación causal (DRPT)
10. Victor Chernozhukov – Inferencia causal (distribuciones contrafactuales)
11. Asesh – Machine Learning Causal en series temporales
12. Dan Geiger – IA Causal (mención nominal)
13. Thomas Verma – IA Causal (mención nominal)
14. Paul W. Holland – Inferencia causal (mención nominal)
15. Gregory Cooper – ML/IA Causal (ALARM, mención nominal)
16. Kenneth A. Bollen – Inferencia causal (mención nominal)
17. J. Whittaker – Modelos gráficos no dirigidos (mención nominal)
18. Christopher (Chris) Meek – IA Causal (axiomas en modelos dirigidos, mención)
19. Stephen E. Fienberg – IA Causal (seminario sobre modelos gráficos, mención)
20. Nancy Cartwright – Inferencia causal (crítica filosófica, mención)

## Progreso

- [x] Identificar investigadores desde causal.json
- [x] Crear carpeta profiles/causal
- [x] Generar perfiles iniciales en Markdown
- [ ] Revisar y enriquecer con datos adicionales desde Scite.ai (cuando haya API/consultas)
- [ ] Actualizar índice de conceptos para causalidad

## Limitaciones metodológicas

- Sin métricas bibliométricas verificadas (Scite.ai, Google Scholar): se respetan los valores null del archivo causal.json.
- No se completan afiliaciones actuales salvo cuando aparecen explícitamente en las referencias.
- No se añaden nuevos papers: cada perfil se basa solo en los títulos, DOIs y descripciones presentes en causal.json y sus referencias asociadas.

## Notas

Este log sirve como punto de partida. Cuando se integren consultas reales a Scite.ai, se recomienda:

- Actualizar secciones de "Producción científica" con más de un paper por autor.
- Añadir métricas (citaciones aproximadas, supporting/contrasting) donde haya datos verificables.
- Revisar niveles de evidencia para perfiles basados solo en menciones nominales.
