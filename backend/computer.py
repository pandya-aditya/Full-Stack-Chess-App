from engine import gameState

class ChessAI:
    def __init__(self):

        self.WHITE_PIECES = {'wR', 'wN', 'wB', 'wQ', 'wK', 'wP'}
        self.BLACK_PIECES = {'bR', 'bN', 'bB', 'bQ', 'bK', 'bP'}
        self.game = gameState()


    def evaluate_board(self, board):
        """Evaluate the board for Black pieces."""
        value = 0
        piece_values = {
            'P': 1,
            'N': 3,
            'B': 3,
            'R': 5,
            'Q': 9,
            'K': 0  
        }
        
        for row in board:
            for piece in row:
                if piece in self.WHITE_PIECES:
                    value -= piece_values[piece[1]] 
                elif piece in self.BLACK_PIECES:
                    value += piece_values[piece[1]] 
        return value
    
    def generate_moves(self, board, player):
        """Generate all possible moves for the given player."""
        moves = []
        for r in range(8):
            for c in range(8):
                piece = board[r][c]
                if piece in player:
                    coords = {'x': c, 'y': r}
                    piece_moves = self.game.get_moves(coords, board)  
                    for move in piece_moves:
                        moves.append((piece, (r, c), (move[0], move[1])))

        return moves
    
    def minimax(self, board, depth, maximizing_player):
        """Minimax algorithm."""
        if depth == 0:
            return self.evaluate_board(board)
        
        player = self.BLACK_PIECES if maximizing_player else self.WHITE_PIECES
        best_value = float('-inf') if maximizing_player else float('inf')
    
        for move in self.generate_moves(board, player):
            
            new_board = self.make_move(board, move)
            value = self.minimax(new_board, depth - 1, not maximizing_player)
            
            if maximizing_player:
                best_value = max(best_value, value)
            else:
                best_value = min(best_value, value)
        
        return best_value
    
    def make_move(self, board, move_to_make):
        """Return a new board with the move applied."""
        new_board = [row[:] for row in board]
        new_board[move_to_make[1][0]][move_to_make[1][1]] = '--' 
        new_board[move_to_make[2][0]][move_to_make[2][1]] = move_to_make[0]
        return new_board
    
    def best_move(self, board, depth):
        """Determine the best move for Black pieces."""
        best_value = float('-inf')
        move_to_make = None
        
        for move in self.generate_moves(board, self.BLACK_PIECES):
            new_board = self.make_move(board, move)
            move_value = self.minimax(new_board, depth - 1, False)
            
            if move_value > best_value:
                best_value = move_value
                move_to_make = move
        print(self.make_move(board, move_to_make))

        return self.make_move(board, move_to_make)
