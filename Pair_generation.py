from collections import Counter

# Pair generation   
def pair_generator(text):
    previous_word = ''
    for word in text:
        if previous_word and word:
            yield f'{previous_word}-{word}' #combine each word with its next word
        previous_word = word or previous_word

# Frequency count
def count_freq(pairs):
    counts = Counter(pairs)
    return counts

# Create unique pair list
def find_unique_pair(bigram_freq):
    pair_list = []
    for k in bigram_freq.keys():
        pair_list.append(k)   
    return(pair_list)

def pair_generation(filteredtext, output_dir):
    filteredtext = filteredtext.split()
    pairs = []
    for pair in pair_generator(filteredtext):
        pairs.append(pair)
    
    counts = count_freq(pairs)
    path1 = output_dir+'_bigram_freq.txt'
    out_file = open(path1, 'w')
    dict = {}   #save the bigram frequency as a dictionary
    for key, count in counts.most_common():
        key = key.strip()
        dict[key] = count
        out_file.write("%s: %s\n" %(str(key), count))
    out_file.close()
    
    unique_pairs = find_unique_pair(dict)
    path2 = output_dir+'_wordpairs.txt'
    text = open(path2, 'w')   #to keep a record of the unique word-pairs
    for pair in unique_pairs:
        text.write("%s\n" %(pair))
    text.close()

    return(counts, dict)