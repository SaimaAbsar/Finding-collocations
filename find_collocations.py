# SNLP Fall 22
# HW1 September 8, 2022
# Author: Saima Absar

# find_collocations

import argparse
import time
from t_test import compute_t_test
from PMI import compute_pmi
import pandas as pd
import os

# Get the start time
st = time.time()

# Function for the main process
def process(in_file, output_dir):
    unigram_freq = dict(pd.read_csv(output_dir+'_unigram_freq.txt', delimiter=": ", header=None, engine='python').to_dict(orient='split')['data'])
    bigram_freq = dict(pd.read_csv(output_dir+'_bigram_freq.txt', delimiter=": ", header=None, engine='python').to_dict(orient='split')['data'])
    
    collocations = compute_t_test(unigram_freq, bigram_freq, output_dir)  #determine the collocations using t-test
    print(f"Top 100 collocations for {in_file}: ")
    print(collocations[:100])

if __name__ == '__main__':  
    # User input for input and output directories
    parser = argparse.ArgumentParser("input directory")
    parser.add_argument("inpath", help="path to input directory", type=str)
    parser.add_argument("outpath", help="path to ouput directory", type=str)
    args = parser.parse_args()
    input_dir = args.inpath
    output_dir = args.outpath
    
    # Iterate through all files in the the input directory
    # read the text files and process it
    for file in os.listdir(input_dir):
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            # name the output files names a/c to input files
            out_file = output_dir+'/'+file.replace('.txt','')
            # process the specific file
            process(file, out_file)

# Get the end time
et = time.time()
# Get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
