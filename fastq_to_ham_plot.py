# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub

import matplotlib.pyplot as plt

def getSeqs(fastq_file):
    #Parse a FASTQ for sequence identities and corresponding sequences
    lines = []
    counter = 0
    f = open(fastq_file)
    for line in f:
    	if line[0] in ["A","T", "C", "G", "R"]: lines.append(line.rstrip())
    return lines

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

#Make some kind of plot that contains the data you've calculated.
fastq= "CTGATC.fastq"
getSeqs(fastq)
plt.show()
