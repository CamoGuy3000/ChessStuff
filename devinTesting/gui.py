import tkinter as tk

# Adjustable square size
# 1 for tiny, 2 for medium, 3 for good sized, 4 for full screen
    # this is probably dependent on screen size
BOARD_SIZE = 3


tile_width = BOARD_SIZE*4
tile_height = tile_width // 2

class ChessBoardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Board")
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.create_board()

    def create_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                square = tk.Label(self.board_frame, bg=color, width=tile_width, height=tile_height, borderwidth=1, relief="solid")
                square.grid(row=row, column=col)
                self.squares[row][col] = square

    def highlight_squares(self, positions, color="yellow"):
        if isinstance(positions, list) and all(isinstance(p, int) for p in positions):
            # if len(positions) != 64:
            #     raise ValueError("List must be 64 elements long.")
            positions = [(i // 8, i % 8) for i, val in enumerate(positions) if val == 1]
        elif isinstance(positions, tuple):
            positions = [positions]
        for row, col in positions:
            if 0 <= row < 8 and 0 <= col < 8:
                self.squares[row][col].config(bg=color)

    def clear_highlights(self):
        """Reset all squares to their original colors."""
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                self.squares[row][col].config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessBoardGUI(root)
    binary_map = [0, 1, 0, 1, 0, 1, 0, 1,
                  0, 1, 0, 1, 1, 0, 1, 0,
                  1, 0, 0, 1, 0, 1, 0, 1,
                  1, 0, 1, 0, 1, 0, 0, 1,
                  0, 1, 0, 1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0, 0, 0, 0]
    gui.highlight_squares(binary_map)
    # gui.clear_highlights()
    root.mainloop()