
from collections import OrderedDict
import numpy as np


# Compute t-test
def t_test(word1, word2, unigram_freq, bigram_freq):
    N = float(sum(unigram_freq.values()))
    prob_word1 = unigram_freq[word1] / N
    prob_word2 = unigram_freq[word2] / N
    mu = float(prob_word1*prob_word2)
    x = float(bigram_freq[word1+'-'+word2] / N)
    t = float((x-mu)/np.sqrt(x/N))
    # the critcal value for alpha=0.001 is 3.091
    if t>3.091: return(t)   # assign a score of 1 if null hypothesis rejected
    else: return(0)


def compute_t_test(unigram_freq, bigram_freq, output_dir):
    max_freq = max(bigram_freq.values())    #find the max frequency of bigrams
    pair_ttest = {}
    for pair in bigram_freq.keys():
        if bigram_freq[pair] < max_freq and bigram_freq[pair] > 5:  #filtering out the pairs the most freuent and least frequent pairs
            words = pair.split('-')
            word1 = words[0]
            word2 = words[1]
            pair_ttest[pair] = t_test(word1, word2, unigram_freq, bigram_freq)
    # accumulates the pairs that has t-test score of 1
    new_dict = {key: val for key,val in pair_ttest.items() if val != 0} 
    sorted_dict = OrderedDict(sorted(new_dict.items(), key=lambda t: t[1], reverse=True))
    collocations = [[key,float(value)] for key,value in sorted_dict.items()]
    
    path = output_dir+'_collocations.txt'
    out_file = open(path, 'w')
    for i in collocations:
        out_file.write("%s, %s\n" %(i[0], i[1]))
    out_file.close()

    return(collocations)