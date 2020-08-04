import numpy as np
import re
import scipy.spatial as sp


def count_lines(txt_file):
    n = 0
    with open(txt_file, 'r') as file:
        for line in file:
            n += 1
    return n


if __name__ == '__main__':
    filename = 'sentences.txt'
    with open(filename) as f:
        lines = count_lines(filename)
        words = {}
        lcount, wcount = 0, 0
        for line in f:
            p = re.compile(r"[^a-z]+")
            tokens = p.split(line.lower())
            tokens.pop()
            for token in tokens:
                if token not in words:
                    words[token] = {
                        "index": wcount,
                        "frequency": [0] * lines
                    }
                    wcount += 1
                elif words[token]["frequency"][lcount] != 0:
                    continue
                words[token]["frequency"][lcount] = tokens.count(token)
            lcount += 1
    matrix = np.zeros((lines,len(words)))
    for word in words:
        i = 0
        j = words[word]['index']
        for kol in words[word]['frequency']:
            matrix[i,j]=kol
            i+=1

    a = matrix[0,]
    print(a)
    answer= ''
    for i in range(1,lines):
        b=matrix[i,]

        answer = answer + str(sp.distance.cosine(a,b)) + ' '
    print(answer)

    filename_1 = open('submission-1.txt','w')
    filename_1.write(answer)
    filename_1.close()
