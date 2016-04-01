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
def step1(particles, dt, L):
	for particle in particles:
		particle.x += (particle.vx * dt) + (particle.ax * dt**2 / 2)
		particle.y += (particle.vy * dt) + (particle.ay * dt**2 / 2)

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


def step2(particles, k, L, B):

	lx = L[0]
	ly = L[1]

	# forces due to inter-particle interactions
	N = len(particles)
	forces = np.zeros((N,2))

	# potential energy
	ep = 0.

	# calculate particle - particle interaction forces
	for i,particle in enumerate(particles):
		for j,particle2 in enumerate(particles[i+1:]):
			x1 = particle.x 
			y1 = particle.y
			x2 = particle2.x
			y2 = particle2.y

			dx = periodic_diff(x1, x2, lx)
			dy = periodic_diff(y1, y2, ly)
			dist = dx**2 + dy**2

			D = max(particle.d, particle2.d)
			if dist < D:
				F = -k * (D/dist - 1) # not sure why -1 
				ep += (D - dist)**2
				forces[i,0] += F * dx
				forces[i,1] += F * dy
				forces[j,0] -= F * dx
				forces[j,1] -= F * dy

	# new accelerations due to forces
	a = np.zeros((N, 2))
	for i, particle in enumerate(particles):
		m = particle.m
		a[i,0] = (forces[i,0] / m) - B * particle.vx
		a[i,1] = (forces[i,1] / m) - B * particle.vy

	# move single particle
	p_i = 1 # particle index
	theta = 2. * np.pi * np.random.uniform(0,1)
	a[p_i,0] += cos(theta) / particles[p_i].m
	a[p_i,1] += sin(theta) / particles[p_i].m

	
	return ((k/2.) * ep), a
	


def step3(particles, accels, dt):

	# kinetic energy
	ek = 0.

	# update velocities from accelerations
	for i,particle in enumerate(particles):
		ax_old = particle.ax
		ay_old = particle.ay
		ax_new = accels[i,0]
		ay_new = accels[i,1]
		particle.vx += (ax_old + ax_new) * (dt/2.)
		particle.vy += (ay_old + ay_new) * (dt/2.)

		ek += particle.m * (particle.vx**2 + particle.vy**2) / 2.

		# new acceleration = old acceleration
		particle.ax = ax_new
		particle.ay = ay_new

	return ek