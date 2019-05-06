import pandas as pd

def union_cp(df_all,U,dim_cols):
  U_keys = U.keys()
  dim_cols_new = [str(i) + '_cp' for i in dim_cols]
  for k in U_keys:
    df_U = pd.DataFrame(U[k])
    dict_index = df_U.to_dict()
    df_all[dim_cols_new[k]] = df_all[dim_cols[k]].map(dict_index[0])

  df_all.to_csv('/Users/kojimajun/MultiAspectForensics/Python/MAF/result_all_cp_union.csv',index=False,header=True)
  return df_all

  #CP1
  #df_cp1 = pd.read_csv('/Users/kojimajun/MultiAspectForensics/MATLAB/result_cp_ip_src.csv',header=None)
  #dict_cp1 = df_cp1.to_dict()
  #df_all['ip_src_cp'] = df_all['ip_src_id'].map(dict_cp1[0])

  #CP2
  #df_cp2 = pd.read_csv('/Users/kojimajun/MultiAspectForensics/MATLAB/result_ip_dst.csv',header=None)
  #dict_cp2 = df_cp2.to_dict()
  #df_all['ip_dst_cp'] = df_all['ip_dst_id'].map(dict_cp2[0])

  #CP3
  #df_cp3 = pd.read_csv('/Users/kojimajun/MultiAspectForensics/MATLAB/result_cp_dst_port.csv',header=None)
  #dict_cp3 = df_cp3.to_dict()
  #df_all['dst_port_cp'] = df_all['dst_port_id'].map(dict_cp3[0])

  #df_all.to_csv('/Users/kojimajun/MultiAspectForensics/result_all_cp_union.csv',index=False,header=True)