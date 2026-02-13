# Proposal v2 — Marco causal unificado (Actualizado)

## Resumen ejecutivo
Versión revisada con: (i) formalización del estimand y población objetivo; (ii) ampliación de la revisión bibliográfica y lagunas detectadas; (iii) roadmap empírico y pre-registro de robustez.

## Pregunta de investigación y estimand (formal)
- Pregunta: ¿Cuál es el efecto causal de la intervención $X$ (cambio de $x_0$ a $x_1$) sobre el desenlace $Y$ en la población objetivo $P$?

- Notación: denotemos $Y(x)$ el resultado potencial cuando la unidad recibe $X=x$. Sea $A$ la variable de asignación observada, $Z$ el conjunto de confusores observados, $U$ confusores no observados, y $V$ covariables de estratificación para heterogeneidad.

- Estimands posibles (seleccionar y documentar uno en el manuscrito):
  - ATE (Average Treatment Effect):

  $$
  ATE = E[Y(x_1) - Y(x_0)] = E[Y\mid do(X=x_1)] - E[Y\mid do(X=x_0)].
  $$

  - ATT (Average Treatment effect on the Treated):

  $$
  ATT = E[Y(x_1) - Y(x_0) \mid A=1].
  $$

  - CATE (Conditional ATE given $V=v$):

  $$
  CATE(v) = E[Y(x_1)-Y(x_0) \mid V=v].
  $$

  - Path-specific or mediated effects (si interesa distinguir vías): definir usando contrafactuales anidados y seguir la notación de Pearl/Robins según sea necesario.

- Población objetivo: especificar claramente la población (ej., población del estudio observacional, población transportada, o población objetivo policy-relevant). Indicar si se aspira a transportabilidad y bajo qué supuestos.

- Supuestos de identificación (declarar y justificar):
  - SUTVA / consistencia.
  - Positividad: $P(X=x\mid Z=z)>0$ para valores de $z$ con $P(Z=z)>0$.
  - Intercambiabilidad condicional (no confounding condicionado a $Z$):

  $$
  Y(x) \perp\!\!\perp X \mid Z.
  $$

  - Si hay proxies o variables instrumentales, documentar los supuestos adicionales (validez de IV, independencia, exclusión).

- Identificación vía back-door (si aplica): si $Z$ satisface el criterio back-door entonces

  $$
  E[Y\mid do(X=x)] = E_Z[E[Y\mid X=x, Z=z]].
  $$

  Indicar alternativa front-door o identificación proximal si el back-door no es viable.

## Diagrama causal (DAG) y supuestos de identificación — detalle operativo

- Incluir una figura DAG principal (archivo sugerido: `figures/DAG_main.svg` o `figures/DAG_main.png`) con nodos: `X` (tratamiento), `Y` (outcome), `Z` (confusores observados), `U` (confusores no observados), `P` (proxies), `M` (mediadores) y `S` (selección) cuando aplique. En la leyenda indique qué flechas se asumen ausentes.

- Breve ejemplo de derivación por do-calculus (cuando aplica back-door): si $Z$ bloquea todos los back-door paths entre $X$ y $Y$, entonces

  $$
  P(Y\mid do(X=x)) \overset{(1)}{=} P(Y\mid X=x, do(Z)) \overset{(2)}{=} \sum_z P(Y\mid X=x, Z=z)P(Z=z),
  $$

  donde (1) denota la aplicación del ajuste por $Z$ (regla de back-door) y (2) la ley de la probabilidad total; escribir en el apéndice 2–4 líneas que muestran por qué las condiciones de independencia implican la igualdad (p. ej. usando la regla 2 de do-calculus o la definición de independencia condicional).

- Si se usa front-door o proximal identification, incluya el esquema de variables y la identidad identificante correspondiente (preferible en apéndice con referencias a Pearl y a la literatura proximal).

## Análisis de sensibilidad (texto a incluir en métodos)

- Incluir al menos dos análisis de sensibilidad pre-especificados:
  1. E-value (VanderWeele): calcule el E-value para el estimador puntual primario y reporte en tabla la magnitud mínima de asociación de un confusor no observado con $X$ y $Y$ necesaria para explicar el efecto.
  2. Rosenbaum bounds / tipping‑point: analice qué combinación de prevalencia y fuerza del confusor no observado reduce el efecto a nulidad; presente una tabla/tres escenarios (conservador/moderado/optimista).

- Añadir una breve sección que explique cómo interpretar fallos en los tests de independencia implícitos por el DAG (p. ej., si $Y \not\perp\!\!\perp X \mid Z$ en datos observados, discutir implicaciones para identificación y presentar análisis alternativos).

- Incluir un gráfico/tabla de robustez que muestre estimadores primarios/secundarios (TMLE/IPTW/DML) bajo: (i) distintos sets de covariables $Z$, (ii) trimming de pesos, y (iii) distintos learners para DML.


## Revisión bibliográfica (ampliada) — lagunas y prioridades de búsqueda
- Categorías a cubrir (prioridad):
  1. Métodos semiparamétricos y TMLE: avances prácticos, variance estimation y ajuste con SuperLearner.
  2. DML / orthogonal ML estimators: teoría reciente sobre tasas de convergencia y aplicabilidad en alta dimensión (Chernozhukov, Wager, Athey y coautores).
  3. Proximal causal inference: condiciones para identificar con proxies y aplicaciones empíricas (Tchetgen y colaboradores).
  4. Sensitivity analysis: E-values, Rosenbaum bounds, y métodos bayesianos para MNAR.
  5. Transportability / external validity: Bareinboim, Pearl; métodos prácticos para adaptar estimandos a poblaciones distintas.
  6. Causal inference en series temporales y dinámicas (Asesh y literatura más reciente).
  7. Benchmarks y datasets usados en la literatura (IHDP, ACIC, LaLonde, Twins) y comparativas de estimadores.

- Lagunas detectadas en el borrador actual:
  - Literatura posterior a 2015 está incompleta; realizar búsquedas explícitas en Web of Science/Scopus/Google Scholar para términos: "double machine learning", "targeted maximum likelihood", "proximal causal inference", "transportability causal", "E-value sensitivity".
  - Falta consolidación de benchmarks y estudios de referencia comparativos (recolectar ACIC competitions y papers reproducibles).

- Tareas concretas (acción):
  1. Ejecutar búsquedas (query sugeridas abajo) y compilar 30–50 referencias recientes (2015–2025) en `improved_proposal/references.bib`.
  2. Extraer 10 papers clave por categoría (métodos + aplicaciones) y resumir en 1–2 párrafos cada uno para el manuscrito.
  3. Incluir sección de "Related work" que distinga: (i) métodos de identificación; (ii) estimadores; (iii) validación/benchmarks; (iv) gaps abiertos que aborda este trabajo.

- Queries sugeridas para Google Scholar / Scopus (copiar/pegar):
  - "double machine learning treatment effect 2016..2025"
  - "targeted maximum likelihood estimation SuperLearner 2015..2025"
  - "proximal causal inference Tchetgen 2018..2025"
  - "transportability causal Bareinboim 2015..2025"

## Mapeo entre estimand e estimadores (pre-especificación)
- Si se elige ATE y back-door con $Z$ observados: IPTW (diagnóstico de pesos) y TMLE (estimador principal por robustez y eficiencia). Reportar ambos y Preferir TMLE como estimador primario si se pretende inferencia semiparamétrica.

- Si se busca heterogeneidad (CATE): emplear DML o causal forests / grf para estimación y validación por cross-fitting.

- Si se sospecha confusión no observada pero existen proxies válidos: especificar modelo proximal y estimador asociado; documentar supuestos sobre proxies.

## Checklist mínimo para formalizar en la versión final del manuscrito
1. Definir y declarar explícitamente el estimand (ATE/ATT/CATE).  
2. Especificar población objetivo y criterios de inclusión/exclusión.  
3. Incluir DAG(s) con variables observadas/no observadas y justificar criterio de identificación.  
4. Derivar la expresión identificante (p. ej. back-door formula) y listar supuestos formales.  
5. Pre-especificar estimador principal (TMLE recomendado) y estimadores secundarios (IPTW, DML).  
6. Pre-especificar tests de robustez y análisis de sensibilidad que se reportarán.  
7. Vincular cada chequeo de robustez a una amenaza concreta (e.g., $U$ confounder, selection bias, model misspecification).  

## Entregables inmediatos que generé
- `improved_proposal/proposal_v2.md` (este documento — formaliza estimand y plan de revisión bibliográfica).

## Siguientes pasos (sugeridos y de alta prioridad)
1. Ejecutar las búsquedas bibliográficas y crear `improved_proposal/references.bib` (yo puedo generar queries y compilar metadata; necesito permiso para acceso web o que pegues las cabeceras RIS/BibTeX si prefieres evitar web calls).  
2. Elegir el estimand final (ATE vs ATT vs CATE) y actualizar el manuscrito con la derivación identificante concreta y el DAG final.  
3. Implementar notebooks de estimación (`02_estimators.ipynb`) con TMLE y DML sobre IHDP y LaLonde (pipeline ya esbozado).  

---

Si quieres, empiezo ahora con (A) ejecutar las búsquedas y compilar `references.bib` localmente (necesita acceso web), o (B) generar la plantilla de `02_estimators.ipynb` con celdas de ejemplo para TMLE/IPTW/DML usando Python. ¿Cuál prefieres?  
