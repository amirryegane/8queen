def safe(board, row, col):
    
    for i in range(row):
        
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return 0
    return 1

def solver(board, row , solo):

    
    if row == len(board):  
        solo.append(board[:])
        
        return
    
    for col in range(len(board)):
        if safe(board, row, col):
            board[row] = col  
            solver(board, row + 1, solo)
            if solver(board, row + 1 ,  solo):  
                return True
            board[row] = -1  
    return 0

def pboard(board):
    n = len(board)
    for i in range(n):
        row = ['.' for _ in range(n)]
        row[board[i]] = 'Q'
        print(" ".join(row))
    print()

def queens():
    n = 8  
    board = [-1] * n  
    solo = []
    solver(board , 0 , solo)
    print(f"Found {len(solo)} solutions:")
    for solution in solo:
        pboard(solution)

print("oh my god")
queens()
