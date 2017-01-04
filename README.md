# 2D Molecular Dynamics Hard Disks

Simulates 2D molecular dynamics simulation with hard sphere potential.


# Definitions

Hooke's Law for spring potential


Velocity Verlet Integration



# Running the Simulation

sh run.sh folder
sh plot.sh folder


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