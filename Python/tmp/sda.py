import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/kojimajun/MultiAspectForensics/result_all_cp_union.csv')


df['ip_src_cp_log'] = [np.log10(i) if i > 0 else np.log10(i*-1) if i < 0 else 0 for i in df['ip_src_cp']]
df['ip_src_cp_log_hist'] = np.trunc(df['ip_src_cp_log']/0.1)

df_hist = df.groupby('ip_src_cp_log_hist').agg({'ip_src':'nunique'})

#ax = df_hist.plot(kind='barh')
#ax.tick_params(labelleft="off",left="off")
#fig = ax.get_figure()
#fig.savefig('/Users/kojimajun/MultiAspectForensics/test.png')
#plt.close('all')
#plt.close('all')
#plt.show()
#plt.close('all')
#plt.tick_params(labelleft="off",left="off")


df_hist = df_hist.sort_values(by='ip_src',ascending=False)
Q_sum = np.sum(np.square(df_hist['ip_src']))
H_max = df_hist['ip_src'].max()

S = pd.DataFrame()
df['inspected'] = False
df['hist_num'] = None
Q = 0
K = 10
s = 0.9
r = 0.5
i = 1

for cp_log_value, freq in df_hist.itertuples(name=None):
  if i > K:
    break
  #Sにヒストグラムの要素を追加
  df['inspected'] = np.logical_or(df['ip_src_cp_log_hist']==cp_log_value,df['inspected'])
  #df[df['ip_src_cp_log_hist']==cp_log_value]['hist_num'] = i
  df.loc[df['ip_src_cp_log_hist']==cp_log_value,'hist_num'] = i
  S = S.append(df[df['ip_src_cp_log_hist']==cp_log_value])
  #Qに頻度を追加
  Q = Q + np.square(freq)
  if Q/Q_sum >= s and H_max/freq < r:
    break
  i += 1

print(Q_sum,Q)
if Q/Q_sum < s:
  #Sを初期化
  S = None

#df_inspected = df.groupby(['ip_src_cp_log_hist']).agg({'ip_src':'nunique','inspected':'max'})
#df_inspected['ip_src_cp_log_hist'] = df_inspected.index
#plt.figure()
#for ci in [0,1]:
#  data = df_inspected[df_inspected['inspected']*1==ci]
#  plt.barh(list(data['ip_src_cp_log_hist']),list(data['ip_src']),color='rb'[ci])
#plt.savefig('/Users/kojimajun/MultiAspectForensics/test_inspected.png')
#plt.show()
#plt.close('all')



S.to_csv('/Users/kojimajun/MultiAspectForensics/inspected.csv',
 index=False,header=True)

df.to_csv('/Users/kojimajun/MultiAspectForensics/result_all_cp_union_inspected.csv',
 index=False,header=True)