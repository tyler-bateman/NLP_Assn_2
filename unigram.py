import languagemodel as lm

def countTokens(data):
    count = 0
    for line in data:
        count += len(line)
    return count


def buildModel(data, lmda, k, outputfile):
  vocab = lm.getVocab(data, k)
  counts = lm.getCounts(data, vocab, 1)
  context_counts = countTokens(data)
  for token, count in counts.items():
      p = lm.calcProbability(count, context_counts, lmda, len(vocab))
      outputfile.write("{} {}\n".format(token, p))


def main():
    output = open("models/unigram.txt", "w")
    data = lm.getLines("data/train.txt", 1)
    buildModel(data, 1, 2, output)

if __name__ == '__main__':
    main()
