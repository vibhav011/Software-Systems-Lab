#! /bin/bash

n=(100 90 50 40 10 9 5 4 1)
c=('C' 'XC' 'L' 'XL' 'X' 'IX' 'V' 'IV' 'I')

f(){
	z=$1
	for i in {0..8}
	do
		if [ $z -ge ${n[$i]} ]
		then
			echo -n "${c[$i]}"
			z=$((z-${n[$i]}))
			break
		fi
	done
	if [ $z -gt 0 ]
	then
		f $z
	fi
}
f $1
echo