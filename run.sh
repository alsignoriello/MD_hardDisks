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
N=50
d=2
m=3
k=10
B=0.1
dt=0.01
Nt=20000

# make directory to save positions
mkdir positions

# make directory to plot disks
mkdir disks

# make directory to plot voronoi
mkdir voronoi 

# run MD simulation
python $HOME/run.py $N $d $m $k $B $dt $Nt

# plot energy
python $HOME/plot_energy.py $dt


