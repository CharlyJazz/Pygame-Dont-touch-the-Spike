import pygame
from dont_touch_the_spikes.entities.bird import Bird
from dont_touch_the_spikes.entities.spawner import Spawner
from dont_touch_the_spikes.settings.constants import BACKGROUND, HEIGHT, WIDTH


class GameSurface(pygame.Surface):
    def __init__(self, screen):
        self.screen = screen
        self.spikes_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle()
        self.player = None
        self.points = 0
        self.reset()
        super().__init__(self.screen.get_size())

    def reset(self):
        self.points = 0

        spawner = Spawner(self.points, 'LEFT')

        self.spikes_group.empty()

        for spike in spawner.spawn_spikes():
            self.spikes_group.add(spike)

        self.player = Bird(self.change_orientation)
        self.player_group.add(self.player)

    def change_orientation(self, new_orientation):
        self.spikes_group.empty()
        self.points += 10

        spawner = Spawner(self.points, 'LEFT' if new_orientation == -1 else 'RIGHT')

        for spike in spawner.spawn_spikes():
            self.spikes_group.add(spike)

    def update(self):
        self.blit(BACKGROUND, (0, 0))
        self.player_group.draw(self)
        self.player_group.update()
        self.spikes_group.draw(self)
        self.spikes_group.update()
        self.screen.blit(self, (0, 0))
        self.render_score()

        # TODO: Use http://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_mask
        if not self.player.dying:
            for unit in pygame.sprite.groupcollide(self.player_group, self.spikes_group, False, False):
                unit.dead()
        else:
            self.render_try_again_message()

    def jump(self):
        self.player.enable_jump()

    def render_score(self):
        self.screen.blit(pygame.font.SysFont('Arial', 15).render(
            'Score {}'.format(str(self.points)), False,
            (106, 242, 65)), (WIDTH - 50, 10)
        )

    def render_try_again_message(self):
        self.screen.blit(pygame.font.SysFont('Arial', 25).render(
            'You are dead, press space to restart.', False,
            (0, 0, 0)), (25, HEIGHT / 2)
        )
