#! /share/apps/python/anaconda3-3.6.0/bin/python3

# This script generates a PBS file for the razor cluster


# define some variables
job_name = "CreativeJobName" # name of job
queue = "med16core" #queue on which to run script
prefix_out = job_name + ".$PBS_JOBID" # prefix for output file
n_nodes = 1 # number of nodes requested
n_process = 1 # number of processors requested
wall = 1 # wall time requested (in hours)

# This section prints the header/required info for the PBS script
print("#PBS -N", job_name) # job name
print("#PBS -q", queue) # which queue to use
print("#PBS -j oe") # join the STDOUT and STDERR into a single file
print("#PBS -o", prefix_out) # set the name of the job output file
print("#PBS -l nodes=" + str(n_nodes) + ":ppn=" + str(n_process)) # how many resource to askf or (nodes = num nodes, ppn = num processors)
print("#PBS -l walltime=" + str(wall) + ":00:00") # set the walltime (default to 1 hr)
print()
# change directory into working directory on cluster
print("cd $PBS_O_WORKDIR")
print()
# load necessary modules
print("# load modules")
print("module purge")
print("module load gcc/7.2.1 python/3.6.0-anaconda java/sunjdk_1.8.0 blast mafft/7.304b")
print()  
# commands for this job
print("# insert commands here")
print("Hello, world!")
print()
print("# make a pretty tower of numbers")
print('for row_num in range(1, 10):')
print('    print(' '.join(' ' if index_num > row_num else str(index_num) for index_num in range(10, 1, -1)), ' \
    '.join(' ' if index_num > row_num else str(index_num) for index_num in range(1, 10))) ')
print()
print("# that gives an output like this:")
print("# NOTE: output should not be part of a bash script, code should be executed on node, not here.")
print("# This is just to look pretty in the example.)")
for row_num in range(1, 10):     print(' '.join(' ' if index_num > row_num else str(index_num) for index_num in range(10, 1, -1)), ' '.join(' ' if index_num > row_num else str(index_num) for index_num in range(1, 10))) 




