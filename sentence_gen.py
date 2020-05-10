import random as r
import math

MODELS = {}

def retrieve_model(filename):
    m_file = open(filename, "r")
    model = {}
        
    for line in m_file:
        line_arr = line.split()
        prob = float(line_arr.pop())
        token = line_arr.pop()
        context = " ".join(line_arr)
        
        if context in model:
            model[context][0].append(token)
            model[context][1].append(prob)
        else:   
            choices = [token] 
            weights = [prob]
            model[context] = (choices, weights)

    
    return model


def nextToken(model, context):
    choices, probs = model[context]
    i = r.choices(range(len(choices)), weights = probs, k = 1)[0]
    return (choices[i], probs[i])

def gen_sentences(num, n):
     sentences = []
     for i in range(num):
         totalProb = 0.0
         model = MODELS[n]
         sentence = ""
         #For unigrams, start out with one word already there to avoid array index out of bounds
         if n == 1:
            choice = nextToken(model, "")
            sentence = choice[0]
            totalProb = math.log(choice[1])
         for j in range(n - 1):
             sentence = sentence + "<s> "
         sentence = sentence.strip()
         sentence = sentence.split()
         while sentence[-1] != "</s>":
            context = " ".join(sentence[(0 - n + 1):]) if n != 1 else ""
            
            #If the context does not appear in the model, try again with the n-1 model
            m_number = n - 1 
            while context not in model:
                model = MODELS[m_number]
                context = context.split()
                context.pop(0)
                context = " ".join(context)
                m_number -= 1
            choice = nextToken(model, context)
            sentence.append(choice[0])
            totalProb += math.log(choice[1])
         sentences.append((sentence, totalProb))
     return sentences

def format(sentence):
    sentence.pop()
    while sentence[0] == "<s>":
        del sentence[0]
    return " ".join(sentence) + ".\n"

def main():
    MODELS[1] = retrieve_model("models/unigram.txt")
    MODELS[2] = retrieve_model("models/bigram.txt")
    MODELS[3] = retrieve_model("models/trigram.txt")
   
    trigram_sentences = gen_sentences(10, 3)
    bigram_sentences = gen_sentences(10, 2)
    unigram_sentences = gen_sentences(10, 1)


    output = open("report/generated_sentences.txt", "w")

    output.write("Sentences generated with unigram model:\n")
    for sentence in unigram_sentences:
        output.write(format(sentence[0]))
        output.write('probability: {}\n\n'.format(sentence[1]))
        
    
    output.write('\n\nSentences generated with bigram model:\n')

    for sentence in bigram_sentences:
        output.write(format(sentence[0]))
        output.write('probability: {}\n\n'.format(sentence[1]))

    output.write('\n\nSentences generated with trigram model:\n')

    for sentence in trigram_sentences:
        output.write(format(sentence[0]))
        output.write('probability: {}\n\n'.format(sentence[1]))

if __name__ == '__main__':
    main()
