import random as r



def retrieve_model(filename):
    m_file = open(filename, "r")
    model = {}
        
    for line in m_file:
        line_arr = line.split()
        prob = float(line_arr.pop())
        token = line_arr.pop()
        context = "".join(line_arr)

        if context in model:
            model[context][0].append(token)
            model[context][1].append(prob)
        else:
            choices = [token] 
            weights = [prob]
            model[context] = (choices, weights)

    
    return model


def nextToken(model, context):
    rand = r.random()
    i = 0
    while rand > 0 and i < len(model):
        if model[i][0] == context:
            rand -= model[i][2]
        i += 1 
    return model[i][1]


def gen_sentences(model, num):
     n = len(model[0][0].split()) + 1
     sentences = []
     for i in range(num):
         #For unigrams, start out with one word already there to avoid array index out of bounds
         sentence = "" if n > 1 else nextToken(model, "")
         for j in range(n - 1):
             sentence = sentence + "<s> "
         sentence = sentence.strip()
         sentence = sentence.split()
         while sentence[-1] != "</s>":
            context = sentence[(0 - n + 1):] if n != 1 else ""
            sentence.append(nextToken(model, context))
            print sentence        
         sentences.append(sentence)

def main():
    sentences = gen_sentences(retrieve_model("models/unigram.txt"), 10)
    for s in sentences:
        print s

main()
