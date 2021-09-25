#!/usr/bin/bash
echo "Looking in the folder : $1"
for dir in {0..50}
do
	echo "$dir" >> success_list.txt
	wc -l $1/$dir/*.success.txt >> sucess_list.txt
done
mv sucess_list.txt $1
