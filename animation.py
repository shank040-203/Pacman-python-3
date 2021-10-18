import pygame

import pacman

pacman_normal = None
pacman_movement = None
pacman_death = None
ghost_images = None
frightened_ghost_1 = None
frightened_ghost_2 = None

frame_count = 0


def load_images():
    global pacman_normal, pacman_movement, pacman_death, ghost_images, frightened_ghost_1, frightened_ghost_2
    # Load all the images
    # Pacman's images
    pacman_normal = pygame.image.load('Images/Pacman/pacman_normal.png')
    pacman_movement = {pacman.UP_dir: pygame.image.load('Images/Pacman/pacman_U.png'),
                       pacman.DOWN_dir: pygame.image.load('Images/Pacman/pacman_D.png'),
                       pacman.LEFT_dir: pygame.image.load('Images/Pacman/pacman_L.png'),
                       pacman.RIGHT_dir: pygame.image.load('Images/Pacman/pacman_R.png'),
                       pacman.NULL_dir: pacman_normal}
    pacman_death = [pacman_normal, pacman_normal, pacman_normal, pacman_normal, pacman_normal, pacman_normal,
                    pacman_normal, pacman_movement[pacman.UP_dir]]
    for i in range(3, 8):
        pacman_death.append(pygame.image.load('Images/Pacman/pacman_die_{}.png'.format(i)))
    # Ghosts images
    # 0 up, 1 left, 2 down, 3 right
    ghost_images = {}
    for ghost in ['Blinky', 'Pinky', 'Inky', 'Clyde']:
        images = []
        for dirn in ['U', 'L', 'D', 'R']:
            path = 'Images/{}/{}_{}.png'.format(ghost, ghost, dirn)
            image = pygame.image.load(path)
            images.append(image)
        ghost_images[ghost] = images

    frightened_ghost_1 = pygame.image.load('Images/Frightened_1.png')
    frightened_ghost_2 = pygame.image.load('Images/Frightened_2.png')


def animate_ghost(ghost, current_time, start_time):
    if ghost.state != 'FRIGHTENED':
        # Use the normal sprites
        ghost_name = ghost.target.ghost
        ghost_n = ghost_name[0]
        for i in range(1, len(ghost_name)):
            ghost_n += ghost_name[i].lower()

        if ghost.direction == pacman.UP_dir:
            return ghost_images[ghost_n][0]
        elif ghost.direction == pacman.LEFT_dir:
            return ghost_images[ghost_n][1]
        elif ghost.direction == pacman.DOWN_dir:
            return ghost_images[ghost_n][2]
        elif ghost.direction == pacman.RIGHT_dir:
            return ghost_images[ghost_n][3]
    else:
        if current_time - start_time < 8000:
            return frightened_ghost_1
        else:
            return frightened_ghost_2


def animate_pacman(player, current_time, start_time):
    global frame_count
    frame_count += 1
    if player.alive:
        # Point in the right direction
        returning_image = pacman_movement[player.direction]

        # Animate it by swapping
        if frame_count % 5 == 0:
            if player.image == returning_image:
                return pacman_normal
            else:
                return returning_image
        else:
            return player.image
    else:
        if current_time - start_time < 3000:
            # Run the death animation
            time_per_frame = 200
            frame = (current_time - start_time) // time_per_frame
            try:
                return pacman_death[frame]
            except IndexError:
                return pacman_death[-2]  # Transparent sprite
