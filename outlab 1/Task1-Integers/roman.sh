# Reduce number of chars for bonus
a(){
	if [ $1 = 0 ]
	then 
		echo
	elif [ $1 -ge 100 ]
	then 
		echo C$(a $(($1-100)))
	elif [ $1 -ge 90 ]
	then 
		echo XC$(a $(($1-90)))
	elif [ $1 -ge 50 ]
	then
		echo L$(a $(($1-50)))
	elif [ $1 -ge 40 ]
	then
		echo XL$(a $(($1-40)))
	elif [ $1 -ge 10 ]
	then
		echo X$(a $(($1-10)))
	elif [ $1 = 9 ]
	then
		echo IX$(a $(($1-9)))
	elif [ $1 -ge 5 ]
	then
		echo V$(a $(($1-5)))
	elif [ $1 = 4 ]
	then
		echo IV$(a $(($1-4)))
	else
		echo I$(a $(($1-1)))
	fi
}
a $1