def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def determine_winner(board):
    if check_winner(board, "X"):
        return "X"
    
    if check_winner(board, "O"):
        return "O"
    
    if check_winner(board, "+"):
        return "+"

    return "DRAW"

t = int(input())

for _ in range(t):
    board = [list(input()) for _ in range(3)] 
    result = determine_winner(board)
    print(result)