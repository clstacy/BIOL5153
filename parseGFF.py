#! /usr/bin/env python3

import csv
import argparse #used to make arguments in terminal much nicer
from Bio import SeqIO
from collections import defaultdict  # don't need value in before creating key. Avoids key errors
import re # regex

# inputs: 1) GFF file (.gff), corresponding genome sequence (FASTA format)
# output: the CDS for each transcriptional gene present

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract whole exon sequences from the genome fasta file')

# add positional arguments (called so b/c their order matters)
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')
parser.add_argument("feature_type_arg", help='feature type that contains exons')

# parse the arguments
args = parser.parse_args()

# read in FASTA file
genome = SeqIO.read(args.fasta.rstrip(),'fasta')

# create a function that reverse complements sequences of gff file that are on the - strand:
def rev_comp(gene_seq, strand):
  # determine whether to reverse complement
  if strand == "-": # if -, need to reverse and complement the strand
    # print the reverse complement of nucleotides in the sequence 
    return(gene_seq.reverse_complement())
  else:
    # print the sequence of the gene
    return(gene_seq)

## Extracting the [CDS] or feature_type_arg regions:

# declare dictionary: key = gene, value = list of exon(s) for that gene
gene_dict = defaultdict(dict)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:
  # create a csv reader object
  reader = csv.reader(gff_in, delimiter = '\t')

  # loop over all lines in reader object (i.e., the parsed file)
  for line in reader:
    # skip header line
    if re.search('^#', line[0]):
      continue
    
    else:
      # identify important components from gff, assign variables.
      start = int(line[3]) # which column corresponds to start location of gene in genome
      end = int(line[4]) # which column corresponds to end location of gene in genome
      strand = line[6] # which strand is the gene on
      header_info = line[-1] #last column of gff is information about the entry
      feature_type = line[2].strip() #type of feature, used to get CDS sequences
      species = line[0] # species from which genes are taken
      exon_number = re.search("exon ?=?(\d)", header_info, re.I) # find the exon number

      # create a variable that later serves as fasta header: (gene_key)
        # only works if gene name is second object in description file, not generalizable
      gene_key = ">" + species.replace(" ", "_") + "_" + header_info.split()[1] 
      

      # select gff objects that are `feature_type_arg` (e.g. CDS) features
      if feature_type == args.feature_type_arg:
        
        # add features with only one exon to the dictionary
        if not exon_number:
          
          # Assign the value (sequence, reverse complemented if needed) to dictionary
          gene_dict[gene_key] = rev_comp(genome.seq[start-1:end], strand)

        # for genes that are >1 exon but not in dictionary yet:
        elif not gene_dict[gene_key]:
          
          #create an entry in dict for new gene that is all null values
            #NOTE:  created 250 because no known CDS has more than 234 exons. would be better to find max of number in gff file, but I am unsure how to properly implement.
          gene_dict[gene_key] = ['']*250 
          
          # Assign the sequence of exon number to the appropriate index in the list for that dictionary key
          gene_dict[gene_key][int(exon_number[1])-1] = rev_comp(genome.seq[start-1:end], strand)
        
        # for genes with >1 exon that are already have a gene_dict entry
        else:
          # add sequence entry to correct place in list
          gene_dict[gene_key][int(exon_number[1])-1] = rev_comp(genome.seq[start-1:end], strand)
        
# convert the sequences from lists to a string with .join()
for key in gene_dict:
  gene_dict[key] = ''.join(str(exon) for exon in gene_dict[key])

# print output
for key, value in gene_dict.items():
  # print the key (which is gene_key, already in fasta format above)
  print(key)
  # print the sequence
  print(value)#''.join(str(exon) for exon in j).strip())
  # add spacing for easier formatting.
  print()
