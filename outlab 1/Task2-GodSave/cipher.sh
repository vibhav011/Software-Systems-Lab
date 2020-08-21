#! /bin/bash

if [ $# != 1 ]
then
	echo "Usage: ./cipher.sh <url>"
	exit 1
fi

wget -q $1 -O ./encrypted.txt

file="encrypted.txt"

m=abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
n=ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ

rot=0
words=('Queen' 'Majesty')

for i in {0..25}
do
	for word in $words
	do
		if grep -qi "$word" <<< $(cat "$file" | tail -1 | tr "$m" "${m:$i}${m:0:$i}" | tr "$n" "${n:$i}${n:0:$i}");
		then
			rot=$i
			break
		fi
	done
done

dest=./deciphered.txt
var=$(cat encrypted.txt | tr "$m" "${m:$rot}${m:0:$rot}" | tr "$n" "${n:$rot}${n:0:$rot}")
printf "%s" "$var" > "$dest"

echo "PS. Give me the names." | tr "${m:$rot}${m:0:$rot}" "$m" | tr "${n:$rot}${n:0:$rot}" "$n" >> encrypted.txt

