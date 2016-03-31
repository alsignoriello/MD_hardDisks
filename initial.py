#!/usr/bin/python
from Particle import Particle
import numpy as np



def initialize_particles(N, d, m, L):
	
	lx = int(L[0])
	ly = int(L[1])

	particles = []

	# initial acceleration is 0
	ax = 0
	ay = 0

	# initialize centers on grid
	count = 0
	for xi in range(0, lx + d, d):
		for yi in range(0, ly + d, d):
			# random initial velocities [-1,1]
			vx = np.random.normal(0,1) / 10.
			vy = np.random.normal(0,1) / 10.
			particle = Particle(count, xi, yi, d, m, vx, vy, ax, ay)
			count += 1
			particles.append(particle)
	return particles



