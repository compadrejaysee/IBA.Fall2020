#!/bin/bash
readfile=$1
counter=1
#first couln represents nmber of occurence
for TOKEN in $@
do
	if [ $counter -gt 1 ]; then
		x=$(grep $TOKEN $readfile| wc )
		echo "$TOKEN  --->  $x"
	fi
	let counter+=1
done


