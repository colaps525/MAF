import pandas as pd

df = pd.read_csv('/Users/kojimajun/MultiAspectForensics/inspected.csv')

K = 10
cols = ['hist_num','freq_count','common_patterns','uniq_element_mode1','uniq_element_mode2']
result = []
for k in range(K):
  tmp = []
  hist = df[df['hist_num'] == k+1]
  ip_src_uniq_num = hist['ip_src'].nunique()
  common_patterns = hist.drop_duplicates(subset=['ip_dst','dst_port'])
  common_patterns = len(common_patterns)
  unique_mode1 = hist['ip_dst'].nunique()
  unique_mode2 = hist['dst_port'].nunique()

  tmp.append(k+1)
  tmp.append(ip_src_uniq_num)
  tmp.append(common_patterns)
  tmp.append(unique_mode1)
  tmp.append(unique_mode2)
  result.append(tmp)

result = pd.DataFrame(result)
result.columns = cols
print(result)