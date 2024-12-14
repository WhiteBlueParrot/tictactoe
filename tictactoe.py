import random

ROWS, COLUMNS = 3, 3

GRID = [['-' for column in range(COLUMNS)] for row in range(ROWS)]  # grid[row][column]


def print_grid(grid):
    print('  ', end='')  # blank space top left of the grid
    print(*range(COLUMNS))  # column coordinates
    for index, rows in enumerate(grid):
        print(index, end=' ')  # row coordinates
        print(*rows, sep=' ')  # rows


def check_status(grid, current_player):
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != '-' or \
            grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != '-' or \
            grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != '-':  # 3 in row
        status = f'{current_player} WON!'
    elif grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != '-' or \
            grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != '-' or \
            grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != '-':  # 3 in column
        status = f'{current_player} WON!'
    elif grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '-' or \
            grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '-':  # 3 in diagonal
        status = f'{current_player} WON!'
    elif not any('-' in row for row in grid):  # if all spaces are either 'o' or 'x'
        status = 'Draw!'
    else:
        status = 'Ongoing...'

    return status


def next_turn(current_player):  # switching players
    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'

    return current_player


def validate_choice(choice):  # testing whether player's input is correct or not
    if not choice.isnumeric():  # retry if input has non-digits
        print(f"Expected 2 digits, got '{choice}'. Try Again")
        print_grid(GRID)
        return False
    elif len(choice) != 2:  # retry if more than 2 digits
        print(f'Expected 2 digits, got {len(choice)} digits instead. Try Again')
        print_grid(GRID)
        return False

    row, column = int(choice[0]), int(choice[1])

    if row >= ROWS or column >= COLUMNS:
        print('Coordinates out of range, try again')
        print_grid(GRID)
        return False
    elif GRID[row][column] != '-':
        print('Space already occupied, try again')
        print_grid(GRID)
        return False
    else:
        return True


game_status = 'Ongoing...'
player = random.choice(('x', 'o'))  # randomly choosing who goes first

while True:  # The Game
    print_grid(GRID)  # printing the grid
    while True:  # player chooses a spot
        print('\n' + f"{player}'s turn!" + '\n')
        coordinates = input('Enter row and column of where you want to mark: ')
        if validate_choice(coordinates):
            row, column = int(coordinates[0]), int(coordinates[1])
            break

    GRID[row][column] = player  # marking the chosen empty space
    game_status = check_status(GRID, player)
    if game_status != 'Ongoing...':
        print(game_status)
        break  # ending the game if it's not ongoing (win or draw)
    player = next_turn(player)

print('GG!!!' + '\n')
print_grid(GRID)
