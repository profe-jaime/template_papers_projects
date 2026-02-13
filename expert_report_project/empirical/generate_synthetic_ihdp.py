import numpy as np
import pandas as pd
from pathlib import Path

OUT = Path(__file__).parent / 'data' / 'ihdp.csv'
OUT.parent.mkdir(exist_ok=True)

np.random.seed(123)
N = 1000
p = 5
X = np.random.normal(0, 1, size=(N, p))
# true propensity depends on first two covariates
logit = -0.2 + 0.5 * X[:,0] - 0.3 * X[:,1]
ps = 1 / (1 + np.exp(-logit))
T = np.random.binomial(1, ps)
# outcome: baseline + treatment effect 2.0 + noise
beta = np.array([0.3, -0.2, 0.1, 0.0, 0.05])
Y0 = X.dot(beta) + np.random.normal(0, 1, size=N)
Y1 = Y0 + 2.0
Y = T * Y1 + (1 - T) * Y0

cols = {f'x{i+1}': X[:,i] for i in range(p)}
cols['treatment'] = T
cols['outcome'] = Y

df = pd.DataFrame(cols)
df.to_csv(OUT, index=False)
print('Wrote synthetic IHDP to', OUT)
