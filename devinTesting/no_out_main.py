
#* Control File

# import RPi.GPIO as GPIO
from time import sleep
from mapping import MAPPING


#########################################
#####         Pin Out Setup         #####
#########################################

# Define Raspberry Pi GPIO pins for shift register
DATA_PIN = 2   # DS (SER) - Serial Data Input
CLOCK_PIN = 3  # SHCP (SRCLK) - Shift Register Clock
LATCH_PIN = 4  # STCP (RCLK) - Storage Register Clock

# GPIO Setup
# GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
# GPIO.setup(DATA_PIN, GPIO.OUT)
# GPIO.setup(CLOCK_PIN, GPIO.OUT)
# GPIO.setup(LATCH_PIN, GPIO.OUT)


"""
  Send 8-bit data to shift register.
  
  Args:
    bits (list of bool): list of True (1) / False (0) values.
  
  TODO: Choose if we want to have a length check, right now this will just send all bytes to shift register
"""
def shift_out(bits):

  # GPIO.output(LATCH_PIN, GPIO.LOW)  # Latch low to start data transfer

  for bit in bits: # Shift out all bits
    # GPIO.output(DATA_PIN, GPIO.HIGH if bit else GPIO.LOW)  # Set data line
    print("DATA_PIN,", "HIGH" if bit else "LOW")

    # GPIO.output(CLOCK_PIN, GPIO.HIGH)  # Pulse clock to shift bit in
    print("CLOCK_PIN,", "HIGH")


    sleep(0.001)  # Small delay for stability
    # GPIO.output(CLOCK_PIN, GPIO.LOW)
    print("CLOCK_PIN,", "LOW")

  # GPIO.output(LATCH_PIN, GPIO.HIGH)
  print("LATCH_PIN,", "HIGH")
  sleep(0.001)
  # GPIO.output(LATCH_PIN, GPIO.LOW)
  print("LATCH_PIN,", "LOW")


if __name__ == "__main__":

  # GPIO.output(LATCH_PIN, GPIO.LOW)
  print("LATCH_PIN,", "LOW")

  # GPIO.output(CLOCK_PIN, GPIO.LOW)
  print("CLOCK_PIN,", "LOW")

  # GPIO.output(CLOCK_PIN, GPIO.LOW)
  print("CLOCK_PIN,", "LOW")


  try:
    while True:
      # Example patterns
      test_patterns = [
        [False, False, False, False, False, False, False, False],  # All off
        [True, True, True, True, True, True, True, True],  # All on
        [True, False, True, False, True, False, True, False],  # Alternating 10101010
        [False, True, False, True, False, True, False, True]  # Alternating 01010101
      ]

      for pattern in test_patterns:
        shift_out(pattern)
        print(f"Sent data: {pattern}")
        sleep(2)  # Wait before next pattern


  except KeyboardInterrupt:
    print("\nExiting...")
    # GPIO.cleanup()  # Clean up GPIO pins before exit
    print("CLEANUP")
