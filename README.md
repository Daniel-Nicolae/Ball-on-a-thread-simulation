# Ball-on-a-thread-simulation

The python code simulates the motion of a ball attached to the end of a thread. The other end of the thread is fixed at (0, 0). The ball is given a sudden kick in the horizontal direction. For large initial speeds, it just circles around the centre, but for lower speeeds it happens that the thread loosens and the ball starts falling.

The dynamics simulation was done using a Verlet integrator.

It is possible to show an animation of the whole motion, altough it's unoptimal to dispay it using the current method. A future step is to generate and export a video.
