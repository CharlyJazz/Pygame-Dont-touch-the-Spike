from dont_touch_the_spikes.entities.bird import Bird
from dont_touch_the_spikes.entities.coin import Coin
from dont_touch_the_spikes.entities.spawner import Spawner
from dont_touch_the_spikes.settings.constants import *


class GameSurface(pygame.Surface):
    def __init__(self, screen):
        self.screen = screen
        self.spikes_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.GroupSingle(Bird(self.change_orientation))
        self.coin_group = pygame.sprite.GroupSingle(Coin())
        self.points = 0
        self.reset()
        self.coin_live_time = 1000
        self.coin_last_remove = 0
        super().__init__(self.screen.get_size())

    @property
    def player(self):
        return self.player_group.sprites()[0]

    def reset(self):
        self.points = 0

        spawner = Spawner(self.points, 'LEFT')

        self.spikes_group.empty()

        for spike in spawner.spawn_spikes():
            self.spikes_group.add(spike)

        self.player.reset()

    def change_orientation(self, new_orientation):
        self.spikes_group.empty()
        self.points += 10

        spawner = Spawner(self.points, 'LEFT' if new_orientation == -1 else 'RIGHT')

        for spike in spawner.spawn_spikes():
            self.spikes_group.add(spike)

    def update(self):
        self.check_coin_timing()
        self.blit(BACKGROUND, (0, 0))
        self.player_group.draw(self)
        self.player_group.update()
        self.spikes_group.draw(self)
        self.spikes_group.update()
        self.coin_group.draw(self)
        self.coin_group.update()
        self.screen.blit(self, (0, 0))
        self.render_score()

        if not self.player.dying:
            for unit in pygame.sprite.groupcollide(self.player_group, self.spikes_group, False, False):
                unit.dead()
            for _ in pygame.sprite.groupcollide(self.player_group, self.coin_group, False, False):
                self.points += 20
                self.create_coin()
        else:
            self.render_try_again_message()

    def jump(self):
        self.player.enable_jump()

    def render_score(self):
        self.screen.blit(pygame.font.SysFont('Arial', 25).render(
            str(self.points), False,
            (0, 0, 0)), (WIDTH - 30, 10)
        )

    def render_try_again_message(self):
        self.screen.blit(pygame.font.SysFont('Arial', 25).render(
            'You are dead, press enter to restart.', False,
            (0, 0, 0)), (100, HEIGHT / 2)
        )

    def check_coin_timing(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.coin_last_remove >= self.coin_live_time:
            self.coin_last_remove = pygame.time.get_ticks()
            self.create_coin()

    def create_coin(self):
        self.coin_group.add(Coin())