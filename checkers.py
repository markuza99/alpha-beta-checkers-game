from copy import deepcopy

_matrix = []
best_move = ()
for i in range(9):
     _matrix.append( [' '] * 9 )


def _darkQuad(row, col):
    return row % 2 != col % 2


for row in range(0, 9):
    for col in range(0, 9):
        if _darkQuad(row, col) == True and row <=3 and row >= 1 and col > 0 :
            _matrix[row][col] = 'a'
        elif row == 0 and col <= 9:
            _matrix[row][col] = col
        elif _darkQuad(row, col) == True and row >= 6 and col > 0:
            _matrix[row][col] = 'b'
        elif col == 0 and row <=9:
            _matrix[row][col] = row
        else:
            _matrix[row][col] = '-'


def transform():
    for row in range(0, 9):
        for col in range(0, 9):
            if "b" in str(_matrix[1][col]):
                _matrix[1][col] = "B"


def _printDebugBoard():
    for row in range(0, 9):
        for col in range(0, 9):
            print(_matrix[row][col], end=" ")
        print()




def avail_moves(player):
    moves = []

    for row in range(9):
        for col in range(9):
            if _matrix[row][col] != "-" and player == "white":
                if can_jump_white([row, col], [row + 1, col + 1], [row + 2, col + 2],_matrix) == True:
                    moves.append([row, col, row + 2, col + 2])
                if can_jump_white([row, col], [row - 1, col + 1], [row - 2, col + 2], _matrix) == True:
                    moves.append([row, col, row - 2, col + 2])
                if can_jump_white([row, col], [row + 1, col - 1], [row + 2, col - 2], _matrix) == True:
                    moves.append([row, col, row + 2, col - 2])
                if can_jump_white([row, col], [row - 1, col - 1], [row - 2, col - 2], _matrix) == True:
                    moves.append([row, col, row - 2, col - 2])
                if can_move_white([row, col], [row + 1, col + 1], _matrix) == True:
                    moves.append([row, col, row + 1, col + 1])
                if can_move_white([row, col], [row - 1, col + 1], _matrix) == True:
                    moves.append([row, col, row - 1, col + 1])
                if can_move_white([row, col], [row + 1, col - 1], _matrix) == True:
                    moves.append([row, col, row + 1, col - 1])
                if can_move_white([row, col], [row - 1, col - 1], _matrix) == True:
                    moves.append([row, col, row - 1, col - 1])
            if _matrix[row][col] != "-" and player == "black":
                if can_jump_black([row, col], [row + 1, col + 1], [row + 2, col + 2], _matrix) == True:
                    moves.append([row, col, row + 2, col + 2])
                if can_jump_black([row, col], [row - 1, col + 1], [row - 2, col + 2], _matrix) == True:
                    moves.append([row, col, row - 2, col + 2])
                if can_jump_black([row, col], [row + 1, col - 1], [row + 2, col - 2], _matrix) == True:
                    moves.append([row, col, row + 2, col - 2])
                if can_jump_black([row, col], [row - 1, col - 1], [row - 2, col - 2], _matrix) == True:
                    moves.append([row, col, row - 2, col - 2])
                if can_move_black([row, col], [row + 1, col + 1], _matrix) == True:
                    moves.append([row, col, row + 1, col + 1])
                if can_move_black([row, col], [row - 1, col + 1], _matrix) == True:
                    moves.append([row, col, row - 1, col + 1])
                if can_move_black([row, col], [row + 1, col - 1], _matrix) == True:
                    moves.append([row, col, row + 1, col - 1])
                if can_move_black([row, col], [row - 1, col - 1], _matrix) == True:
                    moves.append([row, col, row - 1, col - 1])

    return moves

def avail_moves_obavezno(player):
    moves = []

    for row in range(9):
        for col in range(9):
            if _matrix[row][col] != "-" and player == "white":

                if can_jump_white([row, col], [row + 1, col + 1], [row + 2, col + 2], _matrix) == True:
                    moves.append([row, col, row + 2, col + 2])
                if can_jump_white([row, col], [row - 1, col + 1], [row - 2, col + 2], _matrix) == True:
                    moves.append([row, col, row - 2, col + 2])
                if can_jump_white([row, col], [row + 1, col - 1], [row + 2, col - 2], _matrix) == True:
                    moves.append([row, col, row + 2, col - 2])
                if can_jump_white([row, col], [row - 1, col - 1], [row - 2, col - 2], _matrix) == True:
                    moves.append([row, col, row - 2, col - 2])


    if len(moves) == 0:
        for row in range(9):
            for col in range(9):
                if _matrix[row][col] != "-" and player == "white":
                    if can_move_white([row, col], [row + 1, col + 1], _matrix) == True:
                        moves.append([row, col, row + 1, col + 1])
                    if can_move_white([row, col], [row - 1, col + 1], _matrix) == True:
                        moves.append([row, col, row - 1, col + 1])
                    if can_move_white([row, col], [row + 1, col - 1], _matrix) == True:
                        moves.append([row, col, row + 1, col - 1])
                    if can_move_white([row, col], [row - 1, col - 1], _matrix) == True:
                        moves.append([row, col, row - 1, col - 1])
    for row in range(9):
        for col in range(9):
            if _matrix[row][col] != "-" and player == "black":
                if can_jump_black([row, col], [row + 1, col + 1], [row + 2, col + 2], _matrix) == True:
                    moves.append([row, col, row + 2, col + 2])
                if can_jump_black([row, col], [row - 1, col + 1], [row - 2, col + 2], _matrix) == True:
                    moves.append([row, col, row - 2, col + 2])
                if can_jump_black([row, col], [row + 1, col - 1], [row + 2, col - 2], _matrix) == True:
                    moves.append([row, col, row + 2, col - 2])
                if can_jump_black([row, col], [row - 1, col - 1], [row - 2, col - 2], _matrix) == True:
                    moves.append([row, col, row - 2, col - 2])
    if len(moves) == 0:
        for row in range(9):
            for col in range(9):
                if can_move_black([row, col], [row + 1, col + 1], _matrix) == True:
                    moves.append([row, col, row + 1, col + 1])
                if can_move_black([row, col], [row - 1, col + 1], _matrix) == True:
                    moves.append([row, col, row - 1, col + 1])
                if can_move_black([row, col], [row + 1, col - 1], _matrix) == True:
                    moves.append([row, col, row + 1, col - 1])
                if can_move_black([row, col], [row - 1, col - 1], _matrix) == True:
                    moves.append([row, col, row - 1, col - 1])


    return moves 



def can_jump_white(a, via, b, board):
    if b[0] < 1 or b[0] > 8 or b[1] < 1 or b[1] > 8:
        return False
    if board[b[0]][b[1]] != "-":
        return False

    if board[via[0]][via[1]] == "-":
        return False

    if board[a[0]][a[1]] == "b":
        if b[0] > a[0]:
            return False
        if board[via[0]][via[1]] != "A" and board[via[0]][via[1]] != "a":
            return False

        return True

    if board[a[0]][a[1]] == "B":
        if board[via[0]][via[1]] != "A" and board[via[0]][via[1]] != "a":
            return False
        return True


def can_move_white(a, b, board):
    if b[0] < 1 or b[0] > 8 or b[1] < 1 or b[1] > 8:
        return False

    if board[b[0]][b[1]] != "-":
            return False
    if board[a[0]][a[1]] == "b":
        if b[0] > a[0]:
            return False
        return True
    if board[a[0]][a[1]] == "B":
        return True


def can_move_black(a, b, board):
    if b[0] < 1 or b[0] > 8 or b[1] < 1 or b[1] > 8:
        return False

    if board[b[0]][b[1]] != "-":
            return False
    if board[a[0]][a[1]] == "a":
        if b[0] < a[0]:
            return False
        return True
    if board[a[0]][a[1]] == "A":
        return True


def can_jump_black(a, via, b, board):

    if b[0] < 1 or b[0] > 8 or b[1] < 1 or b[1] > 8:
        return False

    if board[b[0]][b[1]] != "-": return False

    if board[via[0]][via[1]] == "-": return False

    if board[a[0]][a[1]] == "a":
        if b[0] < a[0]:
            return False
        if board[via[0]][via[1]] != "b" and board[via[0]][via[1]] != "B":
            return False

        return True
    if board[a[0]][a[1]] == "A":
        if board[via[0]][via[1]] != "b" and board[via[0]][via[1]] != "B":
            return False
        return True


def make_move(a, b, board):
    board[b[0]][b[1]] = board[a[0]][a[1]]
    board[a[0]][a[1]] = "-"


    if b[0] == 8 and board[b[0]][b[1]] == 'a':
        board[b[0]][b[1]] = "A"
    if b[0] == 1 and board[b[0]][b[1]] == 'b':
        board[b[0]][b[1]] = "B"

    if (a[0] - b[0]) % 2 == 0:
        board[(a[0] + b[0]) // 2][(a[1] + b[1]) // 2] = "-"

def evaluate(player):
    def simple_score(player):
        black = 0
        white = 0
        for r in range(9):
            for c in range(9):
                if _matrix[r][c] == "b":
                    white += 100 + ((9-r)*(9-r))
                if _matrix[r][c] == "B":
                    white += 175 + ((9-r)*(9-r))
                if _matrix[r][c] == "a":
                    black += 100 + r*r
                if _matrix[r][c] == "A":
                    black += 175 +r*r
        if player != 'black':
            return white - black
        else:
            return black - white



    def edge(player):
        black, white = 0, 0
        for m in range(9):
            for n in range(9):
                if _matrix[m][1] == "a":
                    black += -25
                if _matrix[m][1] == "b":
                    white += -25
                if _matrix[m][8] == "a":
                    black += -25
                if _matrix[m][1] == "b":
                    white += -25
        if player != 'black':
            return white - black
        else:
            return black - white


    return simple_score(player) + edge(player)

def end_game():
    black = 0
    white = 0
    for r in range(9):
        for c in range(9):
            if _matrix[r][c] == "a":
                black += 1
            if _matrix[r][c] == "A":
                black += 1
            if _matrix[r][c] == "b":
                white += 1
            if _matrix[r][c] == "B":
                white += 1
    return black,white

def kretanjebezgutanja(player):
    print(avail_moves("white"))
    _printDebugBoard()
    movz = []
    pc = []
    p = avail_moves(player)
    x = eval(input("Unesi red figure:"))
    y = eval(input("Unesi kolonu figure:"))
    x1 = eval(input("Unesi red na koji se zelis pomeriti:"))
    y1 = eval(input("Unesi kolonu na koju se zelis pomeriti:"))
    izbor = [x, y, x1, y1]
    for pokret in p:
        pc.append(pokret)

    while izbor not in pc:
        print("Uneli ste pogresan unos")
        x = eval(input("Unesi red figure:"))
        y = eval(input("Unesi kolonu figure:"))
        x1 = eval(input("Unesi red na koji se zelis pomeriti:"))
        y1 = eval(input("Unesi kolonu na koju se zelis pomeriti:"))
        izbor = [x, y, x1, y1]
    _matrix[x1][y1] = _matrix[x][y]
    _matrix[x][y] = "-"
    if (x - x1) % 2 == 0:
        _matrix[(x + x1) // 2][(y + y1) // 2] = "-"
    transform()


def kretanjebezgutanjaobavezno(player):
    print(avail_moves_obavezno("white"))
    _printDebugBoard()
    movz = []
    pc = []
    p = avail_moves_obavezno(player)
    x = eval(input("Unesi red figure:"))
    y = eval(input("Unesi kolonu figure:"))
    x1 = eval(input("Unesi red na koji se zelis pomeriti:"))
    y1 = eval(input("Unesi kolonu na koju se zelis pomeriti:"))
    izbor = [x, y, x1, y1]
    for pokret in p:
        pc.append(pokret)

    while izbor not in pc:
        print("Uneli ste pogresan unos")
        x = eval(input("Unesi red figure:"))
        y = eval(input("Unesi kolonu figure:"))
        x1 = eval(input("Unesi red na koji se zelis pomeriti:"))
        y1 = eval(input("Unesi kolonu na koju se zelis pomeriti:"))
        izbor = [x, y, x1, y1]
    _matrix[x1][y1] = _matrix[x][y]
    _matrix[x][y] = "-"
    if (x - x1) % 2 == 0:
        _matrix[(x + x1) // 2][(y + y1) // 2] = "-"
    transform()


def alpha_beta(player, board, ply, alpha, beta):
	global best_move

	end = end_game()


	if ply >= 7 or end[0] == 0 or end[1] == 0:

		score = evaluate(player)
		return score


	moves = avail_moves(player)


	if player == "black":

		for i in range(len(moves)):

			new_board = deepcopy(board)
			make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)




			score = alpha_beta("white", new_board, ply+1, alpha, beta)


			if score > alpha:
				if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3])
				alpha = score

			if alpha >= beta:

				return alpha


		return alpha

	else:


		for i in range(len(moves)):
			new_board = deepcopy(board)
			make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)


			score = alpha_beta("black", new_board, ply+1, alpha, beta)
			if score < beta: beta = score
			if alpha >= beta: return beta
		return beta







def alpha_beta_obavezno(player, board, ply, alpha, beta):
	global best_move

	end = end_game()


	if ply >= 7 or end[0] == 0 or end[1] == 0:

		score = evaluate(player)
		return score


	moves = avail_moves_obavezno(player)


	if player == "black":

		for i in range(len(moves)):

			new_board = deepcopy(board)
			make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)




			score = alpha_beta("white", new_board, ply+1, alpha, beta)


			if score > alpha:
				if ply == 0: best_move = (moves[i][0], moves[i][1]), (moves[i][2], moves[i][3])
				alpha = score

			if alpha >= beta:

				return alpha


		return alpha

	else:


		for i in range(len(moves)):
			new_board = deepcopy(board)
			make_move((moves[i][0], moves[i][1]), (moves[i][2], moves[i][3]), new_board)


			score = alpha_beta("black", new_board, ply+1, alpha, beta)
			if score < beta: beta = score
			if alpha >= beta: return beta
		return beta

def cpu_play(player):
    global _matrix
    alpha = alpha_beta("black", _matrix, 0,-10000,10000)
    make_move(best_move[0], best_move[1], _matrix)

def cpu_play_obavezno(player):
    global _matrix
    alpha = alpha_beta_obavezno("black", _matrix, 0,-10000,10000)
    make_move(best_move[0], best_move[1], _matrix)

if __name__ == '__main__':

    print("***OPCIJE***")
    print("1. OBAVEZNO GUTANJE.")
    print("2. NEOBAVEZNO GUTANJE.")
    print("************")
    x = input("UNESITE REDNI BROJ OPCIJE:")
    while x != "1." and  x != "2.":
        x = input("POGRESAN UNOS PROBAJTE PONOVO:")
    if x == "1.":
        while True:
            kretanjebezgutanjaobavezno("white")
            _printDebugBoard()
            cpu_play_obavezno("black")
            print(best_move)
            black = 0
            white = 0
            for r in range(9):
                for c in range(9):
                    if _matrix[r][c] == "a":
                        black += 1
                    if _matrix[r][c] == "A":
                        black += 1
                    if _matrix[r][c] == "b":
                        white += 1
                    if _matrix[r][c] == "B":
                        white += 1
            if black == 1 and white > 2:
                print("Pobednik je beli!")
                _printDebugBoard()
                break
            if white == 1 and black > 2:
                print("Pobednik je crni!")
                _printDebugBoard()
                break
            if white == 0:
                print("Pobednik je crni!")
                _printDebugBoard()
                break
            if black == 0:
                print("Pobednik je beli!")
                _printDebugBoard()
                break
    if x == "2.":
        while True:
            kretanjebezgutanja("white")
            _printDebugBoard()
            cpu_play("black")
            print(best_move)
            black = 0
            white = 0
            for r in range(9):
                for c in range(9):
                    if _matrix[r][c] == "a":
                        black += 1
                    if _matrix[r][c] == "A":
                        black += 1
                    if _matrix[r][c] == "b":
                        white += 1
                    if _matrix[r][c] == "B":
                        white += 1
            if black == 1 and white > 2:
                print("Pobednik je beli!")
                _printDebugBoard()
                break
            if white == 1 and black > 2:
                print("Pobednik je crni!")
                _printDebugBoard()
                break
            if white == 0:
                print("Pobednik je crni!")
                _printDebugBoard()
                break
            if black == 0:
                print("Pobednik je beli!")
                _printDebugBoard()
                break