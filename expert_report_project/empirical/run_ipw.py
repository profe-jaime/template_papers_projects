import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import statsmodels.api as sm
from pathlib import Path

DATA = Path(__file__).parent / 'data' / 'ihdp.csv'
if not DATA.exists():
    raise SystemExit('Data file not found: ' + str(DATA))

df = pd.read_csv(DATA)
T = df['treatment']
Y = df['outcome']
X = df.drop(columns=['treatment','outcome'])

ps_model = LogisticRegression(max_iter=1000)
ps_model.fit(X, T)
ps = ps_model.predict_proba(X)[:,1]

p_t = T.mean()
w = np.where(T==1, p_t/ps, (1-p_t)/(1-ps))

wls_mod = sm.WLS(Y, sm.add_constant(T), weights=w)
res = wls_mod.fit(cov_type='HC3')
ate_ipw = res.params[1]
se_ipw = res.bse[1]
print(f'IPTW ATE = {ate_ipw:.4f} (SE {se_ipw:.4f})')
