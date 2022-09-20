#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

import os
import json



#----------------------------------------------------------------FUNCTIONS

def day_list_into_json(actual_day, first_id, last_id, day_block_gas_used, day_block_size, day_block_difficulty, day_block_gas_limit, day_block_total_difficulty, day_block_transaction_count, day_block_call_count, day_block_value_total, day_block_value_total_usd, day_block_internal_value_total, day_block_internal_value_total_usd, day_block_generation, day_block_generation_usd, day_block_fee_total, day_block_fee_total_usd, day_block_reward, day_block_reward_usd, day_output_id):                               #function that take a list of a day as an input and writes the media values in json format in the output file
    day_output_data = open("day_media_output_data/day_media_output_data"+str(day_output_id)+".txt","a")  #the output files are created and opened
    
    stats = os.stat("day_media_output_data/day_media_output_data"+str(day_output_id)+".txt")        #the size of the actual file is checked
    if stats.st_size > 1000000000:                                                                  #if the size is bigger than 1GB, the next line of data is stored in a new file with a new file id
        day_output_data.close()
        day_output_id += 1
        day_output_data = open("day_media_output_data/day_media_output_data"+str(day_output_id)+".txt","a")
    
    day_output_data.write('{')
    day_output_data.write('"date":"')
    day_output_data.write(actual_day)
    day_output_data.write('", "blocks":"')
    day_output_data.write(str(first_id)+"-"+str(last_id))
    day_output_data.write('", "gas_used":')
    day_output_data.write(str(list_media(day_block_gas_used)))
    day_output_data.write(', "gas_limit":')
    day_output_data.write(str(list_media(day_block_gas_limit)))
    day_output_data.write(', "size":')
    day_output_data.write(str(list_media(day_block_size)))
    day_output_data.write(', "difficulty":')
    day_output_data.write(str(list_media(day_block_difficulty)))
    day_output_data.write(', "total_difficulty":')
    day_output_data.write(str(list_media(day_block_total_difficulty)))
    day_output_data.write(', "transaction_count":')
    day_output_data.write(str(list_media(day_block_transaction_count)))
    day_output_data.write(', "call_count":')
    day_output_data.write(str(list_media(day_block_call_count)))
    day_output_data.write(', "value_total":')
    day_output_data.write(str(list_media(day_block_value_total)))
    day_output_data.write(', "value_total_usd":')
    day_output_data.write(str(list_media(day_block_value_total_usd)))
    day_output_data.write(', "internal_value_total":')
    day_output_data.write(str(list_media(day_block_internal_value_total)))
    day_output_data.write(', "internal_value_total_usd":')
    day_output_data.write(str(list_media(day_block_internal_value_total_usd)))
    day_output_data.write(', "generation":')
    day_output_data.write(str(list_media(day_block_generation)))
    day_output_data.write(', "generation_usd":')
    day_output_data.write(str(list_media(day_block_generation_usd)))
    day_output_data.write(', "fee_total":')
    day_output_data.write(str(list_media(day_block_fee_total)))
    day_output_data.write(', "fee_total_usd":')
    day_output_data.write(str(list_media(day_block_fee_total_usd)))
    day_output_data.write(', "reward":')
    day_output_data.write(str(list_media(day_block_reward)))
    day_output_data.write(', "reward_usd":')
    day_output_data.write(str(list_media(day_block_reward_usd)))
    day_output_data.write('}')
    day_output_data.write('\n')
    day_output_data.close()
    
    return day_output_id

def list_media(my_list):                            #function that returns the media of a set of numbers inside a list
    total_sum = 0.0
    aa = 0
    while aa < len(my_list):
        total_sum += float(my_list[aa])
        aa += 1
    media = total_sum/len(my_list)
    media = round(media, 4)
    return media



#----------------------------------------------------------------OUTPUT DATA DIRECTORY AND FILES CREATION

actual_path = os.getcwd()                                                   #obtain actual directory
day_output_data_path = os.path.join(actual_path, 'day_media_output_data')  
if os.path.exists(day_output_data_path) == False:                           #create folder 'day_media_output_data' inside actual directory if it doesn't exist yet
    os.mkdir(day_output_data_path)



#----------------------------------------------------------------VARIABLE DECLARATION

day_output_id = 0                                                           #the id of the actual output file
day_input_id = 8                                                            #the id of the actual input file 

day_block_gas_used = []                                                     #list for storing the gas used of the blocks of the same day
day_block_size = []                                                         #list for storing the size of the blocks of the same day
day_block_difficulty = []                                                   #list for storing the difficulty of the blocks of the same day
day_block_gas_limit = []                                                    #list for storing the gas_limit of the blocks of the same day
day_block_total_difficulty = []                                             #list for storing the total_difficulty of the blocks of the same day
day_block_transaction_count = []                                            #list for storing the transaction_count of the blocks of the same day
day_block_call_count = []                                                   #list for storing the call_count of the blocks of the same day
day_block_value_total = []                                                  #list for storing the value_total of the blocks of the same day
day_block_value_total_usd = []                                              #list for storing the value_total_usd of the blocks of the same day
day_block_internal_value_total = []                                         #list for storing the internal_value_total of the blocks of the same day
day_block_internal_value_total_usd = []                                     #list for storing the internal_value_total_usd of the blocks of the same day
day_block_generation = []                                                   #list for storing the generation of the blocks of the same day
day_block_generation_usd = []                                               #list for storing the generation_usd of the blocks of the same day
day_block_fee_total = []                                                    #list for storing the fee_total of the blocks of the same day
day_block_fee_total_usd = []                                                #list for storing the fee_total_usd of the blocks of the same day
day_block_reward = []                                                       #list for storing the reward of the blocks of the same day
day_block_reward_usd = []                                                   #list for storing the reward_usd of the blocks of the same day
actual_day = 0                                                              #variable for storing the actual day while extracting the data
first_id = 0                                                                #variable for storing the first block id of the actual day
last_id = 0                                                                 #variable for storing the last block id of the actual day

year = 2022
month = 7
day = 9



#---------------------------------START OF THE LOOP


aa = 0
while aa < 2:

    if month < 10:                                                                      #we adapt the date to fit the input notation
        if day < 10:
            actual_day = str(year)+"-"+"0"+str(month)+"-"+"0"+str(day)   
        else:
            actual_day = str(year)+"-"+"0"+str(month)+"-"+str(day)  
    else:
        if day < 10:
            actual_day = str(year)+"-"+str(month)+"-"+"0"+str(day)  
        else:
            actual_day = str(year)+"-"+str(month)+"-"+str(day)  
    print()
    print("File date: "+actual_day)
    print()

    #blocks_file = open("new/new78"+".txt", 'r')   #the json input file is opened
    blocks_file = open("output_data/block_output_data"+str(day_input_id)+".txt", 'r')   #the json input file is opened
    lines = blocks_file.readlines()                                                     #a list containing the lines of the json file is created
    block_counter = 0                                                                   #variable created in order to know if the actual block is the first or not

    for line in lines:                         #this loop will execute until the day changes and it will fill the lists with data of every parameter (e.g gas_used) of the same day
        json_object = json.loads(line)
        word1 = json_object["time"]
        word1 = str(word1).split(" ")
        if actual_day == word1[0]:
            if block_counter == 0:
                first_id = json_object["id"]
            day_block_gas_used.append(json_object["gas_used"])
            day_block_size.append(json_object["size"])
            day_block_difficulty.append(json_object["difficulty"])
            day_block_gas_limit.append(json_object["gas_limit"])
            day_block_total_difficulty.append(json_object["total_difficulty"])
            day_block_transaction_count.append(json_object["transaction_count"])
            day_block_call_count.append(json_object["call_count"])
            day_block_value_total.append(json_object["value_total"])
            day_block_value_total_usd.append(json_object["value_total_usd"])
            day_block_internal_value_total.append(json_object["internal_value_total"])
            day_block_internal_value_total_usd.append(json_object["internal_value_total_usd"])
            day_block_generation.append(json_object["generation"])
            day_block_generation_usd.append(json_object["generation_usd"])
            day_block_fee_total.append(json_object["fee_total"])
            day_block_fee_total_usd.append(json_object["fee_total_usd"])
            day_block_reward.append(json_object["reward"])
            day_block_reward_usd.append(json_object["reward_usd"])
            last_id = json_object["id"]
            block_counter = 1
        else:
            if block_counter == 1:
                block_counter = 0
                break

    new_day_output_id = day_list_into_json(actual_day, first_id, last_id, day_block_gas_used, day_block_size, day_block_difficulty, day_block_gas_limit, day_block_total_difficulty, day_block_transaction_count, day_block_call_count, day_block_value_total, day_block_value_total_usd, day_block_internal_value_total, day_block_internal_value_total_usd, day_block_generation, day_block_generation_usd, day_block_fee_total, day_block_fee_total_usd, day_block_reward, day_block_reward_usd, day_output_id)        #the data extracted is written in the json
    day_output_id = new_day_output_id              #the file id is updated

    day_block_gas_used.clear()                     #the lists are emptied for the next iteration
    day_block_size.clear()
    day_block_difficulty.clear()
    day_block_gas_limit.clear()
    day_block_total_difficulty.clear()
    day_block_transaction_count.clear()
    day_block_call_count.clear()
    day_block_value_total.clear()
    day_block_value_total_usd.clear()
    day_block_internal_value_total.clear()
    day_block_internal_value_total_usd.clear()
    day_block_generation.clear()
    day_block_generation_usd.clear()
    day_block_fee_total.clear()
    day_block_fee_total_usd.clear()
    day_block_reward.clear()
    day_block_reward_usd.clear()
    del lines

    aa += 1                                        #the loop counter is updated
    day += 1                                       #the date is updated
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
    
    blocks_file.close()                                                  