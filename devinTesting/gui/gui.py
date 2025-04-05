import tkinter as tk

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
                square = tk.Label(self.board_frame, bg=color, width=8, height=4, borderwidth=1, relief="solid")
                square.grid(row=row, column=col)
                self.squares[row][col] = square

    def highlight_squares(self, positions, color="yellow"):
        """Highlight squares from a list of (row, col) or from a flat list of 0's and 1's (length 64).
        Each position can be a tuple (row, col) or a list of 1's and 0's.
        """
        if isinstance(positions, list) and all(isinstance(p, int) for p in positions):
            if len(positions) != 64:
                raise ValueError("List must be 64 elements long.")
            positions = [(i // 8, i % 8) for i, val in enumerate(positions) if val == 1]
        elif isinstance(positions, tuple):
            positions = [positions]
        for row, col in positions:
            if 0 <= row < 8 and 0 <= col < 8:
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
    gui.highlight_squares(binary_map)  # Example usage with binary map
    root.mainloop()
