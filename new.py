#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

import os
import pandas as pd
import requests as rq
import gzip as gz
import shutil as sh
import csv


#----------------------------------------------------------------VARIABLE DECLARATION

year = 2015     #year for the url of the input file
month = 7
day = 30
url1 = 'https://gz.blockchair.com/ethereum/blocks/blockchair_ethereum_blocks_'   #the first part of the url of the input file
ext = '.tsv.gz' #extension of the file



global_block_list = []  #the list where all the block data from all the input files is going to be stored



aa = 0
while aa < 10:
    #---------------------------------------------------------------DOWNLOAD INPUT FILE
    #we adapt the file_id
    if month < 10:
        if day < 10:
            file_id = str(year)+"0"+str(month)+"0"+str(day)   
        else:
            file_id = str(year)+"0"+str(month)+str(day)   
    else:
        if day < 10:
            file_id = str(year)+str(month)+"0"+str(day)  
        else:
            file_id = str(year)+str(month)+str(day)   

    print()
    print("File: "+file_id)
    print()


    url = url1 + file_id + ext #the url of the input file

    r = rq.get(url, allow_redirects=True)
    open('input_data/input_file.tsv.gz', 'wb').write(r.content)    #the .gz file is downloaded


    #--------------------------------------------------------------EXTRACT INPUT FILE

    with gz.open('input_data/input_file.tsv.gz', 'rb') as f_in:    #the .gz file is extracted and a .tsv file is obtained
        with open('input_data/input_file.tsv', 'wb') as f_out:
            sh.copyfileobj(f_in, f_out)

    f_in.close()
    f_out.close()

    #---------------------------------------------------------------OPEN INPUT FILE

    input_file = open("input_data/input_file.tsv")
    input_file_list = csv.reader(input_file, delimiter="\t")

    for row in input_file_list:
        del row
        break

    for row in input_file_list:
        del row[1:7]
        del row[2:28]
        global_block_list.append(row)



    aa+=1
    day+=1
    if month == (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if day > 31:
            day = 1
            month += 1
    elif month == (2):
        if day > 28:
            day = 1
            month += 1 
    else:
        if day > 30:
            day = 1
            month += 1


    #df = pd.read_csv("input_data/input_file.tsv", sep='\t') #the .tsv input file is opened as a dataframe
    #df = df.drop(df.columns[[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]],axis = 1) #all columns are dropped except 'id' and 'gas_used'


    #print(df)
    
os.remove("input_data/input_file.tsv.gz")   #the .gz file is deleted
os.remove("input_data/input_file.tsv")   #the .tsv file is deleted

for row in global_block_list:
    print(row)


