#!/usr/bin/bash
export SCRATCH="/lcrc/globalscratch/dan"
rm $2/$1.interrupt.txt
rm $2/$1.failed.txt
rm $2/$1.success.txt
rm $2/$1.results.dat
rm $2/$1.log
rm $2/$1.crashed.txt
for f in  $SCRATCH/logs/$1/[0-9]*.log
do
	if grep -q "crash" $f;
    	then
		echo "event crashed : $f"
		echo "$f" >> $2/$1.crashed.txt
    	elif grep -q "failed" $f;
    	then
		echo "event failed : $f"
		echo "$f" >> $2/$1.failed.txt
	elif grep -q "event 0 completed successfully" $f;
	then
		echo "$f" >> $2/$1.success.txt
		folder=$(echo $f| cut -d '/' -f 7)
		event=$(echo $folder| cut -d '.' -f 1)
		echo "catting $event.dat"
    		rm -rf $SCRATCH/results/$1/results.dat
    		cat $SCRATCH/results/$1/$event.dat >> $2/$1.results.dat
	elif grep -q "interrupt" $f;
	then
		echo "Event was interrupted : $event"
		echo "$f" >> $2/$1.interrupt.txt
	fi
	cat $f >> $2/$1.log
done

echo "done catting and moving the results to $2 folder"
