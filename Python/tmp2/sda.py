import pandas as pd
import numpy as np

def sda(df,col_name):
  S = pd.DataFrame()
  K = 10
  s = 0.9
  r = 0.5

  for col in col_name:
    df[str(col)+'_cp_log'] = [np.log10(i) if i > 0 else np.log10(i*-1) if i < 0 else 0 for i in df[str(col)+'_for_cp_calc_id_cp']]
    df[str(col)+'_cp_log_hist'] = np.trunc(df[str(col)+'_cp_log']/0.1)

    df_hist = df.groupby(str(col)+'_cp_log_hist').agg({col:'nunique'})

    df_hist = df_hist.sort_values(by=col,ascending=False)
    Q_sum = np.sum(np.square(df_hist[col]))
    H_max = df_hist[col].max()

    df[str(col)+'_inspected'] = False
    df[str(col)+'_hist_num'] = None
    Q = 0
    i = 1
    S_tmp = pd.DataFrame()

    for cp_log_value, freq in df_hist.itertuples(name=None):
      if i > K:
        break
      #Sにヒストグラムの要素を追加
      df[str(col)+'_inspected'] = np.logical_or(df[str(col)+'_cp_log_hist']==cp_log_value,df[str(col)+'_inspected'])
    #df[df['ip_src_cp_log_hist']==cp_log_value]['hist_num'] = i
      df.loc[df[str(col)+'_cp_log_hist']==cp_log_value,str(col)+'_hist_num'] = i
      S_tmp = S_tmp.append(df[df[str(col)+'_cp_log_hist']==cp_log_value])
    #Qに頻度を追加
      Q = Q + np.square(freq)
      if Q/Q_sum >= s and H_max/freq < r:
        break
      i += 1

    print(Q_sum,Q)
    if Q/Q_sum < s:
    #Sを初期化
      S_tmp = None
      df[str(col)+'_hist_num'] = None
    S = pd.concat([S,S_tmp])

    S.to_csv('/Users/kojimajun/MultiAspectForensics/Python/MAF/inspected.csv',index=False,header=True)

    #df.to_csv('/Users/kojimajun/MultiAspectForensics/result_all_cp_union_inspected.csv',index=False,header=True)
  return df,S