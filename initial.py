#!/usr/bin/python
from Particle import Particle
import numpy as np

"""

inital.py - initializes class particles with centers on a grid
with periodic bounary conditions
author: Lexi Signoriello
date: 4/5/16


"""


def initialize_particles(N, d, m, L):
	
	lx = int(L[0])
	ly = int(L[1])

	particles = []

	# initial acceleration is 0
	ax = 0
	ay = 0

	# initialize centers on grid
	count = 0
	for xi in range(int(d)/2, lx + int(d)/2, int(d)):
		for yi in range(int(d)/2, ly + int(d)/2, int(d)):

			# random initial velocities [-1,1]
			vx = np.random.normal(0,1) #/ 10.
			vy = np.random.normal(0,1) #/ 10.

			# store in class particle
			particle = Particle(count, xi, yi, d, m, vx, vy, ax, ay)
			particles.append(particle)

			count += 1

	return particles



