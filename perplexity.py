from sentence_gen import retrieve_model 
import languagemodel as lm
import math
from unigram import countTokens 

#Calculates the perplexity of the test data
#param test_data: the data to be tested
#                 list of strings
#param model: The dictionary containing the model
#             Keys -> String
#             Values -> (List of Strings, list of floats)
#param vocab: The set of tokens in the vocabulary
#param n: The size of n-grams
#param lmda: The smoothing constant
#param mSize: The size of the training data
def perplexity(test_data, model, vocab, n, lmda, mSize):
    psum = float(0.0)
    length = 0
    for line in test_data:
        for i in range(n - 1, len(line)):
            token = line[i] if line[i] in vocab else '<UNK>'
            context = ''
            for j in range(i - (n + 1), i):
                context = context + (line[j] if line[j] in vocab else '<UNK>') + ' '
            context = context.strip()

            if context in model:
                (tokens, probs) = model[context]
                psum += math.log(probs[tokens.index(token)])
            else:
                
                psum += math.log(lmda) - math.log(mSize + len(vocab))

            length += 1
    
    return math.exp(-psum / length)

def main():
    output = open("report/perplexity.txt", "w")
    lmda = 2

    #Unigram
    data = lm.getLines("data/test.txt", 1)
    vocab = lm.getVocab(data, 2)
    mSize = countTokens(data)
    model = retrieve_model("models/unigram.txt")
    output.write("\nPerplexity of test data with unigram model:\n")
    output.write(str(perplexity(data, model, vocab, 1, lmda, mSize)))

    #Bigram
    data = lm.getLines("data/test.txt", 2)
    vocab = lm.getVocab(data, 2)
    mSize = countTokens(data)
    model = retrieve_model("models/bigram.txt")
    output.write('\nPerplexity of test data with bigram model:\n')
    output.write(str(perplexity(data, model, vocab, 2, lmda, mSize)))
    
    #Trigram
    data = lm.getLines("data/test.txt", 3)
    vocab = lm.getVocab(data, 2)
    mSize = countTokens(data)
    model = retrieve_model('models/trigram.txt')
    output.write('\nPerplexity of test data with trigram model:\n')
    output.write(str(perplexity(data, model, vocab, 3, lmda, mSize)))
    print('done')

if __name__ == '__main__':
    main()    
