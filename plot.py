#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

import os
import csv
import json
import matplotlib.pyplot as plt

#----------------------------------------------------------------FUNCTIONS

def plot_gas_blocks():      #function for plotting the gas per block
    blocks_list = []
    blocks_gas_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_gas_list.append(json_object["gas_used"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_gas_list)
    plt.xlabel('block')
    plt.ylabel('gas used')
    plt.title('Gas used per block')
    plt.savefig('plots/blocks_gas_used.png')
    del lines
    del blocks_list
    del blocks_gas_list

def plot_tran_blocks(): #function for plotting the transaction count per block
    blocks_list = []
    blocks_tran_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_tran_list.append(json_object["transaction_count"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_tran_list)
    plt.xlabel('block')
    plt.ylabel('transaction count')
    plt.title('Transaction count per block')
    plt.savefig('plots/blocks_tran_count.png')
    del lines
    del blocks_list
    del blocks_tran_list

def plot_val_total_usd_blocks(): #function for plotting the value total usd per block
    blocks_list = []
    blocks_val_total_usd_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_val_total_usd_list.append(json_object["value_total_usd"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_val_total_usd_list)
    plt.xlabel('block')
    plt.ylabel('value total in usd')
    plt.title('Value total in USD per block')
    plt.savefig('plots/blocks_val_total_usd.png')
    del lines
    del blocks_list
    del blocks_val_total_usd_list

def plot_size_blocks(): #function for plotting the size per block
    blocks_list = []
    blocks_size_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_size_list.append(json_object["size"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_size_list)
    plt.xlabel('block')
    plt.ylabel('size')
    plt.title('Size per block')
    plt.savefig('plots/blocks_size.png')
    del lines
    del blocks_list
    del blocks_size_list

def plot_difficulty_blocks(): #function for plotting the difficulty per block
    blocks_list = []
    blocks_difficulty_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_difficulty_list.append(json_object["difficulty"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_difficulty_list)
    plt.xlabel('block')
    plt.ylabel('difficulty')
    plt.title('Difficulty per block')
    plt.savefig('plots/blocks_difficulty.png')
    del lines
    del blocks_list
    del blocks_difficulty_list

def plot_gas_limit_blocks(): #function for plotting the gas limit per block
    blocks_list = []
    blocks_gas_limit_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_gas_limit_list.append(json_object["gas_limit"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_gas_limit_list)
    plt.xlabel('block')
    plt.ylabel('gas_limit')
    plt.title('Gas limit per block')
    plt.savefig('plots/blocks_gas_limit.png')
    del lines
    del blocks_list
    del blocks_gas_limit_list

def plot_total_difficulty_blocks(): #function for plotting the total difficulty per block
    blocks_list = []
    blocks_total_difficulty_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_total_difficulty_list.append(json_object["total_difficulty"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_total_difficulty_list)
    plt.xlabel('block')
    plt.ylabel('total_difficulty')
    plt.title('Total difficulty per block')
    plt.savefig('plots/blocks_total_difficulty.png')
    del lines
    del blocks_list
    del blocks_total_difficulty_list

def plot_call_count_blocks(): #function for plotting the call count per block
    blocks_list = []
    blocks_call_count_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_call_count_list.append(json_object["call_count"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_call_count_list)
    plt.xlabel('block')
    plt.ylabel('call_count')
    plt.title('Call count per block')
    plt.savefig('plots/blocks_call_count.png')
    del lines
    del blocks_list
    del blocks_call_count_list

def plot_value_total_blocks(): #function for plotting the value total per block
    blocks_list = []
    blocks_value_total_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_value_total_list.append(json_object["value_total"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_value_total_list)
    plt.xlabel('block')
    plt.ylabel('value_total')
    plt.title('Value_total per block')
    plt.savefig('plots/blocks_value_total.png')
    del lines
    del blocks_list
    del blocks_value_total_list

def plot_internal_value_total_blocks(): #function for plotting the internal value total per block
    blocks_list = []
    blocks_internal_value_total_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_internal_value_total_list.append(json_object["internal_value_total"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_internal_value_total_list)
    plt.xlabel('block')
    plt.ylabel('internal_value_total')
    plt.title('Internal value total per block')
    plt.savefig('plots/blocks_internal_value_total.png')
    del lines
    del blocks_list
    del blocks_internal_value_total_list

def plot_internal_value_total_usd_blocks(): #function for plotting the internal value total in usd per block
    blocks_list = []
    blocks_internal_value_total_usd_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_internal_value_total_usd_list.append(json_object["internal_value_total_usd"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_internal_value_total_usd_list)
    plt.xlabel('block')
    plt.ylabel('internal_value_total_usd')
    plt.title('Internal value total in USD per block')
    plt.savefig('plots/blocks_internal_value_total_usd.png')
    del lines
    del blocks_list
    del blocks_internal_value_total_usd_list

def plot_generation_blocks(): #function for plotting the generation per block
    blocks_list = []
    blocks_generation_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_generation_list.append(json_object["generation"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_generation_list)
    plt.xlabel('block')
    plt.ylabel('generation')
    plt.title('Generation per block')
    plt.savefig('plots/blocks_generation.png')
    del lines
    del blocks_list
    del blocks_generation_list

def plot_generation_usd_blocks(): #function for plotting the generation in USD per block
    blocks_list = []
    blocks_generation_usd_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_generation_usd_list.append(json_object["generation_usd"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_generation_usd_list)
    plt.xlabel('block')
    plt.ylabel('generation_usd')
    plt.title('Generation in USD per block')
    plt.savefig('plots/blocks_generation_usd.png')
    del lines
    del blocks_list
    del blocks_generation_usd_list

def plot_fee_total_blocks(): #function for plotting the fee_total per block
    blocks_list = []
    blocks_fee_total_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_fee_total_list.append(json_object["fee_total"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_fee_total_list)
    plt.xlabel('block')
    plt.ylabel('fee_total')
    plt.title('Fee total per block')
    plt.savefig('plots/blocks_fee_total.png')
    del lines
    del blocks_list
    del blocks_fee_total_list

def plot_fee_total_usd_blocks(): #function for plotting the fee total in USD per block
    blocks_list = []
    blocks_fee_total_usd_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_fee_total_usd_list.append(json_object["fee_total_usd"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_fee_total_usd_list)
    plt.xlabel('block')
    plt.ylabel('fee_total_usd')
    plt.title('Fee total in USD per block')
    plt.savefig('plots/blocks_fee_total_usd.png')
    del lines
    del blocks_list
    del blocks_fee_total_usd_list

def plot_reward_blocks(): #function for plotting the reward per block
    blocks_list = []
    blocks_reward_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_reward_list.append(json_object["reward"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_reward_list)
    plt.xlabel('block')
    plt.ylabel('reward')
    plt.title('Reward per block')
    plt.savefig('plots/blocks_reward.png')
    del lines
    del blocks_list
    del blocks_reward_list

def plot_reward_usd_blocks(): #function for plotting the reward in USD per block
    blocks_list = []
    blocks_reward_usd_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_reward_usd_list.append(json_object["reward_usd"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_reward_usd_list)
    plt.xlabel('block')
    plt.ylabel('reward_usd')
    plt.title('Reward in USD per block')
    plt.savefig('plots/blocks_reward_usd.png')
    del lines
    del blocks_list
    del blocks_reward_usd_list

def plot_nonce_blocks(): #function for plotting the nonce per block
    blocks_list = []
    blocks_nonce_list = []
    aa=0
    bb=0
    while aa < 9:
        blocks_file = open("output_data/block_output_data"+str(aa)+".txt", 'r')  
        lines = blocks_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            blocks_list.append(json_object["id"])
            blocks_nonce_list.append(json_object["nonce"])
            if bb != json_object["id"]:
                print("Error detected in line "+str(bb))
                break
            bb+=1
            if bb == 11440633:
                bb+=2
        blocks_file.close()
        aa += 1
        
    plt.plot(blocks_list,blocks_nonce_list)
    plt.xlabel('block')
    plt.ylabel('nonce')
    plt.title('Nonce per block')
    plt.savefig('plots/blocks_nonce.png')
    del lines
    del blocks_list
    del blocks_nonce_list


#def plot_gas_days():
#    days_file = open("output_data/day_output_data.txt", 'r')      
#    lines = days_file.readlines()
#    days_list = []
#   days_gas_list = []
#    for line in lines:      
#        json_object = json.loads(line)
#        days_list.append(json_object["day"])
#        days_gas_list.append(json_object["gas_media"])
#    plt.plot(days_list,days_gas_list)
#    plt.xlabel('day')
#    plt.ylabel('gas media per day')
#    plt.title('Gas media used per day')
#    plt.savefig('plots/day_media_gas_used.png')
#    del lines
#    del days_list
#    del days_gas_list
#    days_file.close()


#----------------------------------------------------------------PLOTS DIRECTORY CREATION

actual_path = os.getcwd()
plot_path = os.path.join(actual_path, 'plots')
if os.path.exists(plot_path) == False:                                 #create folder 'plots' inside actual directory if it doesn't exist yet
    os.mkdir(plot_path)

#plot_gas_blocks()

#plot_gas_limit_blocks()

#plot_tran_blocks()






#plot_value_total_blocks()

#plot_val_total_usd_blocks()

#plot_internal_value_total_blocks()



#plot_call_count_blocks()

#plot_internal_value_total_usd_blocks()

#plot_generation_blocks()

#plot_generation_usd_blocks()

#plot_fee_total_blocks()

#plot_fee_total_usd_blocks()

#plot_reward_blocks()

#plot_reward_usd_blocks()


plot_nonce_blocks()



#plot_size_blocks()

#plot_difficulty_blocks()

#plot_total_difficulty_blocks()


