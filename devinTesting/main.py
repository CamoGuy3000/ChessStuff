
#* Control File

import RPi.GPIO as GPIO
from time import sleep
from mapping import array_to_bits
from test import *


#########################################
#####         Pin Out Setup         #####
#########################################

# Define Raspberry Pi GPIO pins for shift register
DATA_PIN = 2   # DS (SER) - Serial Data Input
CLOCK_PIN = 3  # SHCP (SRCLK) - Shift Register Clock
LATCH_PIN = 4  # STCP (RCLK) - Storage Register Clock

# GPIO Setup
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(DATA_PIN, GPIO.OUT)
GPIO.setup(CLOCK_PIN, GPIO.OUT)
GPIO.setup(LATCH_PIN, GPIO.OUT)

# Environment setup
NUM_COILS = 8


"""
  Send data to shift register.
  
  Args:
    bits (list of bool): list of True (1) / False (0) values.
  
  TODO: Choose if we want to have a length check, right now this will just send all bytes to shift register
"""
def shift_out(bits):

  # GPIO.output(LATCH_PIN, GPIO.LOW)  # Latch low to start data transfer

  for bit in bits: # Shift out all bits
    GPIO.output(DATA_PIN, GPIO.HIGH if bit else GPIO.LOW)  # Set data line
    GPIO.output(CLOCK_PIN, GPIO.HIGH)  # Pulse clock to shift bit in
    sleep(0.001)  # Small delay for stability
    GPIO.output(CLOCK_PIN, GPIO.LOW)

  GPIO.output(LATCH_PIN, GPIO.HIGH)  # Latch high to store data
  sleep(0.001)
  GPIO.output(LATCH_PIN, GPIO.LOW)  # Latch high to store data



"""
  Reset to 0

  Args:
    num (integer): the number of things (leds, magnets, etc) you want off
      Defaulted to NUM_COILS
"""
def reset(num=NUM_COILS):
  shift_out([False]*num)



"""
  Resets to 0, GPIO to LOW, and cleans up GPIO

  Args:
    num (integer): the number of things (leds, magnets, etc) in circuit
      Defaulted to NUM_COILS
"""
def clean_and_kill(num=NUM_COILS):
  print("\nExiting...")

  reset(num)

  # Set everything to low
  GPIO.output(LATCH_PIN, GPIO.LOW)
  GPIO.output(CLOCK_PIN, GPIO.LOW)
  GPIO.output(CLOCK_PIN, GPIO.LOW)

  GPIO.cleanup()  # Clean up GPIO pins before exit



if __name__ == "__main__":

  # Set everything to low
  GPIO.output(LATCH_PIN, GPIO.LOW)
  GPIO.output(CLOCK_PIN, GPIO.LOW)
  GPIO.output(CLOCK_PIN, GPIO.LOW)

  flicker_test()

  array_to_bits_test()
