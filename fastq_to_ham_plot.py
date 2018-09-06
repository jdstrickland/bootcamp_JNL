# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt
import itertools

f = open(CTGATC.fastq)

def getSeqs(fastq_file):
    #Parse a FASTQ for sequence identities and corresponding sequences
    seqences = {}
    return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs










#Make some kind of plot that contains the data you've calculated.
seq_list = getSeqs(f)
f.close()
hamming_distances = [hamDist(seq1, seq2) for seq1, seq2 in itertools.combinations(seq_list, 2)]
plt.scatter(range(1, len(hamming_distances) + 1), hamming_distances)
plt.xlabel('Sequence pair')
plt.ylabel('Hamming Distance')
plt.savefig('hamming_plot.png')
