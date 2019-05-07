import pandas as pd

def spike_table(S,col_names):
  df = S
  K = 10

  result = []
  for col in col_names:
    col_names_except = col_names[:]
    col_names_except.remove(col)
    for k in range(K):
      tmp = []
      hist = df[df[str(col)+'_hist_num'] == k+1]
      uniq_num = hist[col].nunique()
      common_patterns = hist.drop_duplicates(subset=col_names_except)
      common_patterns = len(common_patterns)
      unique_mode = []
      for col_except in col_names_except:
        unique_mode.append(hist[col_except].nunique())

      tmp.append(k+1)
      tmp.append(uniq_num)
      tmp.append(common_patterns)
      for mode in unique_mode:
        tmp.append(mode)
      tmp.append(col)
      result.append(tmp)

  result = pd.DataFrame(result)
  cols = ['hist_num','freq_count','common_patterns']
  for i,mode in enumerate(unique_mode):
    cols.append('uniq_element_mode'+str(i))
  cols.append('mode')
  result.columns = cols
  return result