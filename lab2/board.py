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

    def check_winner(self,symbol,col,row):
        """Check whether someone has won the game."""
        # first, check horizontal wins based on col
        num_right=0
        num_left=0
        col_check=col
        while (col_check < self.num_cols-1) and self.rows[row][col_check+1]== symbol:
            num_right+=1
            col_check+=1
        col_check=col
        while col_check>=1 and self.rows[row][col_check-1]==symbol:
            num_left+=1
            col_check-=1
        if num_right+num_left>=3:
            return True
        #now time for the vertical checks
        num_up=0
        num_down=0
        row_check=row
        #count number below our move, only need to check below because they fall from the top
        while (row_check < self.num_rows-1) and self.rows[row_check+1][col]==symbol:
            num_down+=1
            row_check+=1
        if num_down>= 3:
            return True
        #diagonal checks, this one will be on the diagonal towards the top right
        # TODO: Implement this function instead of just returning false
        return False

    def is_full(self):
        """Check whether the board is full."""
        for col in range(self.num_cols):
            if self.rows[0][col] == _EMPTY:
                return False
        # TODO: Implement this function instead of just returning false
        return True

    def add_piece(self, col, symbol):
        """Add a piece to the specified column."""
        # TODO: Add code to check if the move is valid (and raise InvalidMoveError if not)
        if col > self.num_cols:
            raise InvalidMoveError('Column out of range')
        if self.rows[0][col] != _EMPTY:
            raise InvalidMoveError('Column is full!!!!')
        # Find the first empty row in col and replace it with symbol
        for row in reversed(range(self.num_rows)):
            if self.rows[row][col] is _EMPTY:
                self.rows[row][col] = symbol
                return row
                break