#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

import os
import requests as rq
import gzip as gz
import shutil as sh
import csv


#----------------------------------------------------------------FUNCTIONS
def list_into_json(word, output_id):                           #function that take a list as an input and writes it in in json format in the output file
    block_output_data = open("output_data/block_output_data"+str(output_id)+".txt","a")  #the output files are created and opened
    stats = os.stat("output_data/block_output_data"+str(output_id)+".txt")
    #print(stats.st_size)
    if stats.st_size > 1000000000:
        block_output_data.close()
        output_id += 1
        block_output_data = open("output_data/block_output_data"+str(output_id)+".txt","a")
    word1 = str(word).split("', '")                 #has to be edited in function of the number of paramenters of the list
    string_list = []
    string_list.append(word1[0].replace("['", ""))
    string_list.append(word1[1])
    string_list.append(word1[2])
    string_list.append(word1[3])
    string_list.append(word1[4])
    string_list.append(word1[5])
    string_list.append(word1[6])
    string_list.append(word1[7])
    string_list.append(word1[8])
    string_list.append(word1[9])
    string_list.append(word1[10])
    string_list.append(word1[11])
    string_list.append(word1[12])
    string_list.append(word1[13])
    string_list.append(word1[14])
    string_list.append(word1[15])
    string_list.append(word1[16])
    string_list.append(word1[17])
    string_list.append(word1[18])
    string_list.append(word1[19].replace("']", ""))
    block_output_data.write('{')
    block_output_data.write('"id":')
    block_output_data.write(string_list[0])
    block_output_data.write(', "time":"')
    block_output_data.write(string_list[1])
    block_output_data.write('", "size":')
    block_output_data.write(string_list[2])
    block_output_data.write(', "difficulty":')
    block_output_data.write(string_list[3])
    block_output_data.write(', "gas_used":')
    block_output_data.write(string_list[4])
    block_output_data.write(', "gas_limit":')
    block_output_data.write(string_list[5])
    block_output_data.write(', "nonce":')
    block_output_data.write(string_list[6])
    block_output_data.write(', "total_difficulty":')
    block_output_data.write(string_list[7])
    block_output_data.write(', "transaction_count":')
    block_output_data.write(string_list[8])
    block_output_data.write(', "call_count":')
    block_output_data.write(string_list[9])
    block_output_data.write(', "value_total":')
    block_output_data.write(string_list[10])
    block_output_data.write(', "value_total_usd":')
    block_output_data.write(string_list[11])
    block_output_data.write(', "internal_value_total":')
    block_output_data.write(string_list[12])
    block_output_data.write(', "internal_value_total_usd":')
    block_output_data.write(string_list[13])
    block_output_data.write(', "generation":')
    block_output_data.write(string_list[14])
    block_output_data.write(', "generation_usd":')
    block_output_data.write(string_list[15])
    block_output_data.write(', "fee_total":')
    block_output_data.write(string_list[16])
    block_output_data.write(', "fee_total_usd":')
    block_output_data.write(string_list[17])
    block_output_data.write(', "reward":')
    block_output_data.write(string_list[18])
    block_output_data.write(', "reward_usd":')
    block_output_data.write(string_list[19])
    block_output_data.write('}')
    block_output_data.write('\n')
    block_output_data.close()
    return output_id

#def day_media_into_json(da, mo, ye, gas_list, size_list):       #function that write the day date and the day media value into the output file
#    day_output_data.write('{')
#    day_output_data.write('"day":"')
#    day_output_data.write(str(da)+"-"+str(mo)+"-"+str(ye)+'", "gas_media":')
#    day_output_data.write(str(list_media(gas_list)))
#    day_output_data.write(', "size_media":')
#    day_output_data.write(str(list_media(size_list)))
#    day_output_data.write('}')
#    day_output_data.write('\n')

#def list_media(my_list):                            #function that returns the media of a set of numbers inside a list
#    total_sum = 0.0
#    aa = 0
#    while aa < len(my_list):
#        total_sum += float(my_list[aa])
#        aa += 1
#    media = total_sum/len(my_list)
#    return media


#----------------------------------------------------------------INPUT DATA DIRECTORY CREATION

actual_path = os.getcwd()                                   #obtain actual directory
input_data_path = os.path.join(actual_path, 'input_data')  
if os.path.exists(input_data_path) == False:                #create folder 'input_data' inside actual directory if it doesn't exist yet
    os.mkdir(input_data_path)


#----------------------------------------------------------------OUTPUT DATA DIRECTORY AND FILES CREATION

output_data_path = os.path.join(actual_path, 'output_data')  
if os.path.exists(output_data_path) == False:                       #create folder 'output_data' inside actual directory if it doesn't exist yet
    os.mkdir(output_data_path)

output_id=0


#----------------------------------------------------------------URL CREATION

year = 2015     #year of the input file
month = 7       #month of the input file
day = 30        #day of the input file
url1 = 'https://gz.blockchair.com/ethereum/blocks/blockchair_ethereum_blocks_'   #the first part of the input file url
ext = '.tsv.gz' #extension of the input file


#----------------------------------------------------------------VARIABLE DECLARATION

aa = 0
while aa < 1000:


    #------------------------------------------------------------DOWNLOAD INPUT FILE

    if month < 10:                                              #we adapt the date to fit in the url
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

    url = url1 + file_id + ext                                  #the url of the input file

    r = rq.get(url, allow_redirects=True)
    open('input_data/input_file.tsv.gz', 'wb').write(r.content) #the .gz file is downloaded from the url


    #------------------------------------------------------------EXTRACT INPUT FILE

    with gz.open('input_data/input_file.tsv.gz', 'rb') as f_in:     #the .gz file is extracted and a .tsv file is obtained
        with open('input_data/input_file.tsv', 'wb') as f_out:
            sh.copyfileobj(f_in, f_out)

    f_in.close()                                                    #the .gz and .tsv files are closed
    f_out.close()
    os.remove("input_data/input_file.tsv.gz")                       #the .gz file is deleted
    

    #------------------------------------------------------------OPEN INPUT FILE AND OBTAIN DATA

    input_file = open("input_data/input_file.tsv")              #the input file is opened
    input_file_list = csv.reader(input_file, delimiter="\t")    #the data from the file is opened as a list

    for row in input_file_list:                                 #the name of the columns is deleted
        del row
        break

    for row in input_file_list:                                 #the columns not needed are deleted
        del row[1]
        del row[3:5]
        del row[6:8]
        del row[7:10]
        del row[8:10]
        del row [9]
        del row [10]
        del row [16:18]
        new_output_id = list_into_json(row, output_id)                                     #the row is written as json in the output
        output_id = new_output_id

    aa+=1                                                       #the iteration counter and the date of the next file are updated
    day+=1
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        if day > 31:
            day = 1
            if month == 12:
                year += 1
                month = 1
            else:
                month += 1

    elif (month == 2):
        if (year == 2016 or year == 2020):
            if day > 29:
                day = 1
                month += 1
        else:
            if day > 28:
                day = 1
                month += 1 
    else:
        if day > 30:
            day = 1
            month += 1
    
    input_file.close()                                          #the .tsv file is closed and deleted
    os.remove("input_data/input_file.tsv")                     