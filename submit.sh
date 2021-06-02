#!/bin/bash
echo "$1" >> history.txt
result=$(sbatch submit_argonne_vah $2)
#result="jobID"
echo "$result" >> history.txt
cat history.txt
