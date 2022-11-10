# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 23:31:34 2022

@author: SPTINT-07
"""
import pandas as pd
import numpy as np
info=np.array(['P','a','n','d','a','s'])
a=pd.Series(info)
print(a)

x=pd.Series(7,index=[0,1,2,3])
print(x)

index=pd.Index([2,1,1,np.nan,3])
print(index.value_counts())

ser1=pd.Series([1,2,3,4,5])
ser2=pd.Series([3,4,5,6,7])
union=pd.Series(np.union1d(ser1,ser2))
intersect=pd.Series(np.intersect1d(ser1,ser2))
notcommonseries=union[~union.isin(intersect)]
print(notcommonseries)