"""Uniform-wind acoustic propagation in Cartesian metres; no real locations.

The trajectory callable returns position and ground-relative velocity arrays for
emission times. This readable public module contains the model equations, not
private aircraft trajectories or the full historical search orchestration.
"""
import numpy as np

def propagation(trajectory, emission_time_s, observer_m, sound_speed_m_s=343., wind_m_s=(0.,0.,0.)):
    t=np.atleast_1d(emission_time_s).astype(float)
    p,v=trajectory(t);w=np.asarray(wind_m_s,float);c=float(sound_speed_m_s)
    if c<=0 or w@w>=c*c:raise ValueError('Require positive c and subsonic wind')
    q=np.asarray(observer_m,float)-p;a=c*c-w@w;b=q@w
    lag=(-b+np.sqrt(b*b+a*np.sum(q*q,axis=1)))/a
    ray=q-lag[:,None]*w;norm=np.linalg.norm(ray,axis=1)
    if np.any(norm==0):raise ValueError('Coincident listener and source')
    n=ray/norm[:,None];derivative=1-np.sum(n*v,axis=1)/(c+n@w)
    return lag,derivative,np.sqrt(np.sum(q*q,axis=1))

def received_doppler(trajectory, receive_time_s, observer_m, sound_speed_m_s=343., wind_m_s=(0.,0.,0.)):
    tr=np.atleast_1d(receive_time_s).astype(float);te=tr-10
    for _ in range(20):
        tau,den,_=propagation(trajectory,te,observer_m,sound_speed_m_s,wind_m_s)
        if np.any(den<=0):raise ValueError('Non-monotonic retarded-time branch')
        step=np.clip((te+tau-tr)/den,-100,100);te-=step
        if np.max(np.abs(step))<1e-9:break
    tau,den,distance=propagation(trajectory,te,observer_m,sound_speed_m_s,wind_m_s)
    if np.max(np.abs(te+tau-tr))>1e-6:raise ValueError('Propagation solve did not converge')
    return 1/den,te,distance
