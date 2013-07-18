def dictBuilder():
    afinnfile = open("AFINN-111.txt")
    scores = {} #initializes empty dict
    for line in afinnfile:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores
        
if __name__ == "__main__":
    scores = dictBuilder()
    print scores.items()
