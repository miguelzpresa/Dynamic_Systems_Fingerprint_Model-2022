# Copyright (C) 2022  Jadiel Zuñiga Rodriguez
#                     Luis Aarón Nieto Cruz
#                     Miguel Ángel Zamorano Presa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from itertools import product
import math
import random




def Rect_to_uv_dc(x, y, z) :
    n = Normalize(sphere_surface_point - sphere_center)
    u = atan2(nx, nz) / (2*np.pi) + 0.5
    v = n.y * 0.5 + 0.5

def x_coord(theta) :
    return np.sin(theta)

def f(x, y) :
    return np.sin(np.sqrt(x**2 + y**2))

def rho (u, v) :
    global r0
    r0 = 1
    mu = 1
    sigma = 0.05
    c = []
    for i in range (17) :
        c.append(1)
        #c.append(random.normalvariate(mu,sigma))
        
    theta = (math.atan(-c[15]*(v-c[16]))+1)/2
    return ((c[1]+(c[2]*math.exp(-((v-c[3])**2)/c[4])+c[5])*math.sin(u/r0)) + ((c[6]*math.exp(-((v-c[7])**2)/c[8])+c[9])*math.sin((2*u)/r0)) + ((c[10]*math.exp(-((v-c[11])**2)/c[12])+c[13])*math.sin((3*u)/r0)))*theta + (1/math.sqrt((math.cos(u/r0)**2/(c[1]**2))+(math.sin(v/r0)**2/(c[14]**2))))*(1-theta)

def r_vec (u, v) :
    if v < 0 :
        return rho(u, v)*math.cos(u/r0) , v , rho(u, v)*math.sin(u/r0)
    if v > 0 :
        return rho(u, v)*math.cos(u/r0)*math.cos(v/r0) , rho(u, v)*math.sin(v/r0) , rho(u, v)*math.sin(u/r0)*math.cos(v/r0)

def azel_t_thetaphi(az, el) :
    cos_theta = np.cos(el) * np.cos(az)
    tan_phi = np.tan(el) / np.sin(az)
    theta = np.arccos(cos_theta)
    phi = np.arctan2(np.tan(el), np.sin(az))
    phi = (phi + 2 * np.pi) % (2 * np.pi)
    return theta, phi

def thetaphi_to_azel(theta, phi) :
    sin_el = np.sin(phi) * np.sin(theta)
    tan_az = np.cos(phi) * np.tan(theta)
    el = np.arcsin(sin_el)
    az = np.arctan(tan_az)
    return az, el

def thetaphi_to_uv(theta, phi) :
    u = np.sin(theta) * np.cos(phi)
    v = np.sin(theta) * np.sin(phi)
    w = np.cos(theta)
    return u, v

def azel_to_uv(az, el) :
    u = np.cos(el) * np.sin(az)
    v = np.sin(el)
    w = np.cos(az) * np.cos(el)
    return u, v

def uv_to_thetaphi(u, v) :
    theta = np.arcsin(np.sqrt(u**2 + v**2))
    phi = np.arctan2(u, v)
    phi = (phi + 2 * np.pi) % (2 * np.pi)
    return theta, phi

def uv_to_azel(u, v) :
    az = np.arctan2(u, np.sqrt(1 - u**2 - v**2))
    el = np.arcsin(v)
    return az, el

def plot_compare(a, b, ap, bp, title = '', show = False, nf = True) :
    if nf :
        plt.figure()
    plt.subplot(211)
    plt.plot(a, ap, '.', label = title)
    plt.legend()
    plt.subplot(212)
    plt.plot(b, bp, '.', label = title)
    if show :
        plt.show()



#fig = plt.Figure(figsize=(5,5))
#ax = plt.axes(projection="3d")

# Data
r = 0.05
phi = np.linspace(0, (2*np.pi), 30)
theta = np.linspace(0, np.pi, 30)

# Yielding sphere
u, v = np.meshgrid(phi, theta)
x = np.cos(u) * np.sin(v)
y = np.sin(v) * np.sin(u)
z = np.cos(v)
#ax.plot_surface(x, y, z, cmap = plt.cm.YlGnBu_r, alpha = 0.6)
#plt.grid()
#plt.show()



#fig = plt.Figure(figsize=(5, 5))
#ax = plt.axes(projection="3d")
# Data
r = 0.05
phi = np.linspace(0, (2*np.pi), 30)
theta = np.linspace(0, np.pi, 30)
coefi = (1, 5, 3)
rx, ry, rz = 1 / np.sqrt(coefi)

# Yielding sphere
u, v = np.meshgrid(phi, theta)
x = np.cos(u) * np.sin(0.5*v)
x *= rx
y = np.sin(v) * np.sin(u)
y *= ry
z = np.cos(0.5*v)
z *= rz
#ax.plot_surface(x, y, z, alpha = 0.6, cmap = plt.cm.YlGnBu_r)
#plt.grid()
#plt.show()



#fig = plt.figure(figsize = plt.figaspect(1))
#ax = fig.add_subplot(111, projection = '3d')

coefs = (2, 1, 1)  # COefficients in a0/c x**2 + a1/c y**2 + a2/c z**2 = 1
# Radii corresponding to the coefficients :
rx, ry, rz = 1/np.sqrt(coefs)

u = np.linspace(0, 2*np.pi, 100)
v = np.linspace(0, np.pi, 100)

# Cartesian coordinates that correspond to the spherical angles :
# (this is the equation of an ellipsoid) :
x = rx * np.outer(np.cos(u), np.sin(v))
y = ry * np.outer(np.sin(u), np.sin(v))
z = rz * np.outer(np.ones_like(u), np.cos(v))

# Plot :
#ax.plot_surface(x, y, z, alpha = 0.6, cmap = 'BuPu')
# Adjustment of the axes, so that they all have the same span:
max_radius = max(rx, ry, rz)
#for axis in 'xyz' :
#    getattr(ax, 'set_{}lim'.format(axis))((-max_radius, max_radius))

#plt.show()



data = np.linspace(0, 2*(np.pi), 5)
y, x = np.meshgrid(data, data)

#figure = plt.Figure(figsize = (5, 4))
#ax = plt.axes(projection = "3d")
data = np.linspace(0, 2*(np.pi), 5)

X, Y = np.meshgrid(data,data)
Z = f(X, Y)
#ax.plot_surface(X, Y, Z)



fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

U = np.arange(-1.0, 1.0, 0.01)
V = np.arange(-1.0, 1.0, 0.01)

S = []
for u in U :
    for v in V :
        S.append(r_vec(u,v))

#print("Esto es S")
#print(S)

#for u, v in zip(U, V) :
#    S1.append(r_vec(u, v))

#print("Esto es S1")
#print(S1)

S1 = []
S2 = []
S3 = []

for i in S :
    S1.append(i[0])
    S2.append(i[1])
    S3.append(i[2])

ax.scatter(S1, S2, S3,s = 0.5 )
#ax.quiver(U, V, V, S1, S2, S3)

plt.grid()
plt.show()
