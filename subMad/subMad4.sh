#!/bin/bash

#SBATCH -p lipq

module load gcc63/root/6.18.04
module load gcc63/madgraph/2.7.3
module load gcc63/pythia/8.2.40
module load python-2.7.11

# INPUT=proc_v4

mg5_aMC proc_v4

exit 0
