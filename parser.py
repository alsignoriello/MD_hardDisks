#!/usr/bin/python

def write_parameters(parameters):
	f = open("parameters.txt", "w+")
	for key,value in parameters.iteritems():
		if type(value) == float:
			f.write("%s\t%.3f\n" % (key,value))
		if type(value) == int:
			f.write("%s\t%d\n" % (key,value))
	f.close()


def write_coords(particles, t):
	f = open("positions/%d.txt" % t, "w+")
	for particle in particles:
		f.write("%f\t%f\n" % (particle.x,particle.y))
	f.close()
