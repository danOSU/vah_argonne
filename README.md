# Run VAH model Relativistic Heavy Ion Collisions in Argonne

We will run the simulations in Argonne Bebop cluster using singularity containers.

## Singularity Containers
Follow these steps to get the singularity image

1. Load the singularity module in Bebop cluster
>module load singularity
2. Get the container image and make a sandbox folder with write privileges in the home directory
>cd ~/ \
>singularity build --sandbox jetscape docker://dananjaya92/jetscape-bulk:v3 


Now you have a folder named _jetscape_ which has the container files. Changes you make to this folder will apear in any spawned jetscape containers.
For more information on building containers with a sanbox please refer to *[singularity documentaion](https://sylabs.io/guides/3.0/user-guide/build_a_container.html)*

## Run Simulations

1. Clone this repo as _sims_run_events_ folder
>git clone https://github.com/danOSU/vah_argonne.git -b sims vah_run_events

2. The folowing will submit five relativistic heavy ion collision simulations to a single node only using 5 CPUs. All the simulations input
parameters are set to Maximum a Posteriori(MAP) values found in this *[paper](https://arxiv.org/abs/2011.01430)*
> sh submit.sh  "My first simulation run"  MAP

With each submission a _history.txt_ file is updated with the Job_ID and with the comment made at the submision. 
To run the simulation with a different set of input parameters you need to generate and put the relevent input files inside a new folder in _MAP_. 
Please take a look at the _MAP_ input files and the python script that generate these input files by going to _MAP_ to understand what input files are needed 
to run an event.
If you put new set of input files in a directory _new_design_0_ events with this input files can be run by following command.
>sh submit.sh "New set of model parameter values" new_design_0

To change the resources used and to increase the number of events run for a single design point look at _submit_argonne_vah_ file.

## Simulation Results

The raw simulation results can be found in SCRATCH/results/JOB_ID folder. Results forlder contain the final particle lists as .dat files for each event. These results need to be combined for a proper analysis. This is done by _check_cat_move_results.sh_. The file with all the particles from all the
simulated events can be found in _MAP_ after you run >sh check_cat_move_results.sh JOB_ID MAP. Similarly in SCRATCH/logs/JOB_ID you can find the logs for each event.

>sh check_cat_move_results.sh JOB_ID MAP
Results  from each individual run is concatenated and being put in the same folder that had the input files for
the simulation runs. For the example run it would be in _MAP_. In the same folder there is _JOB_ID.log_ file which has the printed standard output of the job and 
several _.txt_ files with more information about the succesful completion/ failure of each individual event. 
