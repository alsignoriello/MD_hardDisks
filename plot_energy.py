#!/usr/bin/python
import numpy as np 
import matplotlib.pyplot as plt
import sys


dt = float(sys.argv[1])

ke = np.loadtxt("kinetic_energy.txt")
pe = np.loadtxt("potential_energy.txt")

Nt = ke.shape[0]
t = dt * np.arange(0,Nt)

plt.semilogy(t,ke,"b")
plt.semilogy(t,pe,"r")
plt.semilogy(t,ke+pe,"m")
plt.savefig("energy.jpg")
