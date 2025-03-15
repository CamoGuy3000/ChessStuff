
#* Testing script

import RPi.GPIO as GPIO
from time import sleep
from main import shift_out, clean_and_kill
from mapping import array_to_bits


def flicker_test():
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
    clean_and_kill()


def array_to_bits_test():
  test_arrays = [
    [
      [1, 1, 1, 1],
      [1, 1, 1, 1],
    ],
    [
      [0, 0, 0, 0],
      [0, 0, 0, 0],
    ],
    [
      [1, 0, 1, 0],
      [0, 1, 0, 1],
    ],
    [
      [0, 1, 0, 1],
      [1, 0, 1, 0],
    ],
    [
      [0, 0, 0, 0],
      [0, 0, 0, 0],
    ],
  ]

  for test_array in test_arrays:
    bits = array_to_bits(test_array)
    print(bits)


if __name__ == "__main__":
  # flicker_test()
  array_to_bits_test()

