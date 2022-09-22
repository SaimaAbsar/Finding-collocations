# SNLP Fall 22
# HW1 September 8, 2022
# Author: Saima Absar

# count_bigrams

import os
import argparse
import time
from Preprocess import preprocess
from Pair_generation import pair_generation
from Unigram_freq import count_unigram_freq

# Get the start time
st = time.time()

# Function for the main process
def process(in_file, out_file):
    print("\nPreprocessing data...\n")
    data = preprocess(in_file) #returns a filtered string of words
    print("Computing unigram frequency...\n")
    new_data, unigram_freq = count_unigram_freq(data, out_file) #creates a dict of unigram frequency
    print("Generating bigrams...\n")
    counts, bigram_freq = pair_generation(new_data, out_file) #generates bigrams and frequency counts
    
    # Display the top 100 most frequent bigrams
    print(f"Top 100 most frequent bigrams for {in_file}: ")
    most_common = []
    for key, count in counts.most_common(100):
        key = key.strip()
        most_common.append((key, count))
    print(most_common)

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
            in_file = f"{input_dir}/{file}"
            out_file = output_dir+'/'+file.replace('.txt','')  #name the output files names a/c to input files
            # process the specific file
            process(in_file, out_file)
        
# Get the end time
et = time.time()
# Get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
