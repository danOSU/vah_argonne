#!/bin/bash
#echo "$1" >> history.txt
#result=$(sbatch submit_argonne_vah $2)
#result=$(sbatch submit_design $2)
#result=$(salloc salloc_submit $2)
#result="jobID"
#echo "$result" >> history.txt
#cat history.txtI
for num in {451..499}
do
	sh submit.sh "submiting initial design $num" "design/$num"
	echo "$num has been submitted"
done
