import numpy as np
import scipy as sp




def update_velocity_position(particle, old_time, new_time, force):
	dt = new_time - old_time
	particle.velocity = particle.velocity + (force/particle.mass)*dt
	particle.position = particle.position +particle.velocity*dt
	handle_boundaries(particle)
	if particle.position[0] >150 and particle.position[0] < 250 and particle.position[1] >=700:
		return False
	else:
		return True


def handle_holes(particle, holes, hole_size):
	for hole in holes:
		if (particle.position[0] < hole[0]+hole_size and particle.position[0] > hole[0]
			and particle.position[1] < hole[1]+ hole_size and particle.position[1] > hole[1]):
			return hole
	return None



def handle_boundaries(particle):
	print ("positions")
	print (particle.position)
	print("velocities")
	print (particle.velocity)	
	if particle.position[1] >=700 and (particle.position[0] <150 or particle.position[0] >250):
		particle.position[1] = 700 - (particle.position[1]-700)
		particle.velocity[1] = - particle.velocity[1]

	if particle.position[1] <= 0:
		particle.position[1] = -particle.position[1]
		particle.velocity[1] = - particle.velocity[1]

	if particle.position[0] <=0:
		particle.position[0] = -particle.position[0]
		particle.velocity[0] = - particle.velocity[0]

	if particle.position[0]>=390:
		particle.position[0] = 390 - (particle.position[0]-390)
		particle.velocity[0] = - particle.velocity[0]

	if particle.position[1] >100:
		if particle.position[0] >= 331 and particle.position[0] <=370 and particle.velocity[0] >0:
			particle.position[0] = 331 - (particle.position[0]-331)
			particle.velocity[0] = - particle.velocity[0] 

		if particle.position[0] >= 350 and particle.position[0] <=370 and particle.velocity[0] <0:
			particle.position[0] = 370 + (370 - particle.position[0])
			particle.velocity[0] = - particle.velocity[0] 