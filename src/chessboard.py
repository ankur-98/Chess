from typing import List, Tuple 
from pieces import *
from config import BOARD_SIZE


class PieceFactory: 
    """ A factory class for creating new pieces. """

    @staticmethod
    def create_piece(piece_type: str, color: str, position: Tuple[int, int]) -> Piece:
        """
        Creates a new piece of the given type, color, and position.

        Parameters:
        - piece_type (str): The type of piece to create ("king", "queen", "rook", "bishop", "knight", or "pawn").
        - color (str): The color of the piece ("white" or "black").
        - position (tuple): The position of the piece on the board, represented as a tuple of integers (row, column).

        Returns:
        - piece (Piece): The newly created piece.
        """
        if piece_type == "king":
            return King(color, position)
        elif piece_type == "queen":
            return Queen(color, position)
        elif piece_type == "rook":
            return Rook(color, position)
        elif piece_type == "bishop":
            return Bishop(color, position)
        elif piece_type == "knight":
            return Knight(color, position)
        elif piece_type == "pawn":
            return Pawn(color, position)
        else:
            raise ValueError(f"Invalid piece type: {piece_type}")

class ChessBoard: 
    """ A class representing a chess board. """
    BOARD_SIZE = BOARD_SIZE

    def __init__(self):
        """
        Initializes a new chess board with all pieces in their starting positions.
        """
        self.board: Dict[Tuple[int, int], Piece] = {}
        self._place_starting_pieces()
        self.losses = []

    def _place_starting_pieces(self):
        """
        Places all pieces in their starting positions on the board.
        """
        # Place pawns
        for col in range(self.BOARD_SIZE):
            self.add_piece(PieceFactory.create_piece("pawn", "white", (1, col)), (1, col))
            self.add_piece(PieceFactory.create_piece("pawn", "black", (self.BOARD_SIZE - 2, col)), (self.BOARD_SIZE - 2, col))

        # Place other pieces
        for row, color in [(0, "white"), (self.BOARD_SIZE - 1, "black")]:
            self.add_piece(PieceFactory.create_piece("rook", color, (row, 0)), (row, 0))
            self.add_piece(PieceFactory.create_piece("knight", color, (row, 1)), (row, 1))
            self.add_piece(PieceFactory.create_piece("bishop", color, (row, 2)), (row, 2))
            self.add_piece(PieceFactory.create_piece("queen", color, (row, 3)), (row, 3))
            self.add_piece(PieceFactory.create_piece("king", color, (row, 4)), (row, 4))
            self.add_piece(PieceFactory.create_piece("bishop", color, (row, 5)), (row, 5))
            self.add_piece(PieceFactory.create_piece("knight", color, (row, 6)), (row, 6))
            self.add_piece(PieceFactory.create_piece("rook", color, (row, 7)), (row, 7))

    def add_piece(self, piece: Piece, position: Tuple[int, int]) -> None:
        """
        Adds a piece to the board at the given position.

        Parameters:
        - piece (Piece): The piece to add to the board.
        - position (tuple): The position to add the piece at, represented as a tuple of integers (row, column).
        """
        if position in self.board and self.board[position].color != piece.color:
            self.losses.append(self.board[position])
        self.board[position] = piece
        piece.position = position

    def remove_piece(self, position: Tuple[int, int]) -> None:
        """
        Removes the piece at the given position from the board.

        Parameters:
        - position (tuple): The position of the piece to remove, represented as a tuple of integers (row, column).
        """   
        del self.board[position]

    def move_piece(self, start: Tuple[int, int], end: Tuple[int, int]) -> None:
        """
        Moves the piece at the start position to the end position.

        Parameters:
        - start (tuple): The starting position of the piece to move, represented as a tuple of integers (row, column).
        - end (tuple): The ending position of the piece to move, represented as a tuple of integers (row, column).
        """
        piece = self.board[start]
        self.remove_piece(start)
        self.add_piece(piece, end)

    def get_piece_at(self, position: Tuple[int, int]) -> Piece:
        """
        Returns the piece at the given position.

        Parameters:
        - position (tuple): The position of the piece to get, represented as a tuple of integers (row, column).

        Returns:
        - The piece at the given position.
        """
        return self.board[position]

    def get_piece(self, piece_name: str, color: str) -> King:
        """
        Returns the piece of the given color and name on the board.

        Parameters:
        - piece_name (str): The name of the piece to get ("king", "queen", "rook", "bishop", "knight", or "pawn").
        - color (str): The color of the king to get ("white" or "black").

        Returns:
        - The piece of the given color on the board, or None if it is not on the board.
        """
        for _, piece in self.board.items():
            if piece.__name__ == piece_name.capitalize() and piece.color == color:
                return piece
        return None

    def is_position_empty(self, position: Tuple[int, int]) -> bool:
        """
        Returns True if the given position is empty, False otherwise.

        Parameters:
        - position (tuple): The position to check, represented as a tuple of integers (row, column).

        Returns:
        - True if the given position is empty, False otherwise.
        """
        return position not in self.board

    def is_position_valid(self, position: Tuple[int, int]) -> bool:
        """
        Returns True if the given position is a valid position on the board, False otherwise.

        Parameters:
        - position (tuple): The position to check, represented as a tuple of integers (row, column).

        Returns:
        - True if the given position is a valid position on the board, False otherwise.
        """
        row, col = position
        return 0 <= row < self.BOARD_SIZE and 0 <= col < self.BOARD_SIZE

    def get_all_pieces(self, color: str) -> List[Piece]:
        """
        Returns a list of all pieces of the given color on the board.

        Parameters:
        - color (str): The color of the pieces to get.

        Returns:
        - A list of all pieces of the given color on the board.
        """
        return [piece for piece in self.board.values() if piece.color == color]

    def __str__(self) -> str:
        """
        Returns a string representation of the chess board.

        Returns:
        - A string representation of the chess board.
        """
        rows = []
        rows.append("   " + "   ".join([str(i) for i in range(0, self.BOARD_SIZE)]))
        for row in range(self.BOARD_SIZE):
            row_str = ""
            for col in range(self.BOARD_SIZE):
                piece = self.board.get((row, col))
                if piece:
                    row_str += f"{piece} "
                else:
                    row_str += " .  "
            rows.append(f"{row} {row_str} {row}\n")
        rows.append("   " + "   ".join([str(i) for i in range(0, self.BOARD_SIZE)]))

        rows.append(f"\nlosses: {self.losses}\n")
        
        return "\n".join(rows)

    def copy(self) -> "ChessBoard":
        """
        Returns a copy of the chess board.

        Returns:
        - A copy of the chess board.
        """
        new_board = ChessBoard()
        for position, piece in self.board.items():
            new_board.add_piece(piece.copy(), position)
        return new_board

    def is_checkmate(self, color):
        """
        Returns True if the given color king is in checkmate on the board, False otherwise.

        Parameters:
        - color (str): The color of the king to check ("white" or "black").

        Returns:
        - is_checkmate (bool): True if the given color is in checkmate, False otherwise.
        """
        if not self.is_check(color):
            return False
        king = self.get_piece("king", color)
        for move in king.legal_moves(self.board):
            temp_board = self.copy()
            temp_board.move_piece(king.position, move)
            if not temp_board.is_check(color):
                return False
        return True

    def is_check(self, color):
        """
        Returns True if the given color king is in check on the board, False otherwise.

        Parameters:
        - color (str): The color of the king to check ("white" or "black").

        Returns:
        - is_checkmate (bool): True if the given color is in checkmate, False otherwise.
        """
        king = self.get_piece("king", color)
        for piece in self.get_all_pieces(color):
            if piece.color != color and king.position in piece.legal_moves(self.board):
                return True
        return False
