import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from splitter import splitter

def get_stats(df):
    print('VARIABLES INFORMATION\n')
    print(df.info())
    print('\n-----\nDESCRIPTIVE STATISTICS\n')
    print(df.describe().T)
    print('\n-----\n')
    for col in df.columns:
        if col != 'customer_id':
            print(col)
            sns.histplot(df[col])
            plt.show()
            print('\n-----\n')

def iqr_analysis(df,k):
    iqr_list = []
    for col in df[['age','annual_income','spending_score']]:
        dict_list={}
        variable = df[col]
        q1 = variable.quantile(.25)
        q2 = variable.median()
        q3 = variable.quantile(.75)
        irq = k * (q3 - q1)
        high_outlier_cutoff = q3 + irq
        if (q1 - irq) > 0:
            low_outlier_cutoff = q1 - irq
        else:
            low_outlier_cutoff = 0
        dict_list['Variable'] = col
        dict_list['Low Outliers'] = low_outlier_cutoff
        dict_list['25% Quantile'] = q1
        dict_list['Median'] = q2
        dict_list['75% Quantile'] = q3
        dict_list['High Outliers'] = high_outlier_cutoff
        iqr_list.append(dict_list)
    return pd.DataFrame(iqr_list).set_index('Variable')

def split_mall(df):
    return splitter(df, target = 'gender')

# Encode
# Scale
# Clean