# Preprocessing Data

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
from nltk.tag.perceptron import PerceptronTagger
from nltk.corpus import stopwords
import re
import string

# Remove stopwords
def remove_stopwords(words):
    print("Removing stopwords..")
    # collect the set of stopwords from the nltk english database
    stopset = set(stopwords.words('english'))
    filtered = []
    for w in words:
        # remove the stopwords
        if not w in stopset:
            filtered.append(w) 
    #return(filtered)
    return(filtered)

# My own generation of tokens
def generate_tokens(content):
    print("Generating tokens..")
    # collected tokens only contain letters a-z upper OR lower
    match_pattern = re.findall(r'\b[a-zA-Z]{3,15}\b', content)
    words = []
    for word in match_pattern:
        words.append(str(word))
    words = [w.lower() for w in words]
    return words

# Parts of Speech tagging to keep only the nouns and adjectives
def tag_pos(tokens, tagger):
    print("Tagging tokens..")
    #tokens = tokens[0:100000]
    filtered = ''
    tagged = tagger.tag(tokens)
    for tag in tagged:
      if tag[1][0]=='N' or tag[1][0]=='J':
          filtered += " "+tag[0] 
    print('tagging done!\n')
    return(filtered)



# main function
def preprocess(path):  
    file = open(path) #Loading the data
    content = file.read() #converts into string
    tokens = generate_tokens(content) #return the tokens
    filtered1 = remove_stopwords(tokens) #remove stopwords
    tagger = PerceptronTagger() 
    filtered2 = tag_pos(filtered1, tagger) #return only nouns and adjective
    return(filtered2)
