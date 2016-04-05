#!/usr/bin/python
import numpy as np
from math import cos, sin

""""


velocity_verlet.py - velocity verlet is an algorithm 
used to integrate Newton's equations of motion

author: Lexi Signoriello
date: 3/31/16

Steps are described here: 
https://en.wikipedia.org/wiki/Verlet_integration
Step 1: Get positions from current velocity and acceleration
Step 2: Derive accelerations from interaction potentials
Step 3: Calculate new velocities from accelerations

"""

# Difference with respect to periodic boundaries
def periodic_diff(x1, x2, L):
	return ((x1 - x2 + L/2.) % L) - L/2.

# (x,y) = dt * velocity + 1/2 * acceleration * dt^2
def get_positions(particles, dt, L):

	for particle in particles:

		particle.x = particle.x + (particle.vx * dt) + 0.5 * (particle.ax * dt**2)
		particle.y = particle.y + (particle.vy * dt) + 0.5 * (particle.ay * dt**2)

		# check periodic boundary conditions
		if particle.x < 0:
			particle.x = particle.x + L[0]

		if particle.x > L[0]:
			particle.x = particle.x - L[0]

		if particle.y < 0:
			particle.y = particle.y + L[1]

		if particle.y > L[1]:
			particle.y = particle.y - L[1]

	return particles


def get_forces(particles, k, L, B):

	lx = L[0]
	ly = L[1]
	N = len(particles)
	forces = np.zeros((N,2))

	# potential energy
	ep = 0.

	# calculate particle - particle interaction forces
	for i in range(N):
		particle = particles[i]

		for j in range(i+1, N):
			particle2 = particles[j]

			x1 = particle.x 
			y1 = particle.y
			x2 = particle2.x
			y2 = particle2.y

			dx = periodic_diff(x1, x2, lx)
			dy = periodic_diff(y1, y2, ly)

			# distance between particle i and particle j
			d_ij = dx**2 + dy**2 

			# two particles interact if they are close enough
			D = 0.5 * (particle.d + particle2.d)
			if d_ij < D**2:

				# euclidean distance is square root
				d_ij = d_ij**0.5

				# Hooke's law for spring potential
				F = -k * (D/d_ij - 1) 
				forces[i,0] -= F * dx
				forces[i,1] -= F * dy
				forces[j,0] += F * dx
				forces[j,1] += F * dy

				# particle-particle potential energy
				# due to overlap
				ep = ep + (D - d_ij)**2



	# new accelerations due to forces
	a = np.zeros((N, 2))
	for i,particle in enumerate(particles):
		m = particle.m
		a[i,0] = (forces[i,0] / m) - B * particle.vx
		a[i,1] = (forces[i,1] / m) - B * particle.vy

	ep = k * 0.5 * ep

	return ep, forces, a



def move_single_particle(particles, a):
	# # move single particle
	p_i = 1 # particle index
	theta = 2. * np.pi * np.random.uniform(0,1)
	a[p_i,0] += cos(theta) / particles[p_i].m
	a[p_i,1] += sin(theta) / particles[p_i].m
	return a
	


def get_velocities(particles, accels, dt):

	# kinetic energy
	ek = 0.

	# update velocities from accelerations
	for i,particle in enumerate(particles):

		ax_old = particle.ax
		ay_old = particle.ay
		ax_new = accels[i,0]
		ay_new = accels[i,1]
		particle.vx = particle.vx + 0.5 * dt * (ax_old + ax_new)
		particle.vy = particle.vy + 0.5 * dt * (ay_old + ay_new)

		ek += 0.5 * particle.m * (particle.vx**2 + particle.vy**2)

		# new acceleration
		particle.ax = ax_new
		particle.ay = ay_new

	return ek