import tkinter as tk
import time
from threading import Thread
from gui import ChessBoardGUI


def run_test(gui):
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


if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessBoardGUI(root)

    # Run the test loop in a separate thread to avoid freezing the GUI
    Thread(target=run_test, args=(gui,), daemon=True).start()

    root.mainloop()
