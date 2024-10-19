class gameState:
    def __init__(self):
        pass

    def get_moves(self, selected, board):
        chosen = board[selected['y']][selected['x']]
        moves = []

        if chosen[1] == 'P':
            moves = self.pawn_moves(selected, board)
        elif chosen[1] == 'R':
            moves = self.rook_moves(selected, board)
        elif chosen[1] == 'B':
            moves = self.bishop_moves(selected, board)
        elif chosen[1] == 'N':
            moves = self.knight_moves(selected, board)
        elif chosen[1] == 'K':
            moves = self.king_moves(selected, board)
        elif chosen[1] == 'Q':
            moves = self.queen_moves(selected, board)
        
        return moves

    def pawn_moves(self, selected, board):
        moves = []
        colour = board[selected['y']][selected['x']][0]
        structure = {'w': [-1, 'b'], 'b': [1, 'w']}

        if board[selected['y'] + structure[colour][0]][selected['x']] == "--":
            moves.append([selected['y'] + structure[colour][0], selected['x']])

        if selected['y'] == 6 and colour == 'w' and board[selected['y'] - 2][selected['x']] == "--":
            moves.append([selected['y'] - 2, selected['x']])
        elif selected['y'] == 1 and colour == 'b' and board[selected['y'] + 2][selected['x']] == "--":
            moves.append([selected['y'] + 2, selected['x']])

        if 0 <= selected['x'] - 1 and board[selected['y'] + structure[colour][0]][selected['x'] - 1][0] == structure[colour][1]:
            moves.append([selected['y'] + structure[colour][0], selected['x'] - 1])
        if selected['x'] + 1 < 8 and board[selected['y'] + structure[colour][0]][selected['x'] + 1][0] == structure[colour][1]:
            moves.append([selected['y'] + structure[colour][0], selected['x'] + 1])

        return moves

    def rook_moves(self, selected, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        colour = board[selected['y']][selected['x']][0]

        for direction in directions:
            for i in range(1, 8):
                end_row = selected['y'] + direction[0] * i
                end_col = selected['x'] + direction[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = board[end_row][end_col]
                    if end_piece == "--":  
                        moves.append([end_row, end_col])
                    elif end_piece[0] != colour:  
                        moves.append([end_row, end_col])
                        break
                    else:  
                        break
                else:
                    break
        return moves


    def knight_moves(self, selected, board):
        moves = []
        colour = board[selected['y']][selected['x']][0]
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for direction in directions:
            end_row = selected['y'] + direction[0]
            end_col = selected['x'] + direction[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = board[end_row][end_col]
                if end_piece == "--" or end_piece[0] != colour:
                    moves.append([end_row, end_col])

        return moves

    def bishop_moves(self, selected, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  
        colour = board[selected['y']][selected['x']][0]

        for direction in directions:
            for i in range(1, 8):
                end_row = selected['y'] + direction[0] * i
                end_col = selected['x'] + direction[1] * i
                if 0 <= end_row < 8 and 0 <= end_col < 8:
                    end_piece = board[end_row][end_col]
                    if end_piece == "--": 
                        moves.append([end_row, end_col])
                    elif end_piece[0] != colour: 
                        moves.append([end_row, end_col])
                        break
                    else: 
                        break
                else:
                    break
        return moves

    def queen_moves(self, selected, board):
        return self.rook_moves(selected, board) + self.bishop_moves(selected, board)

    def king_moves(self, selected, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        colour = board[selected['y']][selected['x']][0]

        for direction in directions:
            end_row = selected['y'] + direction[0]
            end_col = selected['x'] + direction[1]
            if 0 <= end_row < 8 and 0 <= end_col < 8:
                end_piece = board[end_row][end_col]
                if end_piece == "--" or end_piece[0] != colour:
                    moves.append([end_row, end_col])

        return moves

