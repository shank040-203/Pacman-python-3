import pygame

maze_width = 28
maze_height = 31
tile_size_px = 20

LEFT_dir = (-1, 0)
RIGHT_dir = (1, 0)
UP_dir = (0, -1)
DOWN_dir = (0, 1)
NULL_dir = (0, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, speed, surface, image):
        super(Player, self).__init__()

        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.new_direction = direction
        self.go_change = False

        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.x = self.x * tile_size_px
        self.rect.y = self.y * tile_size_px

        self.alive = False
        self.lives = 3

        self.image = image

    def move(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        if self.rect.x <= -2 * tile_size_px:
            self.rect.x = maze_width * tile_size_px
        elif self.rect.x >= (maze_width + 2) * tile_size_px:
            self.rect.x = -2 * tile_size_px

        self.x = self.rect.x // tile_size_px
        self.y = self.rect.y // tile_size_px

    def check_direction(self, grid):
        row, col = self.y, self.x
        t = self.speed // 2  # Tolerance
        allowed = (rough_equal(self.x*20, self.rect.x, t) and rough_equal(self.y*20, self.rect.y, t))  # Time to turn?

        # Changing direction
        try:
            if self.new_direction == UP_dir and grid[row-1][col] != 1:
                self.go_change = True
            elif self.new_direction == LEFT_dir and grid[row][col-1] != 1:
                self.go_change = True
            elif self.new_direction == DOWN_dir and grid[row+1][col] not in [1, 4]:
                self.go_change = True
            elif self.new_direction == RIGHT_dir and grid[row][col+1] != 1:
                self.go_change = True
            else:
                self.go_change = False
        except IndexError:
            pass  # Teleportation time - no worries

        # Checking if current direction takes pacman into a wall
        try:
            if (self.direction == UP_dir and grid[row - 1][col] == 1) and allowed:
                self.direction = NULL_dir
            elif (self.direction == LEFT_dir and grid[row][col - 1] == 1) and allowed:
                self.direction = NULL_dir
            elif (self.direction == DOWN_dir and grid[row + 1][col] in [1, 4]) and allowed:
                self.direction = NULL_dir
            elif (self.direction == RIGHT_dir and grid[row][col + 1] == 1) and allowed:
                self.direction = NULL_dir
        except IndexError:
            pass  # Teleportation time

        if allowed and self.go_change:
            self.direction = self.new_direction
            self.rect.x = self.x * tile_size_px
            self.rect.y = self.y * tile_size_px


def rough_equal(a, b, tolerance):
    if a > b:
        if a <= b + tolerance:
            return True
        else:
            return False
    elif a < b:
        if a >= b - tolerance:
            return True
        else:
            return False
    else:
        return True
