_EMPTY = ' ' # Used to indicate empty spaces in the board

class InvalidMoveError(ValueError):
    pass

class ConnectFourBoard:

    """Represents a Connect 4 board. Handles board state and checks moves for validity."""

    def __init__(self, num_rows, num_cols):
        """Initialize a new board"""
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.clear()

    def clear(self):
        """Replace all pieces with empty spaces."""
        self.rows = list()
        for row in range(self.num_rows):
            self.rows.append([_EMPTY for col in range(self.num_cols)])

    def display(self):
        """Display the current board state"""
        for row in range(self.num_rows):
            print(f'\t|{"|".join(self.rows[row])}|')
        print('\t ' + ' '.join([str(col) for col in range(self.num_cols)]))

    def check_winner(self):
        """Check whether someone has won the game."""
        # TODO: Implement this function instead of just returning false
        return False

    def is_full(self):
        """Check whether the board is full."""
        # TODO: Implement this function instead of just returning false
        return False

    def add_piece(self, col, symbol):
        """Add a piece to the specified column."""
        # TODO: Add code to check if the move is valid (and raise InvalidMoveError if not)

        # Find the first empty row in col and replace it with symbol
        for row in reversed(range(self.num_rows)):
            if self.rows[row][col] is _EMPTY:
                self.rows[row][col] = symbol
                break
