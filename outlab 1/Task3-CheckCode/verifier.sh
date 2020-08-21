if ! [ $# -eq 3 ]
then
	echo "Usage: ./verifier.sh <source file> <testcases url> <cut-dirs arg>"
	exit 1
fi

code=$1
url=$2
x=$3
wget -qr -np -nH --cut-dirs="${x}" -R "index.html*" $2
cp "$code" .
name=$(basename "$code")

dir=$(find . -type d -name "inputs")
parent="$(dirname "$dir")"
mkdir "$parent/my_outputs/"
out="$parent/my_outputs/"
touch feedback.txt
echo "Failed testcases are:" > ./feedback.txt
g++ "$name"
for file in ${dir}/*.in
do
	f=$(basename "$file" .in)
	./a.out < "$file" > "$out/${f}.out"
done

cnt=0
for file in $(ls $out)
do
	val=$(diff "$out/$file" "$parent/outputs/$file")
	if ! [ ${#val} -eq 0 ]
	then
		echo $(basename "$out/$file" .out) >> ./feedback.txt
		cnt=$(($cnt+1))
	fi
done

if [ $cnt -eq 0 ]
then 
	echo "All testcases passed!"
else
	echo "Some testcases failed."
fi