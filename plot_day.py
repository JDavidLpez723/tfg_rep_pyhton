#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

import os
import json
import matplotlib.pyplot as plt
from datetime import date

#----------------------------------------------------------------FUNCTIONS

def plot_gas_days():      #function for plotting the gas per day
    days_list = []
    days_gas_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_gas_list.append(json_object["gas_used"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_gas_list)
    plt.xlabel('date')
    plt.ylabel('gas used')
    plt.title('Gas used per day')
    plt.savefig('plots_days/days_gas_used.png')
    del lines
    del days_list
    del days_gas_list

def plot_tran_days(): #function for plotting the transaction count per day
    days_list = []
    days_tran_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_tran_list.append(json_object["transaction_count"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_tran_list)
    plt.xlabel('date')
    plt.ylabel('transaction count')
    plt.title('Transaction count per day')
    plt.savefig('plots_days/days_tran_count.png')
    del lines
    del days_list
    del days_tran_list

def plot_value_total_usd_days(): #function for plotting the value total usd per day
    days_list = []
    days_val_total_usd_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_val_total_usd_list.append(json_object["value_total_usd"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_val_total_usd_list)
    plt.xlabel('date')
    plt.ylabel('value total in usd')
    plt.title('Value total in USD per day')
    plt.savefig('plots_days/days_value_total_usd.png')
    del lines
    del days_list
    del days_val_total_usd_list

def plot_size_days(): #function for plotting the size per day
    days_list = []
    days_size_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_size_list.append(json_object["size"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_size_list)
    plt.xlabel('date')
    plt.ylabel('size')
    plt.title('Size per day')
    plt.savefig('plots_days/days_size.png')
    del lines
    del days_list
    del days_size_list

def plot_difficulty_days(): #function for plotting the difficulty per day
    days_list = []
    days_difficulty_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_difficulty_list.append(json_object["difficulty"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_difficulty_list)
    plt.xlabel('date')
    plt.ylabel('difficulty')
    plt.title('Difficulty per day')
    plt.savefig('plots_days/days_difficulty.png')
    del lines
    del days_list
    del days_difficulty_list

def plot_gas_limit_days(): #function for plotting the gas limit per day
    days_list = []
    days_gas_limit_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_gas_limit_list.append(json_object["gas_limit"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_gas_limit_list)
    plt.xlabel('date')
    plt.ylabel('gas_limit')
    plt.title('Gas limit per day')
    plt.savefig('plots_days/days_gas_limit.png')
    del lines
    del days_list
    del days_gas_limit_list

def plot_total_difficulty_days(): #function for plotting the total difficulty per day
    days_list = []
    days_total_difficulty_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_total_difficulty_list.append(json_object["total_difficulty"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_total_difficulty_list)
    plt.xlabel('date')
    plt.ylabel('total_difficulty')
    plt.title('Total difficulty per day')
    plt.savefig('plots_days/days_total_difficulty.png')
    del lines
    del days_list
    del days_total_difficulty_list

def plot_call_count_days(): #function for plotting the call count per day
    days_list = []
    days_call_count_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_call_count_list.append(json_object["call_count"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_call_count_list)
    plt.xlabel('date')
    plt.ylabel('call_count')
    plt.title('Call count per day')
    plt.savefig('plots_days/days_call_count.png')
    del lines
    del days_list
    del days_call_count_list

def plot_value_total_days(): #function for plotting the value total per day
    days_list = []
    days_value_total_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_value_total_list.append(json_object["value_total"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_value_total_list)
    plt.xlabel('date')
    plt.ylabel('value_total')
    plt.title('Value_total per day')
    plt.savefig('plots_days/days_value_total.png')
    del lines
    del days_list
    del days_value_total_list

def plot_internal_value_total_days(): #function for plotting the internal value total per day
    days_list = []
    days_internal_value_total_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_internal_value_total_list.append(json_object["internal_value_total"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_internal_value_total_list)
    plt.xlabel('date')
    plt.ylabel('internal_value_total')
    plt.title('Internal value total per day')
    plt.savefig('plots_days/days_internal_value_total.png')
    del lines
    del days_list
    del days_internal_value_total_list

def plot_internal_value_total_usd_days(): #function for plotting the internal value total in usd per day
    days_list = []
    days_internal_value_total_usd_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_internal_value_total_usd_list.append(json_object["internal_value_total_usd"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_internal_value_total_usd_list)
    plt.xlabel('date')
    plt.ylabel('internal_value_total_usd')
    plt.title('Internal value total in USD per day')
    plt.savefig('plots_days/days_internal_value_total_usd.png')
    del lines
    del days_list
    del days_internal_value_total_usd_list

def plot_generation_days(): #function for plotting the generation per day
    days_list = []
    days_generation_list = []
    aa=0
    while aa < 1:
        #days_file = open("day_media_output_data/day_media_output_data"+str(aa)+"_sin_bloque_0.txt", 'r')
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_generation_list.append(json_object["generation"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_generation_list)
    plt.xlabel('date')
    plt.ylabel('generation')
    plt.title('Generation per day')
    #plt.savefig('plots_days_sin_bloque_0/days_generation.png')
    plt.savefig('plots_days/days_generation.png')
    del lines
    del days_list
    del days_generation_list

def plot_generation_usd_days(): #function for plotting the generation in USD per day
    days_list = []
    days_generation_usd_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_generation_usd_list.append(json_object["generation_usd"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_generation_usd_list)
    plt.xlabel('date')
    plt.ylabel('generation_usd')
    plt.title('Generation in USD per day')
    plt.savefig('plots_days/days_generation_usd.png')
    del lines
    del days_list
    del days_generation_usd_list

def plot_fee_total_days(): #function for plotting the fee_total per day
    days_list = []
    days_fee_total_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_fee_total_list.append(json_object["fee_total"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_fee_total_list)
    plt.xlabel('date')
    plt.ylabel('fee_total')
    plt.title('Fee total per day')
    plt.savefig('plots_days/days_fee_total.png')
    del lines
    del days_list
    del days_fee_total_list

def plot_fee_total_usd_days(): #function for plotting the fee total in USD per day
    days_list = []
    days_fee_total_usd_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_fee_total_usd_list.append(json_object["fee_total_usd"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_fee_total_usd_list)
    plt.xlabel('date')
    plt.ylabel('fee_total_usd')
    plt.title('Fee total in USD per day')
    plt.savefig('plots_days/days_fee_total_usd.png')
    del lines
    del days_list
    del days_fee_total_usd_list

def plot_reward_days(): #function for plotting the reward per day
    days_list = []
    days_reward_list = []
    aa=0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_reward_list.append(json_object["reward"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_reward_list)
    plt.xlabel('date')
    plt.ylabel('reward')
    plt.title('Reward per day')
    plt.savefig('plots_days/days_reward.png')
    del lines
    del days_list
    del days_reward_list

def plot_reward_usd_days(): #function for plotting the reward in USD per day
    days_list = []
    days_reward_usd_list = []
    aa = 0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')  
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            days_list.append(date.fromisoformat(json_object["date"]))
            days_reward_usd_list.append(json_object["reward_usd"])
        days_file.close()
        aa += 1
        
    plt.plot(days_list,days_reward_usd_list)
    plt.xlabel('date')
    plt.ylabel('reward_usd')
    plt.title('Reward in USD per day')
    plt.savefig('plots_days/days_reward_usd.png')
    del lines
    del days_list
    del days_reward_usd_list

def internal_total_diff():  #function that check in how many days the internal_value_total is bigger than the value_total
    global_count = 0
    int_bigger_count = 0
    aa = 0
    while aa < 1:
        days_file = open("day_media_output_data/day_media_output_data"+str(aa)+".txt", 'r')
        lines = days_file.readlines()
        for line in lines:
            json_object = json.loads(line)
            global_count += 1
            if json_object["internal_value_total"] > json_object["value_total"]:
                int_bigger_count += 1
        days_file.close()
        aa += 1
    print("N of days: "+str(global_count))
    print("N of days with internal_value_total bigger: "+str(int_bigger_count))
    percentage =  round(((int_bigger_count * 100) / global_count), 2)
    print("The "+str(percentage)+ "% of the days, internal_value_total is bigger than value_total")





#----------------------------------------------------------------PLOTS DIRECTORY CREATION

actual_path = os.getcwd()
plot_path = os.path.join(actual_path, 'plots_days')
if os.path.exists(plot_path) == False:                                 #create folder 'plots_days' insdatee actual directory if it doesn't exist yet
    os.mkdir(plot_path)

actual_path = os.getcwd()
plot_path = os.path.join(actual_path, 'plots_days_sin_bloque_0')
if os.path.exists(plot_path) == False:                                 #create folder 'plots_days_sin_bloque_0' insdatee actual directory if it doesn't exist yet
    os.mkdir(plot_path)

#plot_gas_days()

#plot_gas_limit_days()

#plot_tran_days()

#plot_value_total_days()

#plot_value_total_usd_days()

#plot_internal_value_total_days()

#plot_call_count_days()

#plot_internal_value_total_usd_days()

#plot_generation_days()

#plot_generation_usd_days()

#plot_fee_total_days()

#plot_fee_total_usd_days()

#plot_reward_days()

#plot_reward_usd_days()

#plot_size_days()

#plot_difficulty_days()

#plot_total_difficulty_days()

#internal_total_diff()