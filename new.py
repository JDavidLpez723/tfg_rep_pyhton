#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

import os
import pandas as pd
import requests as rq
import gzip as gz
import shutil as sh
import csv
import matplotlib.pyplot as plt


#----------------------------------------------------------------FUNCTIONS
def row_into_json(word):                            #function that take a list as an input and writes it in in json format in the output file
    word1 = str(word).split("', '")                 #has to be edited in function of the number of paramenters of the list
    string_list = []
    string_list.append(word1[0].replace("['", ""))
    string_list.append(word1[1].replace("']", ""))
    output_data.write('{')
    output_data.write('"id":')
    output_data.write(string_list[0])
    output_data.write(', "gas_used":')
    output_data.write(string_list[1])
    output_data.write('}')
    output_data.write('\n')


#----------------------------------------------------------------INPUT DATA DIRECTORY CREATION

actual_path = os.getcwd()                                   #obtain actual directory
input_data_path = os.path.join(actual_path, 'input_data')  
if os.path.exists == False:                                 #create folder 'input_data' inside actual directory if it doesn't exist yet
    os.mkdir(input_data_path)


#----------------------------------------------------------------OUTPUT DATA FILE CREATION

output_data = open("output_data.txt","w+")      #the output file is created and opened


#----------------------------------------------------------------URL CREATION

year = 2015     #year of the input file
month = 7       #month of the input file
day = 30        #day of the input file
url1 = 'https://gz.blockchair.com/ethereum/blocks/blockchair_ethereum_blocks_'   #the first part of the input file url
ext = '.tsv.gz' #extension of the input file


#----------------------------------------------------------------VARIABLE DECLARATION

global_block_list = []  #list where the block data from input files is stored (FOR GRAPH)
global_gas_list = []    #list where the gas data from input files is stored (FOR GRAPH)

aa = 0
while aa < 10:


    #------------------------------------------------------------DOWNLOAD INPUT FILE

    #we adapt the date to fit in the url
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
    print("File date: "+str(day)+"-"+str(month)+"-"+str(year))
    print()

    url = url1 + file_id + ext #the url of the input file

    r = rq.get(url, allow_redirects=True)
    open('input_data/input_file.tsv.gz', 'wb').write(r.content)    #the .gz file is downloaded from the url


    #------------------------------------------------------------EXTRACT INPUT FILE

    with gz.open('input_data/input_file.tsv.gz', 'rb') as f_in:    #the .gz file is extracted and a .tsv file is obtained
        with open('input_data/input_file.tsv', 'wb') as f_out:
            sh.copyfileobj(f_in, f_out)

    f_in.close()       #the .gz and .tsv files are closed
    f_out.close()


    #------------------------------------------------------------OPEN INPUT FILE AND OBTAIN DATA

    input_file = open("input_data/input_file.tsv")              #the input file is opened
    input_file_list = csv.reader(input_file, delimiter="\t")    #the data from the file is opened as a list

    for row in input_file_list:        #the name of the columns is deleted
        del row
        break

    for row in input_file_list:         #the columns not needed are deleted
        del row[1:7]
        del row[2:28]
        global_block_list.append(row[0])
        global_gas_list.append(row[1])
        row_into_json(row)              #the row is written as json in the output

    aa+=1                               #the iteration counter and the date of the next file are updated
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


#----------------------------------------------------------------DELETING FILES
    
os.remove("input_data/input_file.tsv.gz")   #the .gz file is deleted
os.remove("input_data/input_file.tsv")   #the .tsv file is deleted


#----------------------------------------------------------------CREATING THE GRAPH

plt.plot(global_block_list,global_gas_list)
plt.xlabel('block')
plt.ylabel('gas used')
plt.title('Gas used per Ethereum block')
plt.savefig('blocks_gas_used.png')