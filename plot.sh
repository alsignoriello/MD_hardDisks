#!/usr/bin/bash

HOME=/Users/Lexi/Documents/Ohern_2016/MD_hardDisks

folder=$1
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

# plot energy
python $HOME/plot_energy.py $dt


# plot voronoi
mkdir voronoi
python $HOME/plot_voronoi.py 

# plot disks
mkdir disks
python $HOME/plot_disks.py

