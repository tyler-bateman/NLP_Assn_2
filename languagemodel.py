#returns the given line with n start symbols and 1 end symbol.
def wrap(line, n):
    for i in range(n - 1):
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
            if token in token_counts:
                token_counts[token] += 1
            else:
                token_counts[token] = 1
    
    #exclude any token that occurs k or fewer times
    pairs = token_counts.items()
    v = set()
    for token, occurrences in pairs:
        if occurrences > k:
           v.add(token) 
    v.add("<UNK>")    
    return v 

#returns the number of occurrences of each token
def getCounts(data, vocab, n):
    counts = {}
    for line in data:
        for i in range(len(line) - n + 1):
            ngram = line[i] 
            for j in range(i + 1, i + n ):
                token = line[j] if line[j] in vocab else "<UNK>"
                ngram = ngram + " " + token
            
            if ngram in counts:
                counts[ngram] += 1
            else:
                counts[ngram] = 1
    return counts


#Caluculates the probability that the ngram occurs
def calcProbability(count, context_count, lmda, vSize):
    return float(count + lmda) / (context_count + (vSize * lmda)) 

#Calculates the probability that the ngram occurs in log space
def calcLogProb(count, context_count, lmda, vSize):
    import math
    return math.log(float(count + lmda)) - math.log(context_count + (vSize * lmda))



