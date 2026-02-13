# Proposal v1 — Marco causal unificado

## Resumen ejecutivo
Propuesta para estudiar el efecto causal de la intervención X sobre el resultado Y en contextos observacionales, combinando formalismo teórico (SCM, do-calculus) con estimadores robustos (TMLE, DML) y validación por simulación. Se incorporan referencias y enfoques de los perfiles en `profiles/causal` (Pearl, Hernán, Athey, Bareinboim, Tchetgen).

## Pregunta de investigación y estimand
- Pregunta: ¿Cuál es el efecto promedio causal de cambiar la variable de tratamiento $X$ de $x_0$ a $x_1$ sobre el desenlace $Y$ en la población objetivo? 
- Estimand: el efecto causal medio (ATE) definido como

$$
ATE = E[Y\mid do(X=x_1)] - E[Y\mid do(X=x_0)].
$$

Explicar explícitamente el poblacional objetivo y cualquier subpoblación de interés.

## Diagrama causal (DAG) y supuestos de identificación
- Construir un DAG que incluya: $X$ (tratamiento), $Y$ (resultado), $Z$ (confusores observados), $U$ (confusores no observados), $M$ (mediadores), y variables de selección $S$ si aplican.
- Indicar criterio de identificabilidad (back-door / front-door) y justificar por qué se puede usar: p.ej. si $Z$ satisface back-door, entonces

$$
E[Y\mid do(X=x)] = \sum_z E[Y\mid X=x, Z=z] P(Z=z).
$$

- Incluir chequeos: ausencia de colliders inducidos, definiciones de variables proxies y discusión de transportabilidad si la población difiere (usar conceptos de Bareinboim).

## Estrategia estimativa (pasos técnicos)
1. Preprocesamiento
   - Definir covariables $Z$ y criterios de comparación.
   - Tratar missing: imputación múltiple bajo MAR; plan de sensibilidad para MNAR.
2. Estimadores propuestos
   - Estándar: IPTW con pesos estabilizados; diagnóstico de balance (ASMD, love plots).
   - Robustez y eficiencia semiparamétrica: TMLE con estimadores iniciales basados en `SuperLearner` (ensemble de modelos) para mu_y(x,z) y e(x|z). TMLE update proporciona propiedades doble-robust y eficiencia local.
   - Alternativa con ML: Double/Debiased Machine Learning (DML) para estimar ATE con control de alta dimensionalidad y regularización.
   - Si existen confusores no observados pero proxies válidos, explorar proximal causal inference (Tchetgen et al.).
3. Análisis de sensibilidad
   - E-value y análisis de Rosenbaum para evaluar fuerza necesaria de confusor no observado para explicar efecto.
   - Simulaciones paramétricas y no paramétricas para evaluar sesgos bajo distintos escenarios de $U$ y selection bias.
4. Inferencia y error
   - Intervalos de confianza por bootstrap aleatorizado (para TMLE usar varianza del estimador influencia-function), y pruebas de hipótesis robustas.

## Plan de validación (simulación y falsificación)
- Diseñar 3 escenarios simulados: (A) confusión solo por $Z$ observada, (B) confusor no observado $U$ con correlación moderada, (C) selection bias/feedback. Comparar desempeño de IPTW, TMLE, DML y estimadores proxy.
- Implementar tests de falsificación: efectos en outcomes donde se espera nulidad; placebo tests por períodos o subgrupos.

## Implementación práctica (pasos reproducibles)
1. Repositorio y datos
   - Guardar scripts en `improved_proposal/` con notebooks para preprocesamiento, estimación (R/Python), y simulaciones.
2. Librerías recomendadas
   - R: `tmle`, `SuperLearner`, `MatchIt`, `survey`, `causaldrf`.
   - Python: `econml` (DML, TMLE experimental), `DoWhy`, `zepid`, `causalinference`.
3. Pipeline mínimo
   - `00_data_prep.ipynb` — carga, limpieza, imputación múltiple.
   - `01_dag_and_identification.md` — DAGs, supuestos, estimand.
   - `02_estimators.ipynb` — IPTW, TMLE, DML implementations and diagnostics.
   - `03_simulations.ipynb` — escenarios simulados y resultados.

## Referencias y notas de expertos (extractos)
- Judea Pearl — formalismo de $do(\cdot)$, do-calculus y criterios de identifiability.
- Miguel Hernán — diseño causal en epidemiología; recomendaciones sobre g-methods y análisis de sensibilidad en datos observacionales.
- Susan Athey — integración de ML y causalidad; invariance/transportability para transferir resultados.
- Elias Bareinboim — transportability y adaptación de causalidad entre dominios.
- Tchetgen (proximal methods) — inferencia con confusores no observados usando proxies.

## Entregables
- `improved_proposal/proposal_v1.md` (este documento)
- Notebooks y scripts listados en "Implementación práctica"
- Documento de validación con resultados de simulación y diagnóstico.

---

*Nota:* si quieres, puedo generar los notebooks iniciales (`00_data_prep.ipynb`, `02_estimators.ipynb`, `03_simulations.ipynb`) y los scripts de ejemplo en R o Python dentro de la carpeta creada. Para commits y PR necesito la ruta del repo Git asociado si quieres que realice `git` operations.