#!/usr/bin/python
from velocity_verlet import *
import numpy as np
from plot import plot_disks

def molecular_dynamics(particles, dt, Nt, parameters):

	# store kinetic energy for every time step
	E_k = np.zeros(Nt)

	# store potential energy for every time step
	E_p = np.zeros(Nt)

	# spring potential
	k = parameters['k']

	# length of box
	L = parameters['L']

	# drag coefficient
	B = parameters['B']

 
	for t in range(0,Nt):

		# Integrate Newton's Equations of Motion
		# using velocity verlet algorithm

		# (x,y) += dt * v(t) + 1/2 * a(t) * dt^2
		get_positions(particles, dt, L)

		# calculate forces for particle-particle interactions
		ep, accels = get_forces(particles, k, L, B)
		E_p[t] = ep
		print ep


		# diffuse single particle
		accels = move_single_particle(particles, accels)

		# calculate new velocities
		# v(t+1) = v(t) + 1/2(a(t) + a(t+1)) * dt
		ek = get_velocities(particles, accels, dt)
		E_k[t] = ek
		print ek

		# write coordinates to file

		# plot disks
		if t % 5 == 0:
			plot_disks(particles, L, str(t))

		# plot voronoi



		