Simulated reviews (mock) — Proposal v2

Purpose: fast, actionable feedback synthesized from 6 high-evidence profiles in the project. Use as first-pass comments to improve the manuscript before real external review.

1) Judea Pearl — Focus: Identification / DAGs
- Major: The estimand and back-door formula are correctly stated, but the DAGs in `proposal_v2.md` should explicitly show assumed absence of selection on post-treatment variables and any measurement proxies; please add a labeled Figure with measured/unmeasured nodes.  
- Suggestion: Expand the do-calculus derivation for the most important identification claim (short algebraic steps).  
- Empirical check: include a directed test (conditional independence test) that the chosen $Z$ blocks back-door paths in observed data (report p-values / tests used).  
- References to cite: Pearl (2009) and a short pointer to graph-based independence testing (e.g., Spirtes & Glymour).  

2) Victor Chernozhukov — Focus: Inference, efficiency, DML
- Major: Recommend clarifying the estimators' asymptotic regimes — a short paragraph on required rates for nuisance estimation (SuperLearner/RFs) to ensure orthogonality for DML.  
- Suggestion: Pre-specify cross-fitting folds and hyperparameter tuning to avoid p‑hacking; include variance estimation method for DML (bootstrap vs analytic).  
- Empirical check: run DML with at least two different learners (RF + boosting) and show stability of point estimates.  
- Reference: Chernozhukov et al. (2018) on Double/debiased ML.

3) Eric Tchetgen Tchetgen — Focus: Proximal methods and proxies
- Major: If claiming identification via proxies, you must (i) state proxy validity assumptions explicitly, (ii) propose a prioritized list of candidate proxies in your datasets, and (iii) run a falsification (e.g., show proxy correlates with unobserved confounder surrogates if possible).  
- Suggestion: Add a short schematic on how proxies enter the estimating equations and which moments are used.  
- Empirical check: implement one proximal estimator on a synthetic scenario (in simulations) that violates/fulfills proxy assumptions to show sensitivity.  
- Reference: Tchetgen et al. (2019–2022 work on proximal inference).

4) Susan Athey (ML + heterogeneity) — Focus: CATE / ML workflows
- Major: If heterogeneity is a goal, add a brief pre-specification of CATE estimators (e.g., causal forests, grf) and how you will control multiple testing across subgroups.  
- Suggestion: Provide an explicit plan for honest estimation (sample splitting) and report calibration plots for predicted heterogeneity.  
- Empirical check: show one CATE plot (effect by quantile of propensity or by a strong moderator) from IHDP synthetic data as a demo.  
- Reference: Athey & Wager on causal forests; implement in appendix as optional analysis.

5) John Ioannidis — Focus: Validity, robustness and interpretation
- Major: Highlight risks of over-claiming causal certainty; add a short paragraph tempering claims, clearly labelling results as contingent on untestable assumptions and providing alternative interpretations.  
- Suggestion: Add a formal sensitivity bounding table (E-value + Rosenbaum) for the main estimate to show how robust findings are to unobserved confounding.  
- Empirical check: provide tipping-point analysis for effect size under plausible confounder scenarios.

6) Michael E. West — Focus: Design alternatives and applicability
- Major: For applied audiences, discuss when RCTs are preferred and when the proposed workflow is a valid substitute; practical guidance for choosing between DRPT/hybrid designs and the observational pipeline would be useful.  
- Suggestion: Add a short decision flowchart (1 page) indicating when to trust the observational estimate vs pursue better design.  
- Empirical check: include an example comparing observational estimate to a benchmark (if available) or a simulated RCT baseline.

Summary — prioritized actions to implement now (highest impact):
- Add a clear labeled DAG figure and short do-calculus derivation (Pearl).  
- Pre-specify DML implementation details (folds, learners) and run at least two learners for stability (Chernozhukov).  
- If claiming proxy-based identification, include explicit proxy assumptions and a proximal simulation (Tchetgen).  
- Add an honest CATE demo and calibration (Athey) if heterogeneity is a selling point.  
- Provide sensitivity analyses (E-value, Rosenbaum) and a tipping-point table (Ioannidis).  
- Add a short decision flowchart on when to apply the pipeline vs pursue experimental designs (West).

If you want, I can now (A) expand each simulated review into a fuller paragraph (1 page per reviewer) or (B) convert these action items into concrete edits to `proposal_v2.md` and the notebooks. Which do you prefer?  
