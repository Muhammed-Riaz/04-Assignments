import pygame
import time

# Initialize pygame
pygame.init()

# Constants for the canvas size and cell sizes
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

# Colors
BLUE = (0, 0, 255)      # Color for grid cells
WHITE = (255, 255, 255) # Color to "erase" to
PINK = (255, 105, 180)  # Color for eraser
BACKGROUND_COLOR = (0, 0, 0)  # Black background for better contrast

# Initialize screen
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))
pygame.display.set_caption("Canvas with Eraser")

# Function to draw the grid of blue cells
def draw_grid():
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            pygame.draw.rect(screen, BLUE, (col, row, CELL_SIZE, CELL_SIZE))

# Function to draw the eraser
def draw_eraser(x, y):
    pygame.draw.rect(screen, PINK, (x, y, ERASER_SIZE, ERASER_SIZE))

# Main game loop
def main():
    running = True
    eraser_x, eraser_y = 0, 0

    # Create the initial grid
    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    
    # Update the screen with the grid
    pygame.display.flip()

    # Start the game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Update the position of the eraser
        eraser_x = mouse_x - ERASER_SIZE // 2
        eraser_y = mouse_y - ERASER_SIZE // 2

        # Draw the grid again to keep it on the screen
        draw_grid()

        # Draw the eraser at the new position
        draw_eraser(eraser_x, eraser_y)

        # Erase cells that are overlapping with the eraser
        erase_cells(eraser_x, eraser_y)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        pygame.time.Clock().tick(60)

    pygame.quit()

# Function to erase cells that are overlapping with the eraser
def erase_cells(eraser_x, eraser_y):
    # For simplicity, we erase the cells that overlap with the pink eraser.
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            if (eraser_x < col + CELL_SIZE and eraser_x + ERASER_SIZE > col) and \
               (eraser_y < row + CELL_SIZE and eraser_y + ERASER_SIZE > row):
                pygame.draw.rect(screen, WHITE, (col, row, CELL_SIZE, CELL_SIZE))

if __name__ == "__main__":
    main()
