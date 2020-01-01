#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------
def main():

  # Get variance
  variance = get_variance()

  # Get the number of particles
  number_particle = get_number_particle()

  # Get maximum velocity
  maximum_velocity = get_maximum_velocity(variance)

  # Get random velocity
  velocity = get_random_velocity(variance, number_particle)

  # Get sample velocity
  sample_velocity = get_sample_velocity(maximum_velocity)

  # Get maxwell distribution
  maxwell_distribution = get_maxwell_distribution(variance, sample_velocity)

  # Plot velocity distribution
  plot_velocity_distribution(velocity, \
                             maxwell_distribution, \
                             sample_velocity, \
                             number_particle)
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get coefficient
#------------------------------------------------------------------------------
def get_variance():

  # Import
  from numpy import sqrt
  from scipy.constants import Avogadro, elementary_charge, electron_mass

  # Set atomic weight
  atomic_weight = {'e': 0.0, 'Ar': 39.792, 'Kr': 83.798, 'Xe': 131.293}

  while True:
    # Input
    particle = input('Particle: ')

    # Check particle
    if particle in atomic_weight.keys():
      # Break
      break
    else:
      print('Invalid.')

  # Branch for particle
  if (particle == 'e'):
    # Set mass
    mass = electron_mass
  else:
    # Set mass
    mass = atomic_weight[particle] / Avogadro * 1.0e-3

  while True:
    # Input
    temperature = input('Temperature (eV): ')

    # Convert
    temperature = float(temperature)

    # Check temperature
    if (temperature > 0.0):
      # Break
      break
    else:
      print('Invalid.')

  # Get variance
  variance = sqrt(elementary_charge * temperature / mass)

  # Return
  return variance
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get maxwell distribution
#------------------------------------------------------------------------------
def get_maxwell_distribution(variance, sample_velocity):

  # Import
  from scipy.stats import norm

  # Set average
  average = 0.0

  # Get maxwell distribution
  maxwell_distribution = norm.pdf(sample_velocity, average, variance)

  # Return
  return maxwell_distribution
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get maximum velocity
#------------------------------------------------------------------------------
def get_maximum_velocity(variance):

  # Set maximum velocity as three times of variance
  maximum_velocity = 3.0 * variance

  # Return
  return maximum_velocity
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get the number of particles
#------------------------------------------------------------------------------
def get_number_particle():

  while True:
    # Input
    number_particle = input('The number of particles: ')

    # Convert
    number_particle = int(number_particle)

    # Check
    if (number_particle > 0):
      # Break
      break
    else:
      print('Invalid.')

  # Return
  return number_particle
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get random velocity
#------------------------------------------------------------------------------
def get_random_velocity(variance, number_particle):

  # Import
  from numpy import cos, log, sqrt
  from random import random
  from scipy.constants import pi

  # Format
  velocity = []

  for counter in range(number_particle):
    # Get random velocity
    velocity.append(sqrt(- 2.0 * variance ** 2 * log(random())) \
                  * cos(2.0 * pi * random()))

  # Return
  return velocity
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Get sample velocity
#------------------------------------------------------------------------------
def get_sample_velocity(maximum_velocity):

  # Import
  from numpy import linspace

  # Get sample velocity
  sample_velocity = linspace(- maximum_velocity, maximum_velocity, 100)

  # Return
  return sample_velocity
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Plot velocity distribution
#------------------------------------------------------------------------------
def plot_velocity_distribution(velocity, \
                               maxwell_distribution, \
                               sample_velocity, \
                               number_particle):

  # Import
  import matplotlib.pyplot as plt
  from numpy import exp, sqrt
  from scipy.constants import pi

  # Font
  plt.rcParams['font.family'] = 'FreeSans'
  plt.rcParams['mathtext.default'] = 'regular'

  # Set bins
  bins = int(number_particle / 15)

  # Check bins
  if (bins < 10):
    # Minimum
    bins = 10
  elif (bins > 100):
    # Maximum
    bins = 100

  # Make new window
  fig, ax = plt.subplots()

  # Plot
  plt.hist(velocity, bins = bins, normed = True, label = 'Particle')
  plt.plot(sample_velocity, maxwell_distribution, label = 'Maxwell')

  # Set axes label
  ax.set_xlabel('Velocity (m s$^{-1}$)')
  ax.set_ylabel('Probability density')

  # Set legend
  plt.legend()

  # Save figure
  plt.savefig('maxwell-particle.pdf', bbox_inches = 'tight')

  # Close figure
  plt.close()
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Call main
#------------------------------------------------------------------------------
if __name__ == '__main__':
  main()
#------------------------------------------------------------------------------
