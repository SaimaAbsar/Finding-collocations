import math
from collections import OrderedDict

# Compute Pointwise Mutual Information
def pmi(word1, word2, unigram_freq, bigram_freq):
    prob_word1 = unigram_freq[word1] / float(sum(unigram_freq.values()))
    prob_word2 = unigram_freq[word2] / float(sum(unigram_freq.values()))
    prob_word1_word2 = bigram_freq[word1+'-'+word2] / float(sum(bigram_freq.values()))
    return math.log(prob_word1_word2/float(prob_word1*prob_word2),2) 


def compute_pmi(unigram_freq, bigram_freq, output_dir):
    max_freq = max(bigram_freq.values())    #find the max frequency of bigrams
    pair_pmi = {}
    for pair in bigram_freq.keys():
        if bigram_freq[pair] < max_freq and bigram_freq[pair] > 1:
            words = pair.split('-')
            #print(words)
            word1 = words[0]
            word2 = words[1]
            pair_pmi[pair] = pmi(word1, word2, unigram_freq, bigram_freq)
    sorted_pmi = OrderedDict(sorted(pair_pmi.items(), key=lambda t: t[1], reverse=True))
    
    collocations = [[str(key),float(value)] for key,value in sorted_pmi.items()]

    path = output_dir+'_collocations.txt'
    out_file = open(path, 'w')
    for i in collocations:
        out_file.write("%s, %s\n" %(i[0], i[1]))
    out_file.close()

    return(collocations)