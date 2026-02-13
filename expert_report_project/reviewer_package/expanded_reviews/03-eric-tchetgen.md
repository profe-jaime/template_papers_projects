Review (simulated) — Eric Tchetgen Tchetgen

Major assessment

The manuscript mentions proximal methods and proxies but lacks a precise statement of the proxy-validity assumptions and the moments/equations used for identification. Proximal identification relies on specialized assumptions (presence of valid treatment and outcome proxies satisfying completeness-type conditions) that must be stated and, where possible, empirically assessed.

Suggested edits

1. Add a brief subsection that spells out the proximal identifying assumptions: how the treatment proxy and outcome proxy relate to the unmeasured confounder, conditional independence relations, and any completeness assumptions (state them clearly).  
2. Include a simple schematic showing the proxy relations and the estimating equations (or references to the exact estimator used).

Empirical checks to add

- In simulations, include at least one scenario where proxies are valid and one where they are invalid; show how the proximal estimator performs relative to TMLE/DML.  
- For real-data candidates, list concrete variables proposed as proxies and provide justification from measurement logic (why they capture the latent confounder).

Reference guidance

Cite Tchetgen Tchetgen and coauthors (2019–2022) and include an appendix with the estimator derivation or pointer to code if using published implementations.

Actionable checklist (high priority)

- Explicitly state proxy validity assumptions.  
- Add a proximal simulation comparing performance under proxy violation.  
- Provide candidate proxies and measurement rationale for applied datasets.