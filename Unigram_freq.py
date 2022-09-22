
from collections import OrderedDict

# Determine unigram frequency
def count_unigram_freq(text_string, output_dir):
    
    dict = {}   #save the bigram frequency as a dictionary
    words = text_string.split()
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    new_text = ''
    for word in words:
        if dict[word]>1:
            new_text += " "+word 
    sorted_dict = OrderedDict(sorted(dict.items(), key=lambda t: t[1], reverse=True))
    
    path = output_dir+'_unigram_freq.txt'
    out_file = open(path, 'w')   #to keep a record of the unigram frequency
    for words in sorted_dict:
        # filtering out the words that occurs only once
        if sorted_dict[words] > 1:
            out_file.write("%s: %s\n" %(str(words), sorted_dict[words]))
    out_file.close()

    return (new_text, sorted_dict)