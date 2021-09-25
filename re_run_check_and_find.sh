#!usr/bin/bash
design=0
for n in $(seq $1 $2)
do
	echo "job ID $n"
	echo "design ID $design"
	sh check_cat_move_results.sh $n ~/vah_run_events/$3/$design
	sh find_events_did_not_run $n ~/vah_run_events/$3/$design
	((design++))
done
sh get_sucess_events_per_design_list.sh ~/vah_run_events/$3
