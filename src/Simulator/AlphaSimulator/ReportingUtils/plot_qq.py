import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
import numpy as py
import os

def plot_qq(df_g, **params):
    enums = params['enums']
    #standardize the logreturn with scalre() imported from sklearn.preprocessing
    data=scale(df_g['log_return'])
    #create Q-Q plot with 45-degree line added to plot
    
    sm.qqplot(data,line='45')
    plt.xlabel("Theoretical Quantiles")
    plt.ylabel("Sample Quantiles")
    plt.title('QQ plot of the log return')
    plt.savefig(os.path.join(enums.STAT_FIGURES_DIR, "QQReturnHistogram.png"))
    plt.close()