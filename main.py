import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT)
FRAME_RATE = 60

class Game():
    def __init__(self):
        self.playing = True
        self.clock = pygame.time.Clock()

    def loop(self, window, screen):

        while self.playing:
            tick = self.clock.tick( FRAME_RATE )

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            window.fill( (255, 255, 255) )

            pygame.display.flip()

    def quit(self):
        self.playing = False


def main():
    pygame.init()
    window = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
    screen = pygame.Surface( SCREEN_RES )

    pygame.display.set_caption( 'Example' )

    game = Game()
    game.loop( window, screen )
    game.quit()

    pygame.quit()

if __name__ == '__main__':
    main()
