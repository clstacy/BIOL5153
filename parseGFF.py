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

# create a function that reverse complements sequences of gff file that are on the - strand:
def rev_comp(gene_seq, strand):
  # determine whether to reverse complement
  #if strand == "-": # if -, need to reverse and complement the strand
  if strand == "-":
    # print the reverse complement of nucleotides in the sequence 
    return(print(gene_seq.reverse_complement()))
  else:
    # print the sequence of the gene
    return(print(gene_seq))

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
  # create a csv reader object
  reader = csv.reader(gff_in, delimiter = '\t')
  # loop over all lines in reader object (i.e., the parsed file)
  for line in reader:
    # identify important components from gff, assign variables.
    start = int(line[3]) # which column corresponds to start location of gene in genome
    end = int(line[4]) # which column corresponds to end location of gene in genome
    strand = line[6] # which strand is the gene on
    header_info = line[-1] #last column of gff is information about the entry
    
    # print header line for each fasta sequence:
    print(">" + genome.id, header_info)#, ";", "STRAND", strand)

    # call rev_comp function to print starnds including rev comp if on - strand
    rev_comp(genome.seq[start-1:end], strand)
#note that the -1 is due to 0 indexing of python vs 1 indexing of gff format. not on 'end' b/c of normal py indexing rules excludes last value

    # add empty space between each entry
    print()