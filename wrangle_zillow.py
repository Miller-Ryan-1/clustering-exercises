import pandas as pd
import numpy as np

def row_null_analyzer(df):
    dict_list = []
    for col in df.columns:
        col_nulls = df[col].isnull().sum()
        col_null_percent = col_nulls/len(df.index)
        dict_list.append({'':col,'num_rows_missing':col_nulls,'pct_rows_missing':col_null_percent})
    return pd.DataFrame(dict_list).set_index('').sort_values(by='num_rows_missing', ascending=False)

def remove_columns(df, cols_to_remove):  
    df = df.drop(columns=cols_to_remove)
    return df

def handle_missing_values(df, prop_required_column = .75, prop_required_row = .75):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def data_prep(df, cols_to_remove=[], prop_required_column=.75, prop_required_row=.75):
    df_og = df.copy()
    df = remove_columns(df, cols_to_remove)
    df = handle_missing_values(df, prop_required_column, prop_required_row)
    print(f'Features removed:\n{[x for x in df_og.columns if x not in df.columns]}')
    return df