#!/usr/bin/python
import numpy as np
from initial import initialize_particles
from MD import molecular_dynamics
from parser import write_parameters
import sys


""" 

run.py - Runs molecular dynamics simulation for disks
author: Lexi Signoriello
date: 4/5/16


"""

# dictionary for equation paramters
parameters = {}

# Experiment Parameters
# number of particles
N = int(sys.argv[1])
parameters['N'] = N

# diameter of particles
d = float(sys.argv[2])
parameters['d'] = d

# mass of particles
m = float(sys.argv[3])
parameters['m'] = m

# Equation Parameters
# spring constant for harmonic force law
k = float(sys.argv[4])
parameters['k'] = k

# drag coefficient
B = float(sys.argv[5])
parameters['B'] = B

# size of box
lx = 10. * d 
ly = 10. * d
L = np.array([lx,ly])
parameters['Lx'] = lx
parameters['Ly'] = ly

# Simulation Parameters
# time step
dt = float(sys.argv[6])
parameters['dt'] = dt

# number of time steps
Nt = int(sys.argv[7])
parameters['Nt'] = Nt

# write parameters
write_parameters(parameters)

# initialize all particles on grid
particles = initialize_particles(N, d, m, L)

# Run Molecular Dynamics Simulations
molecular_dynamics(particles, dt, Nt, parameters)
