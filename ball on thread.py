import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def find_theta():
    if x[-1]<=0 and y[-1]<0:
        return np.arctan(x[-1]/y[-1])
    if x[-1]<0 and y[-1] >=0:
        return np.pi/2-np.arctan(y[-1]/x[-1])

    if x[-1]>=0 and y[-1]>0:
        return np.pi + np.arctan(x[-1]/y[-1])
    if x[-1] >0 and y[-1]<=0:
        return 3*np.pi/2-np.arctan(y[-1]/x[-1])

# Various problem constants
R=1
g=9.81
m=1

# Initial speed - vary hmax between 0R and 2R 
hmax = R*1.2
v0=np.sqrt(2*hmax*g)

# Initial position
x=[0]
y=[-R]
vx=[-v0]
vy=[0]

# Initialise lists that will cointain positions of detaching and reattaching to the cirlce
xd=[]
yd=[]
xr=[]
yr=[]

# Time vector
T0=np.pi*R/v0
dt = 0.002
time = np.arange(0, 5*T0, dt)

# parab = 1 means parabolic motion. Otherwise, the particle is on a circle 
parab=0

fig = plt.figure(1)
plt.clf()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.grid()
plt.axis('equal')

# Toggle animation on or off
anim=1

# Motion simulation
for i,t in enumerate(time):

    # Velocity squared and distance to centre squared: needed later
    v2=vx[-1]*vx[-1]+vy[-1]*vy[-1]
    r2=x[-1]**2+y[-1]**2

    theta = find_theta()

    # If on circle, we don't allow the particle to exit
    if r2>=R*R:
        x[-1]/=np.sqrt(r2)/R
        y[-1]/=np.sqrt(r2)/R

        # If it just returned, we switch to the circle case
        if parab == 1:
            parab=0

            # Record return
            xr.append(x[-1])
            yr.append(y[-1])

            theta = find_theta()

            # New velocity along the circle, with the modulus calculated from energy conservation (very inaccurate physically)
            v = np.sqrt(vx[-1]**2+vy[-1]**2)
            vy[-1] = -abs(v*np.sin(theta))
            vx[-1] = abs(v*np.cos(theta))*np.tan(theta)/abs(np.tan(theta))



    # Equilibrium for the circle case, i.e. taut string
    if parab==0:
        T = m*v2/R +m*g*np.cos(theta) # Tension force

        # If tension goes negative, means the string has loosened => parabolic motion
        if T<0:
            parab =1

            #Record detach
            xd.append(x[-1])
            yd.append(y[-1])

    # Parabolic motion means string is loose but we can't allow negative T
    if parab==1:
        T=0
        
    # Acceleration calculations: needed for simulation
    ax = T*np.sin(theta)/m
    ay = -g+T*np.cos(theta)/m

    # Initial simulation step is Euler
    if len(x)==1:
        vx.append(vx[-1]+ax*dt)
        vy.append(vy[-1]+ay*dt)

        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)

    # Verlet simulator
    else:
        x_new=2*x[-1]-x[-2]+ax*dt*dt
        y_new = 2*y[-1]-y[-2]+ay*dt*dt

        x.append(x_new)
        y.append(y_new)

        vx.append((x[-1]-x[-2])/dt)
        vy.append((y[-1]-y[-2])/dt)

    # Animation plot
    if i%6==0 and anim:
        plt.cla()
        plt.grid()
        plt.plot(x, y)
        plt.plot(0, 0, "or")
        plt.plot(xd, yd, "dr")
        plt.plot(xr, yr, "dg")
        plt.plot(x[-1], y[-1], "d")
        plt.pause(0.0000001)

# Final plot
plt.clf()
plt.axis("equal")
plt.plot(0, 0, "or")
plt.plot(xd, yd, "dr")
plt.plot(xr, yr, "dg")
plt.plot(x, y)
plt.grid()
plt.show()







        


