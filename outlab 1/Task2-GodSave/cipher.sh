if [ $# != 1 ]
then
	echo "Usage: ./cipher.sh <url>"
	exit 1
fi

wget -q $1 -O ./encrypted.txt

file="encrypted.txt"
s=zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba
l=ZYXWVUTSRQPONMLKJIHGFEDCBAZYXWVUTSRQPONMLKJIHGFEDCBA
m=abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz
n=ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ

rot=0
for i in {0..26}
do
	if grep -qi "Queen" <<< $(cat "$file" | tail -2 | tr "${s:0:26}" "${s:${i}:26}" | tr "${l:0:26}" "${l:${i}:26}");
	then
		rot=$i
		break
	fi
	if grep -qi "Majesty" <<< $(cat "$file" | tail -2 | tr "${s:0:26}" "${s:${i}:26}" | tr "${l:0:26}" "${l:${i}:26}");
	then
		rot=$i
		break
	fi
done

dest=./deciphered.txt
var=$(cat encrypted.txt | tr "${s:0:26}" "${s:17:26}" | tr "${l:0:26}" "${l:17:26}")
printf "%s" "$var" > "$dest"

echo "PS. Give me the names." | tr "${m:0:26}" "${m:${rot}:26}" | tr "${n:0:26}" "${n:${rot}:26}" >> encrypted.txt