# Proposal v2 — Lengua Unificada para Especificar Preguntas Causales (Actualizado)

**Autores**: [Tu Nombre]  
**Fecha**: Febrero 12, 2026  
**Basado en feedback simulado de expertos**: Judea Pearl, Viktor Chernozhukov, Eric Tchetgen, Susan Athey, John Ioannidis, Michael West.

## Resumen Ejecutivo
Esta propuesta conceptual introduce una "lengua unificada" para especificar preguntas causales, integrando cuatro paradigmas: regresión de experimentos, modelos causales estructurales, causales de Pearl, y aprendizaje automático causal con IA. Surge de la necesidad de un curso sobre Razonamientos Causales que unifique estos abordajes, poco comunes en la literatura. La identificación y estimación permanecen paradigmáticas, pero la especificación se estandariza para facilitar la comunicación interdisciplinaria. Se busca publicación en revistas de causalidad (ej. Journal of Causal Inference, Epidemiology) o IA (Nature Machine Intelligence), adaptando el enfoque para maximizar aceptación. Versión revisada con formalización del estimand, ampliación bibliográfica, y roadmap empírico.

## Pregunta de Investigación y Estimand (Formal)
- Pregunta principal: ¿Es posible desarrollar una lengua unificada para formular preguntas causales que integre regresión experimental, modelos estructurales, do-calculus de Pearl, y ML/IA causal, permitiendo traducción entre paradigmas sin perder rigor?

- Pregunta secundaria (técnica): ¿Cuál es el efecto causal de la intervención $X$ (cambio de $x_0$ a $x_1$) sobre el desenlace $Y$ en la población objetivo $P$, especificado en la lengua unificada?

- Notación: Usamos la lengua unificada: "Efecto de X en Y dado Z" (traducible a ATE/ATT/CATE). Denotemos $Y(x)$ el resultado potencial. Sea $A$ asignación observada, $Z$ confusores observados, $U$ no observados, $V$ estratificación.

- Estimands posibles (seleccionar y documentar):
  - ATE: $ATE = E[Y(x_1) - Y(x_0)]$.
  - ATT: $ATT = E[Y(x_1) - Y(x_0) \mid A=1]$.
  - CATE: $CATE(v) = E[Y(x_1)-Y(x_0) \mid V=v]$.
  - Efectos mediados: Definir con contrafactuales.

- Población objetivo: Población del curso (estudiantes interdisciplinarios), o población policy-relevant para aplicaciones.

- Supuestos de identificación:
  - SUTVA.
  - Positividad.
  - Intercambiabilidad: $Y(x) \perp X \mid Z$.
  - Identificación vía back-door: $E[Y \mid do(X=x)] = E_Z[E[Y \mid X=x, Z=z]]$.

## Diagrama Causal (DAG) y Supuestos — Detalle Operativo
- Figura DAG: `figures/DAG_main.svg` con nodos X, Y, Z, U, P (proxies), M (mediadores). Lengua unificada facilita especificación de paths.

- Derivación do-calculus: Para back-door, $P(Y \mid do(X=x)) = \sum_z P(Y \mid X=x, Z=z) P(Z=z)$.

- Análisis de sensibilidad: E-values, Rosenbaum bounds; tabla de robustez con IPTW/TMLE/DML bajo distintos Z y trimming.

## Revisión Bibliográfica (Ampliada) — Lagunas y Prioridades
- Categorías (prioridad, integradas en lengua unificada):
  1. Regresión experimental: Baseline para especificación simple.
  2. Modelos estructurales: DAGs para traducción.
  3. Pearl: Do-calculus como núcleo.
  4. ML/IA causal: Estimación escalable.
  5. Benchmarks: IHDP, ACIC para validación.

- Feedback de expertos:
  - **Pearl**: "Unifica con do-calculus para rigor gráfico."
  - **Chernozhukov**: "Integra DML para robustez en ML."
  - **Tchetgen**: "Añade proxies para datos complejos."
  - **Athey**: "Facilita CATE en policy."
  - **Ioannidis**: "Valida con benchmarks para replicabilidad."
  - **West**: "Maneja dinámicas en IA."

- Lagunas: Falta marco unificado; literatura fragmentada.

- Tareas: Compilar 30 referencias (2015–2025) en `references.bib`; queries como "unified causal language" o específicas por paradigma.

## Mapeo entre Estimand y Estimadores (Pre-especificación)
- Lengua unificada traduce a estimadores: ATE → IPTW/TMLE; CATE → DML; proxies → proximal.

## Checklist Mínimo
1. Definir estimand en lengua unificada.
2. Especificar población.
3. Incluir DAG.
4. Derivar identificación.
5. Pre-especificar estimadores.
6. Análisis de sensibilidad.
7. Vincular robustez a amenazas.

## Entregables
- Esta propuesta adaptada.
- Perfiles de expertos.
- Análisis empíricos.

## Siguientes Pasos
1. Compilar referencias.
2. Desarrollar prototipo de lengua.
3. Simular revisiones para revistas objetivo.  
