import tkinter as tk
import time
from threading import Thread
from gui import ChessBoardGUI
import random
from mapping import array_to_bits


def run_test(gui: ChessBoardGUI):
    test_patterns = [
        [1 if (i + j) % 2 == 0 else 0 for j in range(8) for i in range(8)],
        [1 if i % 2 == 0 else 0 for i in range(64)],
        [1 if i // 8 == 3 else 0 for i in range(64)],
        [1 if i % 8 == 4 else 0 for i in range(64)]
    ]

    while True:
        for pattern in test_patterns:
            gui.clear_highlights()
            time.sleep(1.5)
            gui.highlight_squares(pattern)
            time.sleep(1.5)

def mapping_test(gui: ChessBoardGUI):

    def generate_6x6_arrays():
        SIZE = 8

        test_arrays = [
            # All ones
            [[1] * SIZE for _ in range(SIZE)],

            # All zeros
            # [[0] * SIZE for _ in range(SIZE)],

            # Checkerboard pattern (starting with 1)
            [[(i + j) % 2 for j in range(SIZE)] for i in range(SIZE)],

            # Checkerboard pattern (starting with 0)
            [[(i + j + 1) % 2 for j in range(SIZE)] for i in range(SIZE)],

            # Half 1's, half 0's (split horizontally)
            [[1 if i < SIZE // 2 else 0 for _ in range(SIZE)] for i in range(SIZE)],

            # Half 1's, half 0's (split vertically)
            [[1 if j < SIZE // 2 else 0 for j in range(SIZE)] for i in range(SIZE)],

            # Random patterns
            [[random.choice([0, 1]) for _ in range(SIZE)] for _ in range(SIZE)],
            [[random.choice([0, 1]) for _ in range(SIZE)] for _ in range(SIZE)],
            [[random.choice([0, 1]) for _ in range(SIZE)] for _ in range(SIZE)],
        ]

        return test_arrays

    test_arrays = generate_6x6_arrays()
    while True:
        for test_array in test_arrays:
            bits = array_to_bits(test_array)
            
            gui.clear_highlights()
            time.sleep(1.5)
            gui.highlight_squares(bits)
            time.sleep(1.5)
            


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessBoardGUI(root)

    # Run the test loop in a separate thread to avoid freezing the GUI
    # Thread(target=run_test, args=(gui,), daemon=True).start()
    Thread(target=mapping_test, args=(gui,), daemon=True).start()

    root.mainloop()
