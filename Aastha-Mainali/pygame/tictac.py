import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic-Tac-Toe")

# Colors
WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (242, 85, 96)
O_COLOR = (28, 170, 156)

# Grid size and cell dimensions
GRID_SIZE = 3
CELL_SIZE = screen_width // GRID_SIZE

# Fonts
font = pygame.font.Font(None, 100)

# Game state variables
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]  # 3x3 grid for Tic-Tac-Toe
player_turn = 'X'  # 'X' starts first
game_over = False
winner = None

# Draw the game grid
def draw_grid():
    for row in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (screen_width, row * CELL_SIZE), 2)
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, screen_height), 2)

# Draw the X's and O's
def draw_marks():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(screen, X_COLOR, (col * CELL_SIZE + 20, row * CELL_SIZE + 20), 
                                 ((col + 1) * CELL_SIZE - 20, (row + 1) * CELL_SIZE - 20), 15)
                pygame.draw.line(screen, X_COLOR, ((col + 1) * CELL_SIZE - 20, row * CELL_SIZE + 20),
                                 (col * CELL_SIZE + 20, (row + 1) * CELL_SIZE - 20), 15)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, O_COLOR, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 10, 10)

# Check for a winner
def check_winner():
    global winner
    # Check rows, columns and diagonals
    for i in range(GRID_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != '':
            winner = board[i][0]
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE + CELL_SIZE // 2), (screen_width, i * CELL_SIZE + CELL_SIZE // 2), 5)
            return True
        if board[0][i] == board[1][i] == board[2][i] != '':
            winner = board[0][i]
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE + CELL_SIZE // 2, 0), (i * CELL_SIZE + CELL_SIZE // 2, screen_height), 5)
            return True
    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        pygame.draw.line(screen, LINE_COLOR, (0, 0), (screen_width, screen_height), 5)
        return True
    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        pygame.draw.line(screen, LINE_COLOR, (screen_width, 0), (0, screen_height), 5)
        return True
    return False

# Check for a draw
def check_draw():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == '':
                return False
    return True

# Main game loop
while True:
    screen.fill(WHITE)
    draw_grid()
    draw_marks()

    if game_over:
        if winner:
            text = font.render(f'{winner} wins!', True, LINE_COLOR)
        else:
            text = font.render("It's a draw!", True, LINE_COLOR)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    else:
        # Check for a winner or a draw
        if check_winner():
            game_over = True
        elif check_draw():
            game_over = True

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE

            # Only place mark if the cell is empty
            if board[row][col] == '':
                board[row][col] = player_turn
                if player_turn == 'X':
                    player_turn = 'O'
                else:
                    player_turn = 'X'

    pygame.display.flip()
    pygame.time.Clock().tick(30)
