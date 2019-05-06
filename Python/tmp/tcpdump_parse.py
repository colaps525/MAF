from scapy.all import *
import collections
import pandas as pd
from datetime import datetime
import csv

file_list = [
'/Users/kojimajun/MultiAspectForensics/lbl-internal.20041004-1313.port003.dump.anon-scanners'
#'/Users/kojimajun/MultiAspectForensics/lbl-internal.20041004-1333.port007.dump.anon'
]
result = []

for path in file_list:
  packets = rdpcap(path)
  for p in packets:
    packet_data = []

    try:
      ip_src = p['IP'].src
    except:
      ip_src = 'NULL'

    try:
      ip_dst = p['IP'].dst
    except:
      ip_dst = 'NULL'

    try:
      dst_port = p['TCP'].dport
    except:
      dst_port = 'NULL'

    try:
      epoch_time = p.time
      datetime_str = datetime.fromtimestamp(epoch_time).isoformat()
    except:
      epoch_time = 'NULL'

    if ip_src != 'NULL' and ip_dst != 'NULL' and dst_port != 'NULL':
      packet_data.append(ip_src)
      packet_data.append(ip_dst)
      packet_data.append(dst_port)
      packet_data.append(datetime_str)

      result.append(packet_data)

name = ['ip_src','ip_dst','dst_port','epoch_time']
df = pd.DataFrame(result)
df.columns = name
print(df)

agg_key = ['ip_src','ip_dst','dst_port']
df_agg = df.groupby(agg_key).count()
print(df_agg)

df_agg.to_csv('/Users/kojimajun/MultiAspectForensics/result_scan.csv',header=True,index=True,quoting=csv.QUOTE_ALL)

