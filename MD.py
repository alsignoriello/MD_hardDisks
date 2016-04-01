#!/usr/bin/python
from velocity_verlet import *
import numpy as np
from plot import plot_disks

def molecular_dynamics(particles, dt, Nt, parameters):

	# kinetic energy for every time step
	E_k = np.zeros(Nt)

	# potential energy for every time step
	E_p = np.zeros(Nt)

	k = parameters['k']
	L = parameters['L']
	B = parameters['B']

 
	for t in range(0,Nt):

		# Integrate Newton's Equations of Motion
		# using velocity verlet algorithm

		# (x,y) = dt * velocity + 1/2 * acceleration * dt^2
		step1(particles, dt, L)

		# derive acceleration from particle-particle interactions
		ep, accels = step2(particles, k, L, B)
		E_p[t] = ep

		# calculate new velocities
		# v(t+1) = v(t) + 1/2(a(t) + a(t+1)) * dt
		ek = step3(particles, accels, dt)
		E_k[t] = ek

		# write coordinates to file

		# plot disks
		plot_disks(particles, L)

		# plot voronoi


		