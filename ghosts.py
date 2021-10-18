import pygame
import random

# from pacman import UP_dir, DOWN_dir, LEFT_dir, RIGHT_dir, tile_size_px, maze_width
# from pacman import rough_equal

import pacman
UP_dir, DOWN_dir, LEFT_dir, RIGHT_dir, tile_size_px, maze_width = pacman.UP_dir, pacman.DOWN_dir, pacman.LEFT_dir, \
                                                                  pacman.RIGHT_dir, pacman.tile_size_px, \
                                                                  pacman.maze_width
rough_equal = pacman.rough_equal

mob_speed = 2


class GhostTarget:
    def __init__(self, x, y, state, ghost):
        self.x = x
        self.y = y

        self.state = state
        self.ghost = ghost

        self.random_targeted = False

    def player_target(self, player, blinky, clyde):
        # State = chase
        if self.ghost == 'BLINKY':
            # Target pacman
            self.x, self.y = player.x, player.y
        elif self.ghost == 'PINKY':
            # Target 4 tiles ahead of Pacman
            if player.direction != (0, 0):
                if player.direction != (0, -1):
                    self.x, self.y = player.x + 4*player.direction[0], player.y + 4*player.direction[1]
                else:
                    self.x, self.y = player.x - 4, player.y - 4
            else:
                if player.new_direction != (0, -1):
                    self.x, self.y = player.x + 4*player.new_direction[0], player.y + 4*player.new_direction[1]
                else:
                    self.x, self.y = player.x - 4, player.y - 4
        elif self.ghost == 'INKY':
            # Intermediate tile
            if player.direction != (0, 0):
                if player.direction != (0, -1):
                    int_x, int_y = player.x + 2 * player.direction[0], player.y + 2 * player.direction[1]
                else:
                    int_x, int_y = player.x - 2, player.y - 2
            else:
                if player.new_direction != (0, -1):
                    int_x, int_y = player.x + 2 * player.new_direction[0], player.y + 2 * player.new_direction[1]
                else:
                    int_x, int_y = player.x - 2, player.y - 2
            del_x = int_x - blinky.x
            del_y = int_y - blinky.y
            try:
                self.x, self.y = int_x + del_x, int_y + del_y
            except IndexError:
                pass
        elif self.ghost == 'CLYDE':
            if (((clyde.x - player.x)**2) + ((clyde.y - player.y)**2)) < 64:
                # Go back to scatter tile
                self.x, self.y = 0, 36
            else:
                # Target pacman
                self.x, self.y = player.x, player.y

    def other_target(self):
        if self.state == 'SCATTER':
            # Scatter targets for Blinky, Pinky, Inky, Clyde
            if self.ghost == 'BLINKY':
                self.x, self.y = 27, 0
            elif self.ghost == 'PINKY':
                self.x, self.y = 0, 0
            elif self.ghost == 'INKY':
                self.x, self.y = 27, 36
            else:
                self.x, self.y = 0, 36
        elif self.state == 'FRIGHTENED':
            # Frightened - target a random tile
            if not self.random_targeted:
                self.x, self.y = random.randint(0, 27), random.randint(0, 27)
                self.random_targeted = True
        elif self.state == 'EATEN':
            # Eaten - target the ghost house entrance
            self.x, self.y = 14, 15


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, direction, target, state, surface):
        super(Ghost, self).__init__()

        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.target = target

        self.state = state

        self.surface = surface
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = self.x * tile_size_px, self.y * tile_size_px

        self.image = None

    def check_direction(self, grid):
        # Additional
        self.state = self.target.state

        row, col = self.y, self.x
        t = self.speed // 2  # Tolerance
        # Time to turn?
        allowed = rough_equal(self.x*tile_size_px, self.rect.x, t) and rough_equal(self.y*tile_size_px, self.rect.y, t)
        # Changing direction
        if allowed:
            # Ready to turn!
            allowed_directions = [UP_dir, LEFT_dir, DOWN_dir, RIGHT_dir]
            # Ghosts cannot turn around
            if self.direction == UP_dir:
                allowed_directions.remove(DOWN_dir)
            elif self.direction == LEFT_dir:
                allowed_directions.remove(RIGHT_dir)
            elif self.direction == DOWN_dir:
                allowed_directions.remove(UP_dir)
            elif self.direction == RIGHT_dir:
                allowed_directions.remove(LEFT_dir)
            # Remove directions that lead into walls or the ghost house
            try:
                if grid[row-1][col] == 1:
                    if UP_dir in allowed_directions:
                        allowed_directions.remove(UP_dir)
                if grid[row][col-1] == 1:
                    if LEFT_dir in allowed_directions:
                        allowed_directions.remove(LEFT_dir)
                if grid[row+1][col] in [1, 4]:
                    if DOWN_dir in allowed_directions:
                        allowed_directions.remove(DOWN_dir)
                if grid[row][col+1] == 1:
                    if RIGHT_dir in allowed_directions:
                        allowed_directions.remove(RIGHT_dir)
            except IndexError:
                pass  # Teleportation time
            # When in teleportation tunnel, remove up and down directions
            if row == 18:
                if (self.rect.x < 5 * tile_size_px) or (self.rect.x > 22 * tile_size_px):
                    if UP_dir in allowed_directions:
                        allowed_directions.remove(UP_dir)
                    if DOWN_dir in allowed_directions:
                        allowed_directions.remove(DOWN_dir)
            # Choose direction that minimizes distance to Pacman
            min_distance = 40000
            min_distance_direction = allowed_directions[0]
            for allowed_direction in allowed_directions:
                next_position = (self.x + allowed_direction[0], self.y + allowed_direction[1])
                distance = (((next_position[0]-self.target.x)**2)+((next_position[1]-self.target.y)**2))
                if distance < min_distance:
                    min_distance = distance
                    min_distance_direction = allowed_direction
            # print('Going', min_distance_direction)
            self.direction = min_distance_direction
            # print(self.x, self.y, self.state)
            if self.state == 'EATEN' and (self.x == self.target.x and self.y == self.target.y):
                self.state = 'CHASE'
                self.target.state = 'CHASE'
                self.check_direction(grid)
                self.speed = mob_speed  # // 2  # <--------------------------------------------------------------------

        '''
        try :
            if self.new_direction == UP_dir and grid[row - 1][col] != 1 :
                self.go_change = True
            elif self.new_direction == LEFT_dir and grid[row][col - 1] != 1 :
                self.go_change = True
            elif self.new_direction == DOWN_dir and grid[row + 1][col] not in [1, 4] :
                self.go_change = True
            elif self.new_direction == RIGHT_dir and grid[row][col + 1] != 1 :
                self.go_change = True
            else :
                self.go_change = False
        except IndexError :
            pass  # Teleportation time - no worries

        # Checking if current direction takes pacman into a wall
        try :
            if (self.direction == UP_dir and grid[row - 1][col] == 1) and allowed :
                self.direction = NULL_dir
            elif (self.direction == LEFT_dir and grid[row][col - 1] == 1) and allowed :
                self.direction = NULL_dir
            elif (self.direction == DOWN_dir and grid[row + 1][col] in [1, 4]) and allowed :
                self.direction = NULL_dir
            elif (self.direction == RIGHT_dir and grid[row][col + 1] == 1) and allowed :
                self.direction = NULL_dir
        except IndexError :
            pass  # Teleportation time
        
        if allowed and self.go_change :
            self.direction = self.new_direction
            self.rect.x = self.x * tile_size_px
            self.rect.y = self.y * tile_size_px
        '''

    def move(self, level):
        if self.state == 'FRIGHTENED':
            self.speed = 1
        else:
            if self.rect.x % 2 == 0 and self.rect.y % 2 == 0:
                if level > 1:
                    self.speed = 2  # // 2
                else:
                    self.speed = 1

        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        if self.rect.x <= -2 * tile_size_px:
            self.rect.x = maze_width * tile_size_px
        elif self.rect.x >= (maze_width + 2) * tile_size_px:
            self.rect.x = -2 * tile_size_px

        self.x = self.rect.x // tile_size_px
        self.y = self.rect.y // tile_size_px

