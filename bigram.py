import languagemodel as lm

def buildModel(data, lmda, k, outputfile):
  vocab = lm.getVocab(data, k)
  counts = lm.getCounts(data, vocab, 2)
  context_counts = lm.getCounts(data, vocab, 1)
  for bigram, count in counts.items():
      context_count = context_counts[bigram.split()[0]]
      p = lm.calcProbability(count, context_count, lmda, len(vocab))
      outputfile.write("{} {}\n".format(bigram, p))


def main():
    output = open("models/bigram.txt", "w")
    data = lm.getLines("data/train.txt", 2)
    buildModel(data, 1, 2, output)

if __name__ == '__main__':
    main()


