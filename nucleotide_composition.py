# set the name of the input sequence file
filename = 'dna.txt'

# open the input file & assign to file handle called "infile"
infile = open(filename, 'r') #creating a file handle

# read the file & save contents of the file as a variable
dna_sequence = infile.read().rstrip() # the .rstrip() method removes the "enter" return at the end of the code, leaves only the sequence

#close the file connection
infile.close()

# Find the length of the DNA sequence
seqlen = len(dna_sequence)
print("Sequence length:", seqlen, "bp")

# count the number of each nucleotide in the sequence and divide by total number of characters

freqA = dna_sequence.count("A") / seqlen
freqC = dna_sequence.count("C") / seqlen
freqG = dna_sequence.count("G") / seqlen
freqT = dna_sequence.count("T") / seqlen
freqGC = round((dna_sequence.count("G") + dna_sequence.count("C") )/ seqlen, 3)

#check to see if the frequencies add up to 1 (so all characters are one of the nucleotides, not another letter)

if (freqA + freqC + freqG + freqT) == 1:
  # print the frequencies of each nucleotide for the sequence
  print("Freq of A:", round(freqA, 3))
  print("Freq of C:", round(freqC, 3))
  print("Freq of G:", round(freqG, 3))
  print("Freq of T:", round(freqT, 3))
  print("G+C content:", round(freqGC, 3))
else:
  print("Oh no! It appears this sequence is not composed of only A,G,T,C characters. Is the input only a nucleotide sequence (without a header")
