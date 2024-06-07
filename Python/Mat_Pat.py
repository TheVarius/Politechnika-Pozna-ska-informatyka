def check_game_status(board, king_position):
    king_i, king_j = king_position

    can_move = any(0 <= king_i + x <= 7 and 0 <= king_j + y <= 7 and board[king_i + x][king_j + y] == 0 for x in range(-1, 2) for y in range(-1, 2) if (x, y) != (0, 0))

    if can_move:
        print("game goes on")
    elif board[king_i][king_j] == 1:
        print("mat")
    else:
        print("pat")

M_symb=[[str(x) for x in input()] for y in range(8)]
M_numbers = [[0] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if M_symb[i][j] == "w":
            for k in range(8):
                M_numbers[i][k] = 1
                M_numbers[k][j] = 1
            M_numbers[i][j] = 0
        if M_symb[i][j] == "k":
            king_position = (i, j)
check_game_status(M_numbers, king_position)
