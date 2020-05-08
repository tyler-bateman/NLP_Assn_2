import languagemodel as lm

def buildModel(data, lmda, k, outputfile):
  vocab = lm.getVocab(data, k)
  counts = lm.getCounts(data, vocab, 2)
  context_counts = lm.getCounts(data, vocab, 1)
  for bigram, count in counts.items():
      context_count = context_counts[bigram.split()[0]]
      p = lm.calcProbability(bigram, count, context_count, lmda, len(vocab))
      outputfile.write("{} {}\n".format(bigram, p))


def main():
    output = open("bigram.txt", "w")
    data = lm.getLines("train.txt", 2)
    buildModel(data, 0, 0, output)
            
main()


