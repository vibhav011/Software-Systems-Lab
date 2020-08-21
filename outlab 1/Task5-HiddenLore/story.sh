#! /bin/bash

# Try to make the code faster, it takes around 7s
f(){
	for file in $(ls $1)
	do
		if [ $(cat $1/${file} | head -2 | tail -1) -eq $2 ]
		then
			if [ $4 -eq 1 ]
			then
				echo $(cat $1/${file} | head -1) > $3
			else
				echo $(cat $1/${file} | head -1) >> $3
			fi
			next=$(cat $1/${file} | tail -1)
			cnt=$(($4+1))
			f $1 $next $3 $cnt
			break
		fi
	done
}

dir=$1
next=$2
out=$3
cnt=1

f $dir $next $out $cnt