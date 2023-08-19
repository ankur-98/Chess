from typing import Dict, List, Set, Tuple
from config import BOARD_SIZE


class Piece:
    """
    A class representing a chess piece.

    Attributes:
    - color (str): The color of the piece, either "white" or "black".
    - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
    - symbol (str): The symbol representing the piece on the board.board.

    Methods:
    - legal_moves(board: object]) -> Set[Tuple[int, int]]: Returns a set of legal moves for the piece on the given board.board.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Initializes a new instance of the Piece class.

        Parameters:
        - color (str): The color of the piece, either "white" or "black".
        - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        self._color = color
        self._position = position
        self._symbol = None

    def __name__(self):
        return self.__class__.__name__

    @property
    def color(self) -> str:
        """
        Returns the color of the piece.

        Returns:
        - (str): The color of the piece, either "white" or "black".
        """
        return self._color

    @property
    def position(self) -> Tuple[int, int]:
        """
        Returns the position of the piece.

        Returns:
        - (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        return self._position

    @position.setter
    def position(self, value: Tuple[int, int]):
        """
        Sets the position of the piece.

        Parameters:
        - value (tuple): The new position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        self._position = value

    @property
    def row(self) -> int:
        """
        Returns the row of the king on the board.board.

        Returns:
        - row (int): The row of the king on the board.board.
        """
        return self.position[0]

    @property
    def col(self) -> int:
        """
        Returns the column of the king on the board.board.

        Returns:
        - col (int): The column of the king on the board.board.
        """
        return self.position[1]

    @property
    def symbol(self) -> str:
        """
        Returns the symbol representing the piece on the board.board.

        Returns:
        - symbol (str): The symbol representing the piece on the board.board.
        """
        return self._symbol

    def __repr__(self) -> str:
        """
        Returns a string representation of the piece.

        Returns:
        - (str): A string representation of the piece.
        """
        return f" {self._symbol} "

    def legal_moves(self, board: object) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal moves for the piece on the given board.board.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board, with tuples as keys and Piece objects as values.

        Returns:
        - moves (set): A set of tuples representing the legal moves for the piece on the given board.board.
        """
        raise NotImplementedError("legal_moves method not implemented")

    def _is_position_capture(self, position: Tuple[int, int], board: Dict[Tuple[int, int], "Piece"]) -> bool:
        return position in board and board[position].color != self.color

    def _get_diagonal_moves(self, board: Dict[Tuple[int, int], "Piece"]) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal diagonal moves.

        Parameters:
        - board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal diagonal moves for the given board.board.
        """
        moves = set()
        row, col = self.position

        # Check for diagonal moves
        for row_offset, col_offset in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            move_pos = (row + row_offset, col + col_offset)
            while move_pos[0] in range(BOARD_SIZE) and move_pos[1] in range(BOARD_SIZE):
                if move_pos in board:
                    if board[move_pos].color != self.color:
                        moves.add(move_pos)
                    break
                else:
                    moves.add(move_pos)
                move_pos = (move_pos[0] + row_offset, move_pos[1] + col_offset)

        return moves

    def _get_horizontal_and_vertical_moves(self, board: Dict[Tuple[int, int], "Piece"]) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal horizontal and vertical moves.

        Parameters:
        - board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal horizontal and vertical moves for the given board.board.
        """
        moves = set()
        row, col = self.position

        # Check for horizontal and vertical moves
        for row_offset, col_offset in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            move_pos = (row + row_offset, col + col_offset)
            while move_pos[0] in range(BOARD_SIZE) and move_pos[1] in range(BOARD_SIZE):
                if move_pos in board:
                    if board[move_pos].color != self.color:
                        moves.add(move_pos)
                    break
                else:
                    moves.add(move_pos)
                move_pos = (move_pos[0] + row_offset, move_pos[1] + col_offset)

        return moves

    def _get_forward_moves(self, board: Dict[Tuple[int, int], "Piece"]) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal forward moves for the pawn.

        Parameters:
        - board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal forward moves.
        """
        moves = set()
        row, col = self.position
        direction = 1 if self.color == "white" else -1

        # Check for forward move
        if (row + direction, col) not in board:
            moves.add((row + direction, col))

            # Check for double move
            if row == 1 and direction == 1 or row == BOARD_SIZE - 2 and direction == -1:
                if (row + 2 * direction, col) not in board:
                    moves.add((row + 2 * direction, col))

        return moves


class Pawn(Piece):
    """
    Represents a pawn chess piece.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Initializes a new pawn chess piece.

        Parameters:
        - color (str): The color of the piece, either "white" or "black".
        - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        super().__init__(color, position)
        self._symbol = "♙" if color == "white" else "♟︎"

    @property
    def symbol(self) -> str:
        """
        Returns the symbol representing the pawn on the board.board.

        Returns:
        - symbol (str): The symbol representing the pawn on the board.board.
        """
        return self._symbol

    def _get_capture_moves(self, board: Dict[Tuple[int, int], "Piece"]) -> Set[Tuple[int, int]]:
        moves = set()
        row, col = self.position
        direction = 1 if self.color == "white" else -1

        # Check for capture moves
        for col_offset in (-1, 1):
            capture_pos = (row + direction, col + col_offset)
            if self._is_position_capture(capture_pos, board):
                moves.add(capture_pos)

        return moves
         

    def legal_moves(self, board: object) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal moves for the pawn.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal moves for the pawn on the given board.board.
        """
        moves = set()
        
        moves |= self._get_forward_moves(board.board)
        moves |= self._get_capture_moves(board.board)

        return moves


class Knight(Piece):
    """
    Represents a knight chess piece.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Initializes a new knight chess piece.

        Parameters:
        - color (str): The color of the piece, either "white" or "black".
        - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        super().__init__(color, position)
        self._symbol = "♘" if color == "white" else "♞"

    @property
    def symbol(self) -> str:
        """
        Returns the symbol representing the knight on the board.board.

        Returns:
        - symbol (str): The symbol representing the knight on the board.board.
        """
        return self._symbol

    def legal_moves(self, board: object) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal moves for the knight.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal moves for the knight on the given board.board.
        """
        moves = set()
        row, col = self.position

        for row_offset, col_offset in ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)):
            move_pos = (row + row_offset, col + col_offset)
            if move_pos[0] in range(BOARD_SIZE) and move_pos[1] in range(BOARD_SIZE):
                if move_pos in board.board and (move_piece := board.board[move_pos]).color == self.color:
                    continue
                else:
                    moves.add(move_pos)

        return moves


class Bishop(Piece):
    """
    Represents a bishop chess piece.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Initializes a new bishop chess piece.

        Parameters:
        - color (str): The color of the piece, either "white" or "black".
        - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        super().__init__(color, position)
        self._symbol = "♗" if color == "white" else "♝"

    @property
    def symbol(self) -> str:
        """
        Returns the symbol representing the bishop on the board.board.

        Returns:
        - symbol (str): The symbol representing the bishop on the board.board.
        """
        return self._symbol

    def legal_moves(self, board: object) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal moves for the bishop.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal moves for the bishop on the given board.board.
        """
        return self._get_diagonal_moves(board.board)


class Rook(Piece):
    """
    Represents a rook chess piece.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Initializes a new rook chess piece.

        Parameters:
        - color (str): The color of the piece, either "white" or "black".
        - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        super().__init__(color, position)
        self._symbol = "♖" if color == "white" else "♜"

    @property
    def symbol(self) -> str:
        """
        Returns the symbol representing the rook on the board.board.

        Returns:
        - symbol (str): The symbol representing the rook on the board.board.
        """
        return self._symbol

    def legal_moves(self, board: object) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal moves for the rook.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal moves for the rook on the given board.board.
        """        
        return self._get_horizontal_and_vertical_moves(board.board)


class Queen(Piece):
    """
    Represents a queen chess piece.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Initializes a new queen chess piece.

        Parameters:
        - color (str): The color of the piece, either "white" or "black".
        - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        super().__init__(color, position)
        self._symbol = "♕" if color == "white" else "♛"

    @property
    def symbol(self) -> str:
        """
        Returns the symbol representing the queen on the board.board.

        Returns:
        - symbol (str): The symbol representing the queen on the board.board.
        """
        return self._symbol

    def legal_moves(self, board: object) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal moves for the queen.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal moves for the queen on the given board.board.
        """
        moves = set()
        moves |= self._get_diagonal_moves(board.board)
        moves |= self._get_horizontal_and_vertical_moves(board.board)
        return moves


class King(Piece):
    """
    Represents a king chess piece.
    """

    def __init__(self, color: str, position: Tuple[int, int]):
        """
        Initializes a new king chess piece.

        Parameters:
        - color (str): The color of the piece, either "white" or "black".
        - position (tuple): The position of the piece on the board.board, represented as a tuple of integers (row, column).
        """
        super().__init__(color, position)
        self._symbol = "♔" if color == "white" else "♚"

    @property
    def symbol(self) -> str:
        """
        Returns the symbol representing the king on the board.board.

        Returns:
        - symbol (str): The symbol representing the king on the board.board.
        """
        return self._symbol

    def legal_moves(self, board: object) -> Set[Tuple[int, int]]:
        """
        Returns a set of legal moves for the king.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - moves (set): A set of tuples representing the legal moves for the king on the given board.board.
        """
        moves = set()
        row, col = self.position

        # Check for adjacent moves
        for row_offset, col_offset in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            move_pos = (row + row_offset, col + col_offset)
            if move_pos in board.board and (move_piece := board.board[move_pos]).color != self.color:
                moves.add(move_pos)

        return moves

    def is_in_check(self, board: object) -> bool:
        """
        Returns True if the king is in check on the given board.board, False otherwise.

        Parameters:
        - board.board (ChessBoard): A ChessBoard object representing the current state of the chess board.board.

        Returns:
        - is_check (bool): True if the king is in check on the given board.board, False otherwise.
        """
        for piece in board.board.get_all_pieces(self.color):
            if piece.color != self.color and self.position in piece.legal_moves(board.board):
                return True
        return False

    def is_in_checkmate(self, board: object) -> bool:
        """
        Returns True if the king is in checkmate on the given board.board, False otherwise.

        Parameters:
        - board.board (dict): A dictionary representing the current state of the chess board.board.

        Returns:
        - is_checkmate (bool): True if the king is in checkmate on the given board.board, False otherwise.
        """
        if not self.is_in_check(board.board):
            return False
        for move in self.legal_moves(board.board):
            new_board = dict(board.board)
            new_board[self.position], new_board[move] = None, self
            if not self.is_in_check(new_board):
                return False
        return True
