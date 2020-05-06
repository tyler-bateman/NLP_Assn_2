
#returns the given line with n start symbols and 1 end symbol.
def wrap(line, n):
    for i in range(n):
        line = "<s> " + line 
    return line.strip() + " </s>"


# returns the tokenized sentences from the given dataset file, with n start symbols
# formatted as a 2-d array
def getLines(filename, n):
    data_file = open(filename, "r")
    lines = []
    for line in data_file:
        lines.append(wrap(line, n).split())
    return lines


# returns the vocabulary as a set
# any tokens that occur k or fewer times are ignored
def getVocab(lines, k):
    #A dict is used to track how many times each token occurs
    token_counts = {}
    for line in lines:
        for token in line:
            if token == "<s>":
                continue
            if token in token_counts:
                token_counts[token] += 1
            else:
                token_counts[token] = 1
    
    #Remove any token that occurs k or fewer times
    for token, occurrences in token_counts.items():
        if occurrences <= k:
            del token_counts[token]
    v = set(token_counts.keys())
    v.add("<UNK>")    
    return set(token_counts.keys())


def buildCounts(inputfile,  n):
    data = getLines(inputfile, n - 1)
    vocab = getVocab(data, k)
    counts = {}
    ngrams = {}
    for line in data:
        for i in range(len(line) - n + 1):
            ngram = ""
            for j in range(i, i + n - 1):
                token = line[j] if line[j] in vocab else "<UNK>"
                ngram = ngram + " " + token
            
            if ngram in counts:
                counts[ngram] += 1
            else:
                counts[ngram] = 1
            
            ngram = ngram + line[i + n - 1]
            
            if ngram in counts:
                counts[ngram] += 1
            else:
                counts[ngram] = 1
            ngrams.add(ngram)
    return (counts, ngrams)

def writeModelToFile(ngrams, counts, lmda, vSize, filename):
    outputfile = open(filename, "w")
    for ngram in ngrams:
        context = "".join(ngram.split().pop(-1))
        p = (counts[ngram] + lmda) / (counts[context] + (vSize * lmda))
        #TODO: Write to output file 
        
