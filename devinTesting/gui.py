import tkinter as tk

#TODO: Turns, un pasant, castling

# Adjustable square size
# 1 for tiny, 2 for medium, 3 for good sized, 4 for full screen
    # this is probably dependent on screen size
BOARD_SIZE = 3

tile_width = BOARD_SIZE*4
tile_height = tile_width // 2

class ChessPiece:
    def __init__(self, name, color):
        self.name = name  # e.g., 'P', 'K', 'Q'
        self.color = color  # 'white' or 'black'

    def __str__(self):
        return f"{self.color[0].upper()}{self.name}"

class ChessBoardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Board")
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        self.pieces = [[None for _ in range(8)] for _ in range(8)]
        self.selected_square = None
        self.valid_moves = []
        self.create_board()
        self.setup_pieces()

    def create_board(self):
        colors = ["white", "gray"]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                square = tk.Label(self.board_frame, bg=color, width=tile_width, height=tile_height, borderwidth=1, relief="solid", font=("Arial", 16))
                square.grid(row=row, column=col)
                square.bind("<Button-1>", lambda e, r=row, c=col: self.on_square_click(r, c))
                self.squares[row][col] = square

    def on_square_click(self, row, col):
        if self.selected_square:
            if (row, col) in self.valid_moves:
                self.move_piece(self.selected_square, (row, col))
                self.selected_square = None
                self.valid_moves = []
                self.clear_highlights()
                return

        piece = self.pieces[row][col]
        self.clear_highlights()
        if piece:
            self.selected_square = (row, col)
            self.highlight_squares((row, col), color="cyan")  # Highlight selected piece
            self.valid_moves = self.get_valid_moves(row, col)
            self.highlight_squares(self.valid_moves, color="lightgreen")
        else:
            self.selected_square = None
            self.valid_moves = []

    def move_piece(self, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        piece = self.pieces[from_row][from_col]
        self.place_piece(to_row, to_col, piece)
        self.remove_piece(from_row, from_col)

    def get_valid_moves(self, row, col):
        piece = self.pieces[row][col]
        if not piece:
            return []

        directions = []
        moves = []
        name = piece.name.upper()
        color = piece.color

        def in_bounds(r, c):
            return 0 <= r < 8 and 0 <= c < 8

        def is_opponent(r, c):
            target = self.pieces[r][c]
            return target and target.color != color

        def is_empty(r, c):
            return self.pieces[r][c] is None

        if name == 'P':
            dir = -1 if color == 'white' else 1
            start_row = 6 if color == 'white' else 1

            # forward
            if in_bounds(row + dir, col) and is_empty(row + dir, col):
                moves.append((row + dir, col))
                if row == start_row and is_empty(row + 2 * dir, col):
                    moves.append((row + 2 * dir, col))

            # captures
            for dc in [-1, 1]:
                r, c = row + dir, col + dc
                if in_bounds(r, c) and is_opponent(r, c):
                    moves.append((r, c))

        elif name == 'R':
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        elif name == 'B':
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        elif name == 'Q':
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        elif name == 'N':
            knight_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                            (1, -2), (1, 2), (2, -1), (2, 1)]
            for dr, dc in knight_moves:
                r, c = row + dr, col + dc
                if in_bounds(r, c) and (is_empty(r, c) or is_opponent(r, c)):
                    moves.append((r, c))
        elif name == 'K':
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if in_bounds(r, c) and (is_empty(r, c) or is_opponent(r, c)):
                    moves.append((r, c))
            return moves  # King moves only one square, return here

        if directions:
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while in_bounds(r, c):
                    if is_empty(r, c):
                        moves.append((r, c))
                    elif is_opponent(r, c):
                        moves.append((r, c))
                        break
                    else:
                        break
                    r += dr
                    c += dc

        return moves

    def place_piece(self, row, col, piece: ChessPiece):
        self.pieces[row][col] = piece
        self.squares[row][col].config(text=str(piece))

    def remove_piece(self, row, col):
        self.pieces[row][col] = None
        self.squares[row][col].config(text="")

    def highlight_squares(self, positions, color="yellow"):
        if isinstance(positions, list) and all(isinstance(p, int) for p in positions):
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

    def setup_pieces(self):
        # Setup black pieces (top of GUI)
        order = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        for col in range(8):
            self.place_piece(0, col, ChessPiece(order[col], 'black'))
            self.place_piece(1, col, ChessPiece('P', 'black'))

        # Setup white pieces (bottom of GUI)
        for col in range(8):
            self.place_piece(6, col, ChessPiece('P', 'white'))
            self.place_piece(7, col, ChessPiece(order[col], 'white'))

if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessBoardGUI(root)
    root.mainloop()
