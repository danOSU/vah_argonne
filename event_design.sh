echo "input directory "
echo $1
echo "job number"
echo $2
echo "event number"
echo $3
python3 /home/jetscape-user/JETSCAPE-COMP/sims_scripts/submit/run-events-ALICE-VAH.py --nevent 1 --logfile /scr/logs/$2/$3.log --tmpdir=$TMPDIR --tablesdir=$1 /scr/results/$2/$3.dat
