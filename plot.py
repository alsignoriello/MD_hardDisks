#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle
from scipy.spatial import Voronoi
from math import sqrt
  

# def unit_vector(v1, v2):
# 	vector = v1 - v2
# 	dist = euclidean_distance(v1[0], v1[1], v2[0],v2[1])
# 	uv = vector / dist
# 	return uv

# # Euclidean distance between (x,y) coordinates
# def euclidean_distance(x1, y1, x2, y2):
# 	return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# def plot_force(x,y,fx,fy):

# 	f = np.array([fx,fy])
# 	tail = unit_vector(f, np.array([0,0]))

# 	x1 = x - (0.5 * tail[0])
# 	y1 = y - (0.5 * tail[1])
# 	plt.plot([x,x1],[y,y1],color="k")
# 	return


def plot_disks(particles, forces, L, file):


	plt.cla()
	frame = plt.gca()
	for i,particle in enumerate(particles):
		# print particle.id, particle.x, particle.y
		x = particle.x
		y = particle.y
		r = particle.d / 2. 
		c = "r"
		plt.scatter(x,y,color=c)
		# fx = forces[i,0]
		# fy = forces[i,1]
		# plot_force(x,y,fx,fy)
		circle = plt.Circle((x,y),radius=r,color=c,fill=False)
		frame.add_artist(circle)

	plt.axis([0,L[0],0,L[1]])
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])
	plt.savefig("disks/%s.jpg" % file) 



# def plot_voronoi(particles):
#   N = len(particles)
#   coords = np.zeros((N,2))
#   for particle in particles:
#     x = particle.x
#     y = particle.y
#     coords[i,0] = x
#     coords[i,1] = y

#   vor = Voronoi(coords)
  

	