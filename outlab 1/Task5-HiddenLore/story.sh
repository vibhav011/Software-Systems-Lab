#! /bin/bash

dir=$1
next=$2
out=$3

files=($( grep -n "^$next$" $dir/* | grep ':2:' | cut -d: -f1 ))

if [ ${#files[@]} -eq 0 ]
then
	echo '' > $out
else
	echo $(cat ${files[0]} | head -1) > $out
	next=$(cat ${files[0]} | tail -1)
	cur=${files[0]}
	files=($( grep -n "^$next$" $dir/* | grep ':2:' | cut -d: -f1 ))
fi

while [ ${#files[@]} -eq 1 ]
do
	for i in 0 1
	do
		file=${files[$i]}
		if [[ $file != $cur ]]
		then
			echo $(cat $file | head -1) >> $out
			next=$(cat $file | tail -1)
			cur=$file
			break
		fi
	done
	files=($( grep -n "^$next$" $dir/* | grep ':2:' | cut -d: -f1 ))
done

