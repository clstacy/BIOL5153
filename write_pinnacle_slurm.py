#! /share/apps/python/anaconda3-3.6.0/bin/python3


# This script generates a SLURM file for the pinnacle cluster


# define some variables
job_name = "CreativeJobName" # name of job
queue = "comp01" #queue on which to run script
prefix_out = job_name + ".$SLURM_JOBID" # prefix for output file
n_nodes = 1 # number of nodes requested
n_process = 1 # number of processors requested
wall = 1 # wall time requested (in hours)

# This section prints the header/required info for the PBS script
print("#!/bin/bash")
print()
print("#SBATCH -J", job_name) # job name
print("#SBATCH --partition", queue) # which queue to use
 # in slurm, this -o flag joins the STDOUT and STDERR into a single file (use -e to get error)
print("#SBATCH -o", prefix_out) # set the name of the job output file
print("#SBATCH --nodes=" + str(n_nodes)) # number of nodes/cpus to use
print("#SBATCH --ntasks-per-node=" + str(n_process)) #number of tasks per node
print("#SBATCH --time=" + str(wall) + ":00:00") # set the walltime (default to 1 hr)
print()
print("export OMP_NUM_THREADS=1")
print()
# change directory into working directory on cluster
print("cd $SLURM_SUBMIT_DIR")
print()
# load necessary modules
print("# load modules")
print("module purge")
print("module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0 blast mafft/7.304b")
print()  
# commands for this job
print("# INSERT COMMANDS BELOW")
print()
print("# copy files from storage to scratch")
print('rsync -av *.fasta /scratch/$SLURM_JOB_ID')
print()
print('# cd onto the scratch disk to run the job')
print('cd /scratch/$SLURM_JOB_ID/')
print()
print('#run the thing')
print('# /share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 1 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output examplename')
print()
print('#copy output files back to storage')
print('rsync -av examplename $SLURM_SUBMIT_DIR')
print()

