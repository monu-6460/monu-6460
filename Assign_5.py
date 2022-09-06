import numpy as np
import math
imax = 6
jmax = 6
nmax = 50
rw = 0.1
rx = 1.0
ry = 1.0
rz = 0.1
theb = 0.0
then = 90.0
eps = 0.00001
om = 1.5

imap = imax-1
jmap = jmax-1
aim = imap
ajm = jmap
drwx = (rx-rw)/aim
drzy = (ry-rz)/aim
dth = (then - theb)/ajm
pi = math.pi

for j in range(jmax):
    aj = j
    thj = (theb + aj*dth)*pi/180
    cj = cos(thj)
    sj = sin(thj)
    dr = drwx + (drzy - drwx)*aj*ajm
    
