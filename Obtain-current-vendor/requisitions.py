# coding: utf-8
import os
import glob
import pandas as pd


def _main():
    path = r'C:\path\to\csvFiles'
    all_files = glob.glob(os.path.join(path, "*.csv"))
    df_from_each_file = (pd.read_csv(f, delimiter=',', encoding='ISO-8859-1',
                                     low_memory=False, skipinitialspace=True) for f in all_files)
    concatenated_df = pd.concat(df_from_each_file, ignore_index=True)
    concatenated_df = concatenated_df.rename(columns={'PO date': 'date'})
    concatenated_df['date'] = pd.to_datetime(concatenated_df.date)
    df_summary = concatenated_df.sort_values(
        'date').groupby('Material').tail(1)
    finalFile = df_summary.loc[:, [
        'Vendor Name 1', 'Material', 'Vendor #', 'date']]
    finalFile.to_csv(r'%s\out.txt' % path, sep='\t')


_main()
