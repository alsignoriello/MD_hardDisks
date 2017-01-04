#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle
from scipy.spatial import Voronoi, voronoi_plot_2d


def plot_disks(particles, L, color, fill, t):


	plt.cla()
	frame = plt.gca()
	for i,particle in enumerate(particles):
		# print particle.id, particle.x, particle.y
		x = particle.x
		y = particle.y
		r = particle.d / 2. 
		circle = plt.Circle((x,y),radius=r,color=color,fill=fill)
		frame.add_artist(circle)

	plt.axis([0,L[0],0,L[1]])
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])
	plt.savefig("disks/%s.jpg" % t) 
	plt.close()



def plot_voronoi(particles, L, color, t):
  	N = len(particles)
  	coords = np.zeros((N,2))
  	d = particles[0].d
    
  	for i,particle in enumerate(particles):
  		x = particle.x
  		y = particle.y
  		coords[i,0] = x
  		coords[i,1] = y
  		plt.scatter(x,y,color=color,marker='.')

  	vor = Voronoi(coords)

 	for edge in vor.ridge_vertices:
  		e1 = edge[0]
  		e2 = edge[1]

  		if e1 != -1 and e2 != -1:
  			x1,y1 = vor.vertices[e1,:]
  			x2,y2 = vor.vertices[e2,:]
  			plt.plot([x1,x2],[y1,y2],color="c")

	plt.axis([d,L[0]-d,d,L[1]-d])
	frame = plt.gca()
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])
	plt.savefig("voronoi/%s.jpg" % t)
	plt.close()


