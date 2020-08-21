#! /bin/bash

dir=$(pwd)
songs="$dir/songs"
mkdir "$dir/albums"
mkdir "$dir/playlists"
albums="$dir/albums"
playlists="$dir/playlists"

for file in $(ls "$songs")
do
	album=$(cat "$songs/$file" | head -1)
	if ! [ -d "$albums/$album" ]
	then
		mkdir "$albums/$album"
	fi
	ln -s "$songs/$file" "$albums/$album/$file"
	n=$(cat "$songs/$file" | head -2 | tail -1)
	curr=3
	while [[ $curr -le $((2+$n)) ]]
	do
		playlist=$(cat "$songs/$file" | head -$curr | tail -1)
		if ! [ -d "$playlists/$playlist" ]
		then
			mkdir "$playlists/$playlist"
		fi
		ln -s "$songs/$file" "$playlists/$playlist/$file"
		curr=$(($curr+1))
	done
done