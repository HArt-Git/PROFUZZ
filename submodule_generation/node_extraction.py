#Note: Here the submodule (submodule.v) should be given"####

import sys
import glob
import math
import torch
import re, random



import numpy as np
import networkx as nx
import collections

import h5py
from sklearn.preprocessing import MinMaxScaler
from networkx.readwrite import json_graph
import json
import pandas as pd
import time
from sklearn.preprocessing import LabelEncoder
import torch.nn.functional as F
start_time = time.time()

from google.colab import drive
drive.mount('/content/drive')

def verilog_to_bench(v_dir):
    with open(f'{v_dir}') as f:
        readline=f.read().split(";")
   
    clean_n = [i.replace("\n"," ") for i in readline]
   

   
    clean_white = [' '.join(i.split()) for i in clean_n]
  
       wire_list = []
    for line in clean_white:

        if 'wire' in line:

            wires = line

            wire_clean = re.split(r'[ ,]', wires)
            wire_empty_str_clean = [i for i in wire_clean if i]
            wire_empty_str_clean.remove('wire')
           # print(wire_empty_str_clean)
            for i in wire_empty_str_clean:
                wire_w = f'WIRE({i}) \n'
                wire_list.append(i)
               # print(wire_list)
                #bench_write.write(wire_w)

    #bench_write.close()
    return wire_list

if __name__ == '__main__':

    bench_dir = '' # Replace with your rtl source directory
    log_file = open(f'{bench_dir}/verilog2bench_log.txt', 'w')
    # Returns a list of names in list files.
    files = glob.glob(bench_dir +'/**/*.v',
                       recursive = True)
    files = sorted(files)

    print(files)
    for indx, file in enumerate(files):
        if 'lib' not in file:
            log_file.write(file)
            li=verilog_to_bench(file)
    log_file.close()

print(li)

import sys
import random

def generate_random_sample(low, high, percentage):
    # Calculate the total number of numbers in the range [low, high]
    total_numbers = high - low + 1

    # Calculate how many numbers to sample based on the percentage
    sample_size = int((percentage / 100) * total_numbers)

    # Generate the random sample
    random_sample = random.sample(range(low, high + 1), sample_size)

    return random_sample


low = 0    # Lowest number in range
high = len(li) -1  # Highest number in range
percentage = 50  # Percentage of target nets to sample


#random.seed(100)


sample = generate_random_sample(low, high, percentage)

#for x in sample:
 # print(li[x])

with open("target.txt", "w") as f:
  for x in sample:
    f.write(str(li[x]) + " ")
