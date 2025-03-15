
#* Testing script

from time import sleep
# from main import shift_out, clean_and_kill
from mapping import array_to_bits
import random


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
        # shift_out(pattern)
        print(f"Sent data: {pattern}")
        sleep(2)  # Wait before next pattern


  except KeyboardInterrupt:
    print(f"cleaning and killing...")
    # clean_and_kill()


def array_to_bits_test():

  def generate_6x6_arrays():
    test_arrays = [
        # All ones
        [[1] * 6 for _ in range(6)],

        # All zeros
        [[0] * 6 for _ in range(6)],

        # Checkerboard pattern (starting with 1)
        [[(i + j) % 2 for j in range(6)] for i in range(6)],

        # Checkerboard pattern (starting with 0)
        [[(i + j + 1) % 2 for j in range(6)] for i in range(6)],

        # Half 1's, half 0's (split horizontally)
        [[1 if i < 3 else 0 for _ in range(6)] for i in range(6)],

        # Half 1's, half 0's (split vertically)
        [[1 if j < 3 else 0 for j in range(6)] for i in range(6)],

        # Random patterns
        [[random.choice([0, 1]) for _ in range(6)] for _ in range(6)],
        [[random.choice([0, 1]) for _ in range(6)] for _ in range(6)],
        [[random.choice([0, 1]) for _ in range(6)] for _ in range(6)],
    ]

    return test_arrays

  test_arrays = generate_6x6_arrays()
  # test_arrays = [
  #   [
  #     [1, 1, 1, 1],
  #     [1, 1, 1, 1],
  #   ],
  #   [
  #     [0, 0, 0, 0],
  #     [0, 0, 0, 0],
  #   ],
  #   [
  #     [1, 0, 1, 0],
  #     [0, 1, 0, 1],
  #   ],
  #   [
  #     [0, 1, 0, 1],
  #     [1, 0, 1, 0],
  #   ],
  #   [
  #     [0, 0, 0, 0],
  #     [0, 0, 0, 0],
  #   ],
  # ]

  for test_array in test_arrays:
    bits = array_to_bits(test_array)
    print(bits)


if __name__ == "__main__":
  # flicker_test()
  array_to_bits_test()

