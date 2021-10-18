import pygame
import time

import pacman
import ghosts

maze_width = 28
maze_height = 31
tile_size_px = 10

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
PINK = (255, 184, 255)
TURQUOISE = (0, 255, 255)
ORANGE = (255, 184, 82)
BLACK = (0, 0, 0)

# 0: Empty, 1: Wall, 2: Pellet, 3: Power Pellet, 4: Ghost house entrance
pacman_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
               [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
               [1, 3, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1],
               [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
               [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
               [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
               [1, 2, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 2, 1],
               [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
               [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 4, 4, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
               [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0],
               [1, 1, 1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 1],
               [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
               [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
               [1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1],
               [1, 3, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 3, 1],
               [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
               [1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1],
               [1, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1],
               [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
               [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1],
               [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
               ]

# Game code
pygame.init()

maze_image = pygame.image.load('Images/maze_img_10px.png')

level = 0
level_scores = [0, 0, 0, 0]

screen = pygame.display.set_mode([maze_width*tile_size_px, maze_height*tile_size_px])

image_scale = 2
pellet_scale = 4

fright_time = 10000

# Pacman initialization - Surface (temporary)
pacman_look = pygame.Surface([tile_size_px*image_scale, tile_size_px*image_scale])
pacman_look.fill(YELLOW)
# Pacman initialization - Images
pacman_image_1 = pygame.image.load('Images/Pacman/pacman_normal.png')
pacman_image_scaled_1 = pygame.transform.scale(pacman_image_1, [int(tile_size_px*image_scale),
                                                                int(tile_size_px*image_scale)])
pacman_image_2 = pygame.image.load('Images/Pacman/pacman_R.png')
pacman_image_scaled_2 = pygame.transform.scale(pacman_image_2, [int(tile_size_px * image_scale),
                                                                int(tile_size_px * image_scale)])
# Pacman initialization - Player object
player = pacman.Player((14, 23), pacman.NULL_dir, pacman_look, pacman_image_scaled_1)

# Blinky initialization - Surface (temporary)
blinky_look = pygame.Surface([tile_size_px, tile_size_px])
blinky_look.fill(RED)
# Blinky initialization - Ghost object
blinky = ghosts.Ghost((26, 1), pacman.LEFT_dir, blinky_look)
# Blinky initialization - Images
blinky_U = pygame.image.load('Images/Blinky/Blinky_U.png')
blinky_L = pygame.image.load('Images/Blinky/Blinky_L.png')
blinky_D = pygame.image.load('Images/Blinky/Blinky_D.png')
blinky_R = pygame.image.load('Images/Blinky/Blinky_R.png')

# Pinky initialization - Surface (temporary)
pinky_look = pygame.Surface([tile_size_px, tile_size_px])
pinky_look.fill(PINK)
# Pinky initialization - Ghost object
pinky = ghosts.Ghost((1, 1), pacman.RIGHT_dir, pinky_look)

# Inky initialization - Surface (temporary)
inky_look = pygame.Surface([tile_size_px, tile_size_px])
inky_look.fill(TURQUOISE)
# Inky initialization - Ghost object
inky = ghosts.Ghost((26, 29), pacman.LEFT_dir, inky_look)

# Clyde initialization - Surface (temporary)
clyde_look = pygame.Surface([tile_size_px, tile_size_px])
clyde_look.fill(ORANGE)
# Clyde initialization - Ghost object
clyde = ghosts.Ghost((1, 29), pacman.RIGHT_dir, inky_look)

# Frightened ghost surface
frightened_ghost_look = pygame.Surface([tile_size_px, tile_size_px])
frightened_ghost_look.fill(BLUE)

start_fright = 0

running = True
while running:
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if player.alive:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.nd = pacman.UP_dir
                elif event.key == pygame.K_LEFT:
                    player.nd = pacman.LEFT_dir
                elif event.key == pygame.K_DOWN:
                    player.nd = pacman.DOWN_dir
                elif event.key == pygame.K_RIGHT:
                    player.nd = pacman.RIGHT_dir

    # Game logic
    if player.alive:
        # Player code
        player.change_dir(player.nd, pacman_maze)
        player.move()
        ghost_touched = player.touch(blinky.pos, pinky.pos, inky.pos, clyde.pos)
        if ghost_touched == 'Blinky':
            if blinky.state == 'FRIGHTENED':
                blinky.state = 'EATEN'
                level_scores[level] += 200
        elif ghost_touched == 'Pinky':
            if pinky.state == 'FRIGHTENED':
                pinky.state = 'EATEN'
                level_scores[level] += 200
        elif ghost_touched == 'Inky':
            if inky.state == 'FRIGHTENED':
                inky.state = 'EATEN'
                level_scores[level] += 200
        elif ghost_touched == 'Clyde':
            if clyde.state == 'FRIGHTENED':
                clyde.state = 'EATEN'
                level_scores[level] += 200

        ate = player.eat(pacman_maze)
        if ate and ate != 'POWER':
            level_scores[level] = level_scores[level] + 1
        if ate == 'POWER':
            blinky.state = 'FRIGHTENED'
            pinky.state = 'FRIGHTENED'
            inky.state = 'FRIGHTENED'
            clyde.state = 'FRIGHTENED'

            blinky.direction = (-blinky.direction[0], -blinky.direction[1])
            pinky.direction = (-pinky.direction[0], -pinky.direction[1])
            inky.direction = (-inky.direction[0], -inky.direction[1])
            clyde.direction = (-clyde.direction[0], -clyde.direction[1])

            blinky.set_dir((26, 1), pacman_maze)
            pinky.set_dir((1, 1), pacman_maze)
            inky.set_dir((29, 26), pacman_maze)
            clyde.set_dir((1, 29), pacman_maze)

            start_fright = pygame.time.get_ticks()

        ghost_states = [blinky.state, pinky.state, inky.state, clyde.state]
        if pygame.time.get_ticks() - start_fright > fright_time and 'FRIGHTENED' in ghost_states:
            start_fright = 0
            # Revert to chase
            blinky.state = 'CHASE'
            pinky.state = 'CHASE'
            inky.state = 'CHASE'
            clyde.state = 'CHASE'

        # Ghost code - Blinky, the chaser
        if blinky.state != 'EATEN':
            blinky.set_dir(player.pos, pacman_maze)
        else:
            blinky.set_dir((14, 11), pacman_maze)
        blinky.move()
        # Ghost code - Pinky, the flanker
        try:
            p_target = (player.pos[0] + 4*player.direction[0],
                        player.pos[1] + 4*player.direction[1])
            if player.direction == pacman.UP_dir:
                p_target = (player.pos[0] - 4,
                            player.pos[1] - 4)
        except IndexError:
            p_target = player.pos
        if pinky.state == 'EATEN':
            p_target = (14, 11)
        pinky.set_dir(p_target, pacman_maze)
        pinky.move()
        # Ghost code - Inky, the ambusher
        try:
            intermediate_tile = (player.pos[0] + 2*player.direction[0],
                                 player.pos[1] + 2*player.direction[1])
            if player.direction == pacman.UP_dir:
                intermediate_tile = (player.pos[0] - 2,
                                     player.pos[1] - 2)
        except IndexError:
            intermediate_tile = player.pos
        i_target_vector = (player.pos[0] - blinky.pos[0],
                           player.pos[1] - blinky.pos[1])
        try:
            i_target = (player.pos[0] + i_target_vector[0],
                        player.pos[1] + i_target_vector[1])
        except IndexError:
            i_target = p_target
        if inky.state == 'EATEN':
            i_target = (14, 11)
        inky.set_dir(i_target, pacman_maze)
        inky.move()
        # Ghost code - Clyde, the guard
        dist_to_player = ((clyde.pos[0]-player.pos[0])**2 + (clyde.pos[1]-player.pos[1])**2)**0.5
        if dist_to_player > 8:
            c_target = player.pos
        else:
            c_target = (1, 29)
        if clyde.state == 'EATEN':
            c_target = (14, 11)
        clyde.set_dir(c_target, pacman_maze)
        clyde.move()

        if blinky.state == 'EATEN' and blinky.pos == (14, 11):
            blinky.state = 'CHASE'
        if pinky.state == 'EATEN' and pinky.pos == (14, 11):
            pinky.state = 'CHASE'
        if inky.state == 'EATEN' and inky.pos == (14, 11):
            inky.state = 'CHASE'
        if clyde.state == 'EATEN' and clyde.pos == (14, 11) :
            clyde.state = 'CHASE'

    # Drawing
    screen.blit(maze_image, [0, 0])
    # Draw the pellets first
    for i in range(maze_height):
        for j in range(maze_width):
            if pacman_maze[i][j] == 2:
                pellet = pygame.Surface([tile_size_px/pellet_scale, tile_size_px/pellet_scale])
                pellet.fill(WHITE)
                screen.blit(pellet, [tile_size_px * j + (tile_size_px - tile_size_px/pellet_scale)/2,
                                     tile_size_px * i + (tile_size_px - tile_size_px/pellet_scale)/2])
            elif pacman_maze[i][j] == 3:
                pellet = pygame.Surface([2*tile_size_px/pellet_scale, 2*tile_size_px/pellet_scale])
                pellet.fill(WHITE)
                screen.blit(pellet, [tile_size_px * j + (tile_size_px - tile_size_px / pellet_scale)/4,
                                     tile_size_px * i + (tile_size_px - tile_size_px / pellet_scale)/4])

    # Draw the ghosts next  - Blinky
    if blinky.state == 'CHASE' or blinky.state == 'SCATTER':
        if blinky.direction == pacman.UP_dir:
            blinky_image = blinky_U
        elif blinky.direction == pacman.LEFT_dir:
            blinky_image = blinky_L
        elif blinky.direction == pacman.DOWN_dir:
            blinky_image = blinky_D
        else:
            blinky_image = blinky_R
        screen.blit(blinky_image, [tile_size_px*blinky.pos[0]-tile_size_px/image_scale,
                                  tile_size_px*blinky.pos[1]-tile_size_px/image_scale])
    elif blinky.state == 'FRIGHTENED':
        screen.blit(frightened_ghost_look, [tile_size_px*blinky.pos[0],
                                            tile_size_px*blinky.pos[1]])

    if pinky.state != 'EATEN':
        screen.blit(pinky_look, [tile_size_px*pinky.pos[0],
                                 tile_size_px*pinky.pos[1]])
    # Inky
    if inky.state != 'EATEN':
        screen.blit(inky_look, [tile_size_px*inky.pos[0],
                                tile_size_px*inky.pos[1]])
    # Clyde
    if clyde.state != 'EATEN':
        screen.blit(clyde_look, [tile_size_px*clyde.pos[0],
                                 tile_size_px*clyde.pos[1]])
    # Draw pacman at the end
    if player.alive:
        pass
    screen.blit(player.image, [tile_size_px*player.pos[0]-tile_size_px/image_scale,
                               tile_size_px*player.pos[1]-tile_size_px/image_scale])

    pygame.display.flip()

    time.sleep(0.1)

print(level_scores)
print('Exited the loop')
