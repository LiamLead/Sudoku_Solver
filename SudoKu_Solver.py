the_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


# basic function to show the board nicely
def show_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:   # and so that the lines don't start from above and left
            print("---------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# loop through the board to find empty positions(0)
def find_empty_num(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j      # row, column instead of column row as usual

    return None         # if there are no more squares that are blank (= 0) then we are done


# find your position in the board
def valid_number(board, number, position):

    # check which row we are in
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check the column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check the box
    box_x = position[1] // 3    # column
    box_y = position[0] // 3    # row

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    # the number is good to go
    return True


def solve_board(board):
    # print(the_board)
    find = find_empty_num(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):      # to go through each number to see which one fits in
        if valid_number(board, i, (row, col)):      # check if the number is valid
            board[row][col] = i         # add the valid number to the row/col

            if solve_board(board):  # solve_board inside itself to keep calling it on the new board
                return True
            board[row][col] = 0

    return False


show_board(the_board)
solve_board(the_board)
print("$" * 20)
show_board(the_board)
