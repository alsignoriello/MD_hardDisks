# 2D Molecular Dynamics Hard Disks

Simulates 2D molecular dynamics simulation with hard sphere potential.


# Definitions

## Hooke's Law for spring potential

F = -kx


## Velocity Verlet Integration

Steps are described here: 
https://en.wikipedia.org/wiki/Verlet_integration

Step 1: Get positions from current velocity and acceleration

Step 2: Derive accelerations from interaction potentials

Step 3: Calculate new velocities from accelerations


# Running the Simulation

sh run.sh [folder]


# Parameters

| Parameter | Definition | Type |
|-----------|------------|------|
| folder	| folder to write data | str |
| N 		| number of particles | int |
| d 		| diameter of particles | float |
| m 		| mass of particle 		| float |
| k 		| spring potential | float 	|
| B 		| drag force 		| float |
| L 		| length of Box 	| float | 
| dt 		| time step 		| float |
| Nt 		| number of time steps | int |



# Assumptions

-periodic boundary conditions

-Max N is 100 (or adapt initalization)