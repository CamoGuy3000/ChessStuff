

# MAPPING = [
#     [3, 4, 1, 0, 5, 2],
#     [6, 7, 8, 9, 10, 11],
#     [12, 13, 14, 15, 16, 17],
#     [18, 19, 20, 21, 22, 23],
#     [24, 25, 26, 27, 28, 29],
#     [30, 31, 32, 33, 34, 35]
# ]

MAPPING = [
    [0, 1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30, 31],
    [32, 33, 34, 35, 36, 37, 38, 39],
    [40, 41, 42, 43, 44, 45, 46, 47],
    [48, 49, 50, 51, 52, 53, 54, 55],
    [56, 57, 58, 59, 60, 61, 62, 63],
]

"""
  Turns a 2D array of 1's and 0's to the flat bits to send through shift_out
"""
def array_to_bits(array: list[list[int]]) -> list[bool]:


  # Check lengths
  if len(array) > len(MAPPING):
    print("ERROR: `array_to_bits` array size mismatch.")
    return [-1]
  for i in range(len(array)):
    if len(array[i]) > len(MAPPING[i]):
      print("ERROR: `array_to_bits` array size mismatch.")
      return [-1]

  bits = [0]*(sum(len(sub_mapping) for sub_mapping in MAPPING))
  # print(bits)

  for i in range(len(array)):
    for j in range(len(array[i])):
      # print(f"{MAPPING[i][j]}: " + ("on" if array[i][j] == 1 else "off"))
      bits[MAPPING[i][j]] = array[i][j]


  return bits


if __name__ == "__main__":
  
  arr = [
    [1, 1, 0, 0, 1, 1], 
    [1, 1, 1]
  ]

  print(array_to_bits(arr))

