"""Synthetic physics checks. Arbitrary coordinates, not a recorded location."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from doppler import propagation,received_doppler

def trajectory(t):
    return np.column_stack([65*t,np.full(t.shape,2200.),np.full(t.shape,900.)]),np.column_stack([np.full(t.shape,65.),np.zeros_like(t),np.zeros_like(t)])
t=np.array([-35.,-10.,20.,50.]);w=(7.,-4.,1.);o=np.zeros(3);tau,d,_=propagation(trajectory,t,o,343,w);eps=1e-3
plus=propagation(trajectory,t+eps,o,343,w)[0];minus=propagation(trajectory,t-eps,o,343,w)[0]
err=np.max(np.abs(d-(1+(plus-minus)/(2*eps))))
assert err<1e-7,err
factor,te,_=received_doppler(trajectory,t+tau,o,343,w)
assert np.max(np.abs(te-t))<1e-7
p,v=trajectory(t);r=np.linalg.norm(p,axis=1);rdot=np.sum(p*v,axis=1)/r
assert np.max(np.abs(propagation(trajectory,t,o)[1]-(1+rdot/343)))<1e-12
print('PASS: finite-difference derivative, retarded-time inversion, and still-air Doppler sign. Max derivative error:',err)
