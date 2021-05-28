#!/usr/bin/bash
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
    		cat $SCRATCH/results/$1/$event.dat >> results.dat
	else
		echo "something went teribely wrong : $event"
		echo "$f" >> $2/$1.unknown.txt
	fi
	cat $f >> log
done

mv results.dat $2/$1.results.dat
mv log $2/$1.log
echo "done catting and moving the results to $2 folder"
