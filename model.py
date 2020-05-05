
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
    return token_counts.keys()


vocab = getVocab(getLines("train.txt", 2), 1) 
for i in range(20):
    print vocab[i]
