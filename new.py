#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

from calendar import month_name
import os
import pandas as pd
import requests as rq
import gzip as gz
import shutil as sh
import csv
import matplotlib.pyplot as plt


#----------------------------------------------------------------FUNCTIONS
def list_into_json(word):                            #function that take a list as an input and writes it in in json format in the output file
    word1 = str(word).split("', '")                  #has to be edited in function of the number of paramenters of the list
    string_list = []
    string_list.append(word1[0].replace("['", ""))
    string_list.append(word1[1].replace("']", ""))
    block_output_data.write('{')
    block_output_data.write('"id":')
    block_output_data.write(string_list[0])
    block_output_data.write(', "gas_used":')
    block_output_data.write(string_list[1])
    block_output_data.write('}')
    block_output_data.write('\n')

def day_media_into_json(da, mo, ye, my_list):   
    day_output_data.write('{')
    day_output_data.write('"day":"')
    day_output_data.write(str(da)+"-"+str(mo)+"-"+str(ye)+'", "gas_media":')
    day_output_data.write(str(list_media(my_list)))
    day_output_data.write('}')
    day_output_data.write('\n')
    return list_media(my_list)

def list_media(my_list):                            #function that returns the media of a set of numbers inside a list
    total_sum = 0.0
    aa = 0
    while aa < len(my_list):
        total_sum += float(my_list[aa])
        aa += 1
    media = total_sum/len(my_list)
    return media


#----------------------------------------------------------------INPUT DATA DIRECTORY CREATION

actual_path = os.getcwd()                                   #obtain actual directory
input_data_path = os.path.join(actual_path, 'input_data')  
if os.path.exists(input_data_path) == False:                                 #create folder 'input_data' inside actual directory if it doesn't exist yet
    os.mkdir(input_data_path)


#----------------------------------------------------------------OUTPUT DATA FILE CREATION

block_output_data = open("block_output_data.txt","w+")      #the output file is created and opened
day_output_data = open("day_output_data.txt","w+")


#----------------------------------------------------------------URL CREATION

year = 2015     #year of the input file
month = 7       #month of the input file
day = 30        #day of the input file
url1 = 'https://gz.blockchair.com/ethereum/blocks/blockchair_ethereum_blocks_'   #the first part of the input file url
ext = '.tsv.gz' #extension of the input file


#----------------------------------------------------------------VARIABLE DECLARATION

day_block_list = []  #list where the block data from input files is stored (FOR GRAPH)
day_gas_list = []    #list where the gas data from input files is stored (FOR GRAPH)

day_string_media_list = []
day_media_gas_list = []


aa = 0
while aa < 50:


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
        #day_block_list.append(row[0])
        day_gas_list.append(row[1])
        list_into_json(row)              #the row is written as json in the output

    aa+=1                               #the iteration counter and the date of the next file are updated


    day_media = day_media_into_json(day, month, year, day_gas_list)     #the media of the gas used in this day is calculated
    day_media_gas_list.append(day_media)                                #the media is added to the suitable list

    date_string = str(day)+"-"+str(month)+"-"+str(year)
    day_string_media_list.append(date_string)
    day_gas_list = []

    day+=1
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        if day > 31:
            day = 1
            month += 1
    elif (month == 2):
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

plt.plot(day_string_media_list,day_media_gas_list)
plt.xlabel('day')
plt.ylabel('gas media per day')
plt.title('Gas media used per day')
plt.savefig('day_media_gas_used.png')

print()
print("Data extraction finished!")