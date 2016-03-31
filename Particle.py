#!/usr/bin/python

""" 

Particle.py - Class particle to keep track of particles in simulation


author: Lexi Signoriello 
date: 3/31/16

id - unique integer 
x - geometric center
y - geometric center
d - diamter of particle
m - mass 
vx - velocity wrt x
vy - velocity wrt y
ax - acceleration wrt x
ay - acceleration wrt y

* assure all are floats - necessary for computing equations

"""


class Particle:

	def __init__(self, id, x, y, d, m, vx, vy, ax, ay):
		self.id = id
		self.x = float(x)
		self.y = float(y)
		self.d = float(d)
		self.m = float(m)
		self.vx = float(vx)
		self.vy = float(vy)
		self.ax = float(ax)
		self.ay = float(ay)




