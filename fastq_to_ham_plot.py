# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
import itertools

def getSeqs(fastq_file):
    #Parse a FASTQ for sequence identities and corresponding sequences
    lines = []
    f = open(fastq_file)
    for line in f:
    	if line[0] in ["A","T", "C", "G", "N"]: lines.append(line.rstrip())
    f.close()
    return lines

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   for i in xrange(len(str1)):
       if str1[i] == 'N' or str2[i] == 'N':
           diffs += 1
       elif str1[i] != str2[i]:
           diffs += 1
       else:
           continue
   return diffs

#Make some kind of plot that contains the data you've calculated.
fastq= "CTGATC.fastq"
seq_list = getSeqs(f)
hamming_distances = [hamDist(seq1, seq2) for seq1, seq2 in itertools.combinations(seq_list, 2)]
plt.scatter(range(1, len(hamming_distances) + 1), hamming_distances)
plt.xlabel('Sequence pair')
plt.ylabel('Hamming Distance')
plt.savefig('hamming_plot.png')
