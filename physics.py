import numpy as np
import scipy as sp




def update_velocity_position(particle, old_time, new_time, force):
	dt = new_time - old_time
	particle.velocity = particle.velocity + (force/particle.mass)*dt
	particle.position = particle.position +particle.velocity*dt



def handle_collisions(particle1):

	pass