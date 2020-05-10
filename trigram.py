import languagemodel as lm

def buildModel(data, lmda, k, outputfile):
  vocab = lm.getVocab(data, k)
  counts = lm.getCounts(data, vocab, 3)
  context_counts = lm.getCounts(data, vocab, 2)
  for trigram, count in counts.items():
      t_split = trigram.split()
      context_count = context_counts["{} {}".format(t_split[0], t_split[1])]
      p = lm.calcProbability(count, context_count, lmda, len(vocab))
      outputfile.write("{} {}\n".format(trigram, p))


def main():
    output = open("models/trigram.txt", "w")
    data = lm.getLines("data/train.txt", 3)
    buildModel(data, 1, 2, output)

if __name__ == '__main__':
    
    main()


