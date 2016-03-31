#!/usr/bin/python
from velocity_verlet import *
import numpy as np
from plot import plot_disks

def molecular_dynamics(particles, dt, Nt, parameters):

	# kinetic energy for every time step
	E_k = np.zeros(Nt)

	# potential energy for every time step
	E_p = np.zeros(Nt)


	for t in range(0,Nt):

		# Integrate Newton's Equations of Motion
		# using velocity verlet algorithm

		step1(particles, dt)

		k = parameters['k']
		L = parameters['L']
		B = parameters['B']
		ep, accels = step2(particles, k, L, B)
		E_p[t] = ep

		# step3(particles)
		ek = step3(particles, accels, dt)
		E_k[t] = ek


		# write coordinates to file

		# plot disks
		plot_disks(particles)

		# plot voronoi


		