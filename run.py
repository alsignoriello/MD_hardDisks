#!/usr/bin/python
import numpy as np
from initial import initialize_particles
from MD import molecular_dynamics


# Experiment Parameters
# number of particles
N = 100

# diameter of particles
d = 2

# mass of particles
m = 3

# Equation Parameters
# dictionary for equation paramters
parameters = {}
# spring constant for harmonic force law
k = 1.
parameters['k'] = k

# drag coefficient
B = 0.1
parameters['B'] = B

# force on mobile particle
fd = 10.
parameters['fd'] = fd

# size of box
lx = 10. * d 
ly = 10. * d
L = np.array([lx,ly])
parameters['L'] = L

# Simulation Parameters
# time step
dt = 0.01

# number of time steps
Nt = 50000;

# initialize all particles on grid
particles = initialize_particles(N, d, m, L)

# Run Molecular Dynamics Simulations
molecular_dynamics(particles, dt, Nt, parameters)
