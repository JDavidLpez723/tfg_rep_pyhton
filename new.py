#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pandas as pd
import requests as rq


df = pd.read_csv("input_data/myfile.tsv", sep='\t') #open the input file as a dataframe
df = df.drop(df.columns[[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]],axis = 1) #drops all columns except 'id' and 'gas_used'


print(df)