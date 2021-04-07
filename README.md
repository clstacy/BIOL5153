# BIOL5153

## Practical Programming for Biologists at the University of Arkansas
### Spring 2020

This is a repository that I use for this course. My assignments are submitted here. 


## File Descriptions:

### Python Scripts
  
  - `write_razor_pbs.py` : This python script generates an output which can be saved as a bash (.sh) script for submitting jobs to the Razor cluster on the Uark AHPCC using PBS scheduling syntax.
  - `write_pinnacle_slurm.py` : This python script generates an output which can be saved as a bash (.sh) script for submitting jobs to the Pinnacle cluster on the Uark AHPCC using SLURM scheduling syntax.
  - `nucleotide_composition.py` : This python script calculates the frequency of nucleotides of a string of characters of a nucleotide sequence (requires removal of header prior to entering into script, as written). Created in completion of Assignment 5 of this course, not written to be practical for everyday use as is.
  - `parseGFF.py` : This python script runs from command line, takes two inputs (1) a .gff file with genomic features and (2) a .fasta file of the corresponding genome. This script extracts the sequence of each feature of the gff file and returns them as individual fasta formatted sequences to STDOUT. Features that are coded to be on the "-" strand in the input gff file will return their reverse complement to STDOUT in this script.
  
### Miscellaneous

  - `CV.md` : This file is my curriculum vitae written in markdown format.
  - `assn03.tgz` : The assn03.tgz file is a zipped tape archive containing the bash scripts that I used to create BLAST databases and complete BLAST searches, as well as their outputs and answers to all questions in completion of assignment 3 questions in this course.
  - `Supplemental_files` : A folder that contains README images, and other "clutter" in this repo.



### Demonstration of PBS script output

Here is an example output of python script that generates PBS bash scripts for submission on the razor cluster:

![Output of python script that generates PBS bash scripts for submission on the razor cluster](https://raw.githubusercontent.com/clstacy/BIOL5153/main/Supplemental_Files/stacy_assn04_BIOL5143_PBS_screenshot.png.png)]

