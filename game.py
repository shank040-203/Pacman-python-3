# --------------------- #
# RUN THIS FOR THE GAME #
# --------------------- #


def game():
    import pygame

    import pacman
    import ghosts
    import animation

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    PINK = (255, 184, 255)
    TURQUOISE = (0, 255, 255)
    ORANGE = (255, 184, 82)
    # BLACK = (0, 0, 0)

    maze_width = 28
    maze_height = 37
    tile_size_px = 20

    mob_speed = 2


    # The maze - 0: Empty, 1: Wall, 2: Pellet, 3: Power Pellet, 4: Ghost house entrance
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
            [0, 0, 0, 0, 3, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 3, 0, 0, 0, 0],
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
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
    maze_temp = [[j for j in i] for i in maze]

    # Instructions
    '''
    print('INSTRUCTIONS:           # Triple quote these
------------
Use the arrow keys to control pacman (The yellow square). There are 4 ghosts who will attempt to catch pacman
(they are pretty good at it!) and if they touch pacman, then he loses a life. Lose 3 lives and you lose. To progress to
the next level, eat all the pellets. The larger pellets will turn the ghosts blue and you can eat them for points.
They can help you out of tight spots. Use them carefully.
Try to get a high score!')

    _ = input('Press enter to enter the game: ')
    '''

    # Game Code
    pygame.init()
    score = 0

    screen = pygame.display.set_mode([maze_width*tile_size_px, maze_height*tile_size_px])
    pygame.display.set_caption('PAC-MAN')

    font = pygame.font.Font('freesansbold.ttf', 40)
    new_font = pygame.font.Font('freesansbold.ttf', 20)
    # Score text
    score_text = font.render('Score: {}'.format(score), True, WHITE, None)
    score_text_rect = score_text.get_rect()
    score_text_rect.x, score_text_rect.y = tile_size_px * 1, tile_size_px * 1
    # "Ready!" text
    ready_text = font.render('Ready!', True, YELLOW, None)
    ready_text_rect = ready_text.get_rect()
    ready_text_rect.x, ready_text_rect.y = tile_size_px * 10.7, tile_size_px * 20.5
    # Lives text
    lives_text = font.render('Lives: 3', True, WHITE, None)
    lives_text_rect = lives_text.get_rect()
    lives_text_rect.x, lives_text_rect.y = tile_size_px * 1, tile_size_px * 35
    # "ENDLESS MODE" text
    end_text = new_font.render('ENDLESS MODE', True, RED, None)
    end_text_rect = end_text.get_rect()
    end_text_rect.x, end_text_rect.y = tile_size_px * 18, tile_size_px * 1.5
    # Maze image
    maze_image = pygame.image.load('Images/maze_image.png')

    # Time to import a TON of images!
    offset = tile_size_px // 2
    animation.load_images()

    # Pacman surface
    pacman_look = pygame.Surface([tile_size_px, tile_size_px])
    pacman_look.fill(YELLOW)

    # Pacman object
    player = pacman.Player(13, 27, pacman.NULL_dir, mob_speed, pacman_look, animation.pacman_normal)

    # Targets
    blinky_target = ghosts.GhostTarget(27, 0, 'SCATTER', 'BLINKY')
    pinky_target = ghosts.GhostTarget(0, 0, 'SCATTER', 'PINKY')
    inky_target = ghosts.GhostTarget(27, 36, 'SCATTER', 'INKY')
    clyde_target = ghosts.GhostTarget(0, 36, 'SCATTER', 'CLYDE')

    targets = [blinky_target, pinky_target, inky_target, clyde_target]

    # Targets' surfaces
    blinky_target_surface = pygame.Surface((tile_size_px/2, tile_size_px/2))
    blinky_target_surface.fill(RED)
    pinky_target_surface = pygame.Surface((tile_size_px/2, tile_size_px/2))
    pinky_target_surface.fill(PINK)
    inky_target_surface = pygame.Surface((tile_size_px/2, tile_size_px/2))
    inky_target_surface.fill(TURQUOISE)
    clyde_target_surface = pygame.Surface((tile_size_px/2, tile_size_px/2))
    clyde_target_surface.fill(ORANGE)

    # Ghosts' surfaces
    frightened_surface = pygame.Surface((tile_size_px, tile_size_px))
    frightened_surface.fill(BLUE)
    blinky_surface = pygame.Surface((tile_size_px, tile_size_px))
    blinky_surface.fill(RED)
    pinky_surface = pygame.Surface((tile_size_px, tile_size_px))
    pinky_surface.fill(PINK)
    inky_surface = pygame.Surface((tile_size_px, tile_size_px))
    inky_surface.fill(TURQUOISE)
    clyde_surface = pygame.Surface((tile_size_px, tile_size_px))
    clyde_surface.fill(ORANGE)

    # Ghosts
    blinky = ghosts.Ghost(16, 15, mob_speed//2, pacman.RIGHT_dir, blinky_target, blinky_target.state, blinky_surface)
    pinky = ghosts.Ghost(11, 15, mob_speed//2, pacman.LEFT_dir, pinky_target, pinky_target.state, pinky_surface)
    inky = ghosts.Ghost(18, 15, mob_speed//2, pacman.RIGHT_dir, inky_target, inky_target.state, inky_surface)
    clyde = ghosts.Ghost(9, 15, mob_speed//2, pacman.LEFT_dir, clyde_target, clyde_target.state, clyde_surface)

    ghosts_list = [blinky, pinky, inky, clyde]
    ghosts_group = pygame.sprite.Group()
    for ghost in ghosts_list:
        ghosts_group.add(ghost)

    # Timers and other miscellaneous level variables
    # 30 seconds chase, 10 seconds scatter
    start_time = pygame.time.get_ticks()
    scatter_start = start_time
    frightened_start = 0
    ghost_eaten_count = 0
    # start_running = False
    pellet_count = 240
    dontdie = True
    reset_level = True

    level = 1

    game_over = False

    running = True
    while running:
        # Event Handler
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # pygame.display.quit()
                # pygame.quit()
            if player.alive:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player.new_direction = pacman.UP_dir
                    elif event.key == pygame.K_LEFT:
                        player.new_direction = pacman.LEFT_dir
                    elif event.key == pygame.K_DOWN:
                        player.new_direction = pacman.DOWN_dir
                    elif event.key == pygame.K_RIGHT:
                        player.new_direction = pacman.RIGHT_dir

        if current_time - start_time >= 5000 and not player.alive:
            # start_running = True
            # Bring the player back to life
            player.alive = True
            player.x, player.y = 13, 27  # Position the player
            player.rect.x, player.rect.y = tile_size_px * player.x, tile_size_px * player.y
            # Position the ghosts
            blinky.x, blinky.y = 16, 15
            blinky.rect.x, blinky.rect.y = tile_size_px * blinky.x, tile_size_px * blinky.y
            pinky.x, pinky.y = 11, 15
            pinky.rect.x, pinky.rect.y = tile_size_px * pinky.x, tile_size_px * pinky.y
            inky.x, inky.y = 18, 15
            inky.rect.x, inky.rect.y = tile_size_px * inky.x, tile_size_px * inky.y
            clyde.x, clyde.y = 9, 15
            clyde.rect.x, clyde.rect.y = tile_size_px * clyde.x, tile_size_px * clyde.y

        # Game logic
        if player.alive:
            player.check_direction(maze)
            player.move()

            try:
                if maze[player.y][player.x] == 2:
                    # Normal pellet
                    maze[player.y][player.x] = 0
                    score += 10
                    pellet_count -= 1
                elif maze[player.y][player.x] == 3:
                    # Power pellet
                    maze[player.y][player.x] = 0
                    for target in targets:
                        if target.state in ['SCATTER', 'CHASE']:
                            target.state = 'FRIGHTENED'
                            ghost_eaten_count = 0
                    frightened_start = pygame.time.get_ticks()
                    maze[player.y][player.x] = 0
                    for ghost in ghosts_list:
                        if ghost.direction == pacman.UP_dir:
                            ghost.direction = pacman.DOWN_dir
                        elif ghost.direction == pacman.LEFT_dir:
                            ghost.direction = pacman.RIGHT_dir
                        elif ghost.direction == pacman.DOWN_dir:
                            ghost.direction = pacman.UP_dir
                        else:
                            ghost.direction = pacman.LEFT_dir
                        ghost.check_direction(maze)
            except IndexError:
                pass

            # Targeting
            # Assign the target mode
            if current_time - frightened_start > 10000:
                # Frightened time up
                ghost_eaten_count = 0
                for target in targets:
                    if target.state == 'FRIGHTENED':
                        target.state = 'CHASE'
            if current_time - scatter_start > 10000:
                # Scatter time up
                for target in targets:
                    if target.state == 'SCATTER':
                        target.state = 'CHASE'
                if current_time - scatter_start < 10005:
                    for ghost in ghosts_list:
                        if ghost.direction == pacman.UP_dir:
                            ghost.direction = pacman.DOWN_dir
                        elif ghost.direction == pacman.LEFT_dir:
                            ghost.direction = pacman.RIGHT_dir
                        elif ghost.direction == pacman.DOWN_dir:
                            ghost.direction = pacman.UP_dir
                        else:
                            ghost.direction = pacman.LEFT_dir
                        ghost.check_direction(maze)
            if current_time - scatter_start > 40000:
                # Start next scatter
                scatter_start = current_time
                for target in targets:
                    if target.state == 'CHASE':
                        target.state = 'SCATTER'
            # Target based on the assigned mode
            for target in targets:
                if target.state == 'CHASE':
                    target.player_target(player, blinky, clyde)
                else:
                    target.other_target()

            # Move the ghosts
            blinky.check_direction(maze)
            blinky.move(level)
            pinky.check_direction(maze)
            pinky.move(level)
            inky.check_direction(maze)
            inky.move(level)
            clyde.check_direction(maze)
            clyde.move(level)

            # Check for collisions with ghosts
            collide_list = pygame.sprite.spritecollide(player, ghosts_group, False, None)
            for ghost in collide_list:
                if ghost.state in ['SCATTER', 'CHASE']:
                    # Kill pacman
                    score -= 500
                    player.alive = False
                    dontdie = False  # Please die
                    start_time = pygame.time.get_ticks()

                    # start_running = False
                    if player.lives == 1:
                        running = False
                        # pygame.display.quit()
                        # pygame.quit()
                    else:
                        player.lives -= 1

                elif ghost.state == 'FRIGHTENED':
                    ghost.state = 'EATEN'
                    score += 100 * 2 ** (ghost_eaten_count + 1)
                    ghost_eaten_count += 1
                    ghost.target.state = 'EATEN'

            if pellet_count == 0 and not game_over:
                # Reset level
                reset_level = True
                player.alive = False
                frightened_start = 0
                dontdie = True
                start_time = pygame.time.get_ticks()
                # start_running = False
                scatter_start = start_time

                level += 1

                if player.lives > 0:
                    pellet_count = 240

            # Game over
            if player.lives == 0:
                running = False
                # pygame.display.quit()
                # pygame.quit()

        # Drawing
        # Drawing the maze
        screen.blit(maze_image, (0, 0))
        # Drawing the "Ready!" text and positioning entities
        if 3000 < current_time - start_time < 5000:
            screen.blit(ready_text, ready_text_rect)
            # Position the player
            player.x, player.y = 13, 27
            player.rect.x, player.rect.y = tile_size_px * player.x, tile_size_px * player.y
            # Position the ghosts
            blinky.x, blinky.y = 16, 15
            blinky.rect.x, blinky.rect.y = tile_size_px * blinky.x, tile_size_px * blinky.y
            pinky.x, pinky.y = 11, 15
            pinky.rect.x, pinky.rect.y = tile_size_px * pinky.x, tile_size_px * pinky.y
            inky.x, inky.y = 18, 15
            inky.rect.x, inky.rect.y = tile_size_px * inky.x, tile_size_px * inky.y
            clyde.x, clyde.y = 9, 15
            clyde.rect.x, clyde.rect.y = tile_size_px * clyde.x, tile_size_px * clyde.y
            # Set ghost states to SCATTER
            for ghost in ghosts_list:
                ghost.state = 'SCATTER'
                ghost.direction = pacman.UP_dir
            if current_time - start_time > 4000 and reset_level:
                maze = [[j for j in i] for i in maze_temp]
                reset_level = False
            dontdie = True

        # Drawing the score
        score_text = font.render('Score: {}'.format(score), True, WHITE, None)
        screen.blit(score_text, score_text_rect)
        # Drawing the lives
        lives_text = font.render('Lives: {}'.format(player.lives), True, WHITE, None)
        screen.blit(lives_text, lives_text_rect)
        # Drawing "ENDLESS MODE"
        if level > 1:
            screen.blit(end_text, end_text_rect)
        # Drawing the pellets
        for i in range(maze_height):
            for j in range(maze_width):
                if maze[i][j] == 2:
                    pellet = pygame.Surface([tile_size_px/4, tile_size_px/4])
                    pellet.fill(WHITE)
                    screen.blit(pellet, (tile_size_px*j + 3*tile_size_px/8, tile_size_px*i + 3*tile_size_px/8))
                elif maze[i][j] == 3:
                    power_pellet = pygame.Surface((tile_size_px/2, tile_size_px/2))
                    power_pellet.fill(WHITE)
                    screen.blit(power_pellet, (tile_size_px*j + tile_size_px/4, tile_size_px*i + tile_size_px/4))
        # Drawing the ghosts
        if player.alive or (3000 < current_time - start_time < 5000):
            for ghost in ghosts_list:
                if ghost.state != 'EATEN':
                    ghost.image = animation.animate_ghost(ghost, current_time, frightened_start)
                    screen.blit(ghost.image, (ghost.rect.x - offset, ghost.rect.y - offset))
        if not dontdie:
            player.image = animation.animate_pacman(player, current_time, start_time)
            try:
                screen.blit(player.image, (player.rect.x - offset, player.rect.y - offset))
            except TypeError:
                pass
        else:
            screen.blit(animation.pacman_normal, (player.rect.x - offset, player.rect.y - offset))
            if current_time - start_time > 5000:
                dontdie = False

        '''
        # Drawing the targets
        
        screen.blit(blinky_target_surface, (blinky_target.x*tile_size_px + tile_size_px/4,
                                            blinky_target.y*tile_size_px + tile_size_px/4))
        screen.blit(pinky_target_surface, (pinky_target.x * tile_size_px + tile_size_px/4,
                                           pinky_target.y * tile_size_px + tile_size_px/4))
        screen.blit(inky_target_surface, (inky_target.x * tile_size_px + tile_size_px/4,
                                          inky_target.y * tile_size_px + tile_size_px/4))
        screen.blit(clyde_target_surface, (clyde_target.x * tile_size_px + tile_size_px/4,
                                           clyde_target.y * tile_size_px + tile_size_px/4))
        '''
        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()

    return score

game()
