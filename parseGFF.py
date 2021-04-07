#! /usr/bin/env python3

import csv
import argparse #used to make arguments in terminal much nicer
from Bio import SeqIO

# inputs: 1) GFF file (.gff), corresponding genome sequence (FASTA format)
# output:

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature from the genome')

# add positional arguments (called so b/c their order matters)
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta,'fasta')
# print(genome)
# print(len(genome.seq))
# print(genome.id)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
  # create a csv reader object
  reader = csv.reader(gff_in, delimiter = '\t')
  # loop over all lines in reader object (i.e., the parsed file)
  for line in reader:
    start = line[3] # which column corresponds to start location of gene in genome
    end = line[4] # which column corresponds to end location of gene in genome
    strand = line[6] # which strand is the gene on
    print(line[3], line[4], line[6])
    # extract the sequence
    



# parse the GFF file

