#!/usr/bin/bash

HOME=/Users/Lexi/Documents/Ohern_2016/MD_hardDisks

folder=$1
if [ -d "$folder" ]; then
	rm -r $folder
fi
mkdir $folder
cd $folder
echo $folder

# parameters
N=100
d=2
m=3
k=1
B=0
dt=0.01
Nt=2000

# make directory to save positions
mkdir positions
python $HOME/run.py $N $d $m $k $B $dt $Nt

