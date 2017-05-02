#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:05:45 2017

@author: administrator
"""

import numpy as np
import pandas as pd

#initialize random like rates for 100 couriers
couriers = np.random.rand(100,1)
#round floats to 2 decimals to be like 
np.around(couriers, decimals=2, out=couriers)
#index numeration
index = [int(i) for i in range(1, len(couriers)+1)]
#here data frame is created
columns = ['likes rate']
df = pd.DataFrame(couriers, index=index, columns=columns)
df['to terminate'] = 'no'
#mean of like rate for all couriers is estimated
mean = np.mean(df['likes rate'])

#couriers having like rate less than 2/3 mean are adviced for termination
to_terminate=(df[(3*df <= 2*mean).all(axis=1)])
df=(df[(3*df > 2*mean).all(axis=1)])
to_terminate['to terminate'] = 'yes'
#results are concatenated and sorted in single dataframe
df_concatenated = pd.concat([df, to_terminate])
df_sorted=df_concatenated.sort_index(axis=0, kind='mergesort')
print(df_sorted)
