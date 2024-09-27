def available_moves(solution):
    free_moves = []
    for r in range(9):
        for c in range(9):
            if solution[r][c] == ' ':
                free_moves.append((r,c))
    
    return free_moves

def num_area(puzzle):
    unique_areas = []
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] not in unique_areas:
                unique_areas.append(puzzle[r][c])
    
    num_area = len(unique_areas)
    return num_area

# marks a board with all the x's and place a new star in row,col, then return the new board
def mark_board(solution, puzzle, row, col):

    new_solution = [row[:] for row in solution]
    new_solution[row][col] = '*'

    for i in range(9*row + col):
        if new_solution[i // 9][i % 9] == ' ':
            new_solution[i // 9][i % 9] = 'x'

    for i in range(max(0, row-1), min(9, row+2)):
        for j in range(max(0, col-1), min(9, col+2)):
            if new_solution[i][j] == '*':
                continue
            new_solution[i][j] = 'x'

    col_vals = [new_solution[i][col] for i in range(9)]
    if col_vals.count('*') == 2:
        for i in range(9):
            if new_solution[i][col] == '*':
                continue
            new_solution[i][col] = 'x'

    if new_solution[row].count('*') == 2:
        for i in range(9):
            if new_solution[row][i] == '*':
                continue
            new_solution[row][i] = 'x'
    
    area_vals = []
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == puzzle[row][col]:
                area_vals.append(new_solution[i][j])

    if area_vals.count('*') == 2:
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == puzzle[row][col]:
                    if new_solution[i][j] == '*':
                        continue
                    new_solution[i][j] = 'x'

    return new_solution

def is_valid(solution, puzzle, row, col):
    
    test_solution = mark_board(solution, puzzle, row, col)

    for i in range(9):
        col_vals =  [test_solution[j][i] for j in range(9)] 
        if col_vals.count(' ') == 0:
            if not col_vals.count('*') == 2:
                return False

    for i in range(9):
        row_vals = test_solution[i]
        if row_vals.count(' ') == 0:
            if not row_vals.count('*') == 2:
                return False

    area_count = num_area(puzzle)
    
    for area in range(area_count):
        area_vals = []
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == area:
                    area_vals.append(test_solution[i][j])

        if area_vals.count(' ') == 0:
            if not area_vals.count('*') == 2:
                return False

    return True

def print_nice(solution):
    for r in range(9): 
        print(solution[r])
    print('\n')

recursion_count = 0

def solve(solution, puzzle):
    global recursion_count
    recursion_count += 1

    if len(available_moves(solution)) == 0:
        for i in range(9):
            for j in range(9):
                if solution[i][j] == 'x':
                    solution[i][j] = ' '
        print_nice(solution)
        return True

    for (row,col) in available_moves(solution):
        if is_valid(solution, puzzle, row, col):
            new_solution = mark_board(solution, puzzle, row, col)
            if solve(new_solution, puzzle):
                return True

    return False

if __name__ == '__main__':
    
    solution = [[' ' for _ in range(9)] for _ in range(9)]
    puzzle = [ # Fiendish #136 Puzzle
        [ 0, 0, 1, 1, 1, 1, 2, 2, 2],
        [ 0, 3, 1, 1, 1, 5, 2, 2, 2],
        [ 0, 3, 1, 1, 5, 5, 5, 2, 2],
        [ 3, 3, 3, 3, 5, 5, 5, 2, 2],
        [ 3, 6, 7, 7, 5, 5, 5, 2, 2],
        [ 6, 6, 6, 7, 7, 5, 8, 2, 2],
        [ 6, 6, 6, 7, 7, 8, 8, 4, 4],
        [ 6, 6, 6, 7, 7, 8, 8, 8, 4],
        [ 6, 6, 6, 6, 7, 8, 8, 4, 4]
    ]
    valid_puzzle = solve(solution, puzzle)
    print(valid_puzzle)
    print(recursion_count)
            


    


