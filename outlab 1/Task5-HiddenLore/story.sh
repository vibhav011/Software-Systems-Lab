#! /bin/bash

dir=$1
next=$2
out=$3

files=($( grep -Hl "^$next$" $dir/* ))
echo $(cat ${files[0]} | head -1) > $out
next=$(cat ${files[0]} | tail -1)
cur=${files[0]}

files=($( grep -Hl "^$next$" $dir/* ))

while [ ${#files[@]} -eq 2 ]
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
	files=($( grep -Hl "^$next$" $dir/* ))
done

