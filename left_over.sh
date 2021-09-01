sh check_cat_move_results.sh $1 /home/ac.liyanage/vah_run_events/design/$2/
sh find_events_did_not_run $1 /home/ac.liyanage/vah_run_events/design/$2/
mv slurm-$1.out design/$2/
