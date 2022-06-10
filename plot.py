#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#----------------------------------------------------------------IMPORTS

import os
import csv
import json
import matplotlib.pyplot as plt

#----------------------------------------------------------------FUNCTIONS

def plot_gas_blocks():
    blocks_file = open("output_data/block_output_data.txt", 'r')  
    lines = blocks_file.readlines()
    blocks_list = []
    blocks_gas_list = []
    for line in lines:      
        json_object = json.loads(line)
        blocks_list.append(json_object["id"])
        blocks_gas_list.append(json_object["gas_used"])
    plt.plot(blocks_list,blocks_gas_list)
    #ax = plt.gca()
    #ax.set_ylim([0, 30000000])
    plt.xlabel('block')
    plt.ylabel('gas used')
    plt.title('Gas used per block')
    plt.savefig('plots/blocks_gas_used.png')
    del lines
    del blocks_list
    del blocks_gas_list
    blocks_file.close()

def plot_gas_days():
    days_file = open("output_data/day_output_data.txt", 'r')      
    lines = days_file.readlines()
    days_list = []
    days_gas_list = []
    for line in lines:      
        json_object = json.loads(line)
        days_list.append(json_object["day"])
        days_gas_list.append(json_object["gas_media"])
    plt.plot(days_list,days_gas_list)
    plt.xlabel('day')
    plt.ylabel('gas media per day')
    plt.title('Gas media used per day')
    plt.savefig('plots/day_media_gas_used.png')
    del lines
    del days_list
    del days_gas_list
    days_file.close()


#----------------------------------------------------------------PLOTS DIRECTORY CREATION

actual_path = os.getcwd()
plot_path = os.path.join(actual_path, 'plots')
if os.path.exists(plot_path) == False:                                 #create folder 'plots' inside actual directory if it doesn't exist yet
    os.mkdir(plot_path)

plot_gas_blocks()

#plot_gas_days()
