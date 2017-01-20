import pandas as pd
import numpy as np
df1=pd.read_csv('load_zones.tab',sep="\t",index_col=0)
df2=pd.read_csv('loads.tab',sep="\t",index_col=0)
df3=pd.read_csv('project_info.tab',sep='\t')
df4=pd.DataFrame(index=df1.index,columns=['distribution','generation','peak_load'])
for i in df4.index:
    df4.loc[i,'distribution']=float(df1.loc[i,'existing_local_td'])
    df4.loc[i,'generation']=df3[df3['proj_load_zone']==i]['proj_capacity_limit_mw'].sum()
    df4.loc[i,'peak_load']=df2.loc[i,'lz_demand_mw'].max()
df4.to_csv('comparison.csv')