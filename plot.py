#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from Particle import Particle
from scipy.spatial import Voronoi
  
# % plot particles
# if(plotit && rem(nt-1,Nplotskip)==0)
#   voronoi(mod(x,Lx),mod(y,Ly));
#   hold on;
#   plot(mod(x(1),Lx),mod(y(1),Ly),'.r','Markersize',30);
#   hold off;
#   axis('equal');
#   axis([0 Lx 0 Ly]);
#   set(gca,'xtick',[]);
#   set(gca,'ytick',[]);
#   drawnow;
#   saveas(gcf, strcat(int2str(nt), '.jpg'))
# end


def plot_disks(particles, L):
	plt.cla()
	frame = plt.gca()
	for particle in particles:
		x = particle.x
		y = particle.y
		r = particle.d / 2. 
		circle = plt.Circle((x,y),radius=r,color="c",fill=False)
		frame.add_artist(circle)

	plt.axis([0,L[0],0,L[1]])
	frame.axes.get_xaxis().set_ticks([])
	frame.axes.get_yaxis().set_ticks([])
	plt.show() 



# def plot_voronoi(particles):
#   N = len(particles)
#   coords = np.zeros((N,2))
#   for particle in particles:
#     x = particle.x
#     y = particle.y
#     coords[i,0] = x
#     coords[i,1] = y

#   vor = Voronoi(coords)
  

	