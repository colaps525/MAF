from attr_to_id import attr_to_id
from cp_als import cp_als
from union_cp import union_cp
from sda import sda
from spike_table import spike_table

#1:属性をid(番号)に変換(attr_to_id)
input_path = '/Users/kojimajun/MultiAspectForensics/Python/MAF/データ準備(tcpdump)/result.csv'
df,dim_cols,value_col,dim_cols_orig = attr_to_id(input_path)

#2:CP分解(cp_als・sparse_tensor_util)
target_cols = []
target_cols = dim_cols[:]
target_cols.append(value_col)
df_id = df[target_cols]
X = {}
for index,row in df_id.iterrows():
  dim_id = []
  for d in dim_cols:
    dim_id.append(row[d])
  dim_id = tuple(dim_id)
  X[dim_id] = row[value_col]
#print(X)
U,lamb = cp_als(X,1)

#3:CP分解の結果をデータと結合(union_cp)
df_all,cp_col_name = union_cp(df,U,dim_cols)

#4:スパイク検出(sda)
df_sda,S = sda(df_all,dim_cols_orig)

#5:検出されたスパイクの分析(spike_table)
resutl = spike_table(S,dim_cols_orig)
print(resutl)