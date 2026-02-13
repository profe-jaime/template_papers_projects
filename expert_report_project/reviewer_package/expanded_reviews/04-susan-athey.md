Review (simulated) — Susan Athey

Major assessment

The proposal appropriately recognises heterogeneity as important, but the current manuscript lacks a pre-specified workflow for honest CATE estimation and multiplicity control. If heterogeneity is a selling point, the authors must commit to a principled estimation strategy (sample-splitting, honest forests or CATE cross-fitting) and show calibration/validity diagnostics.

Suggested edits

1. Add a methods subsection titled "Heterogeneity analysis" where you pre-specify (i) the CATE estimator(s) you will use (e.g., causal forests/grf, DML CATE), (ii) the sample-splitting or cross-fitting plan, and (iii) how you control false discovery when reporting multiple subgroup effects.  
2. Provide a short plan for visualizations: CATE distribution plot, calibration plot, and variable importance for heterogeneity.

Empirical checks to add

- Include a demo CATE plot from the synthetic IHDP dataset (effect by quantile of a strong moderator) to show feasibility.  
- Implement honest inference (variance estimates for CATE) and report whether heterogeneous effects hold after correction for multiplicity.

Reference guidance

Cite Athey & Wager (causal forests) and recent papers on honest inference and multiplicity correction in heterogeneous treatment effect estimation.

Actionable checklist (high priority)

- Add pre-specification of CATE methods and sample-splitting.  
- Provide demo figure from IHDP in the appendix.  
- Add a short paragraph describing multiplicity control strategy.