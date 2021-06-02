#!/bin/bash
#SBATCH -J Pb_Pb_2760_MAP_VAH
#SBATCH -p bdwall
#SBATCH -N 20
#SBATCH --ntasks-per-node 36
#SBATCH -t 04:00:00
#SBATCH --mail-user=liyanage.5@osu.edu
#SBATCH --mail-type=all
#SBATCH -A unedf_optimization
module reset
module load parallel
module load singularity

printf "Start time: "; /bin/date
printf "Job is running on node: "; /bin/hostname
printf "Job running as user: "; /usr/bin/id
printf "Job is running in directory: "; pwd

inputdir="/home/ac.liyanage/vah_run_events/$1/" #where the tables for iS3D, smash... are located. design_pts should be a folder inside!
echo "inputdir = "
echo $inputdir
###export TMPDIR="~/run_events/output_simulation"
#SCRATCH="output_simulation"
SCRATCH="/lcrc/globalscratch/dan"
echo "scratch = "
echo ${SCRATCH}
job=$SLURM_JOB_ID
echo "job : "
echo $job

mkdir $SCRATCH/$job
#n_cores=15

#let max_cores=$n_cores-1

#n_events_per_core=10
my_parallel="parallel --delay .8 -j $SLURM_NTASKS"
my_srun="srun --export=all --exclusive -n1 --cpus-per-task=1 --cpu-bind=cores"
$my_parallel "$my_srun singularity exec -B $SCRATCH:/scr ~/jetscape_vah sh event.sh $inputdir $job " ::: {1..5000}

echo "All events have finished. Goodbye!"


