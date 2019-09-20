import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import statsmodels.formula.api as ols

HS300=pd.read_csv('tudata/HS300.csv').sort_values(by='trade_date')
ols('Reaefa~c',data=HS300.dropna()).fit()

