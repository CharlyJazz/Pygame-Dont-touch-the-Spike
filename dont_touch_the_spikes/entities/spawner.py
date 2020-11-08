from dont_touch_the_spikes.entities.spike import Spike
from dont_touch_the_spikes.settings.constants import WIDTH


class Spawner:
    def __init__(self, score: int, orientation: str):
        self.score = score
        self.orientation = orientation

    def spawn_spikes(self):
        spikes = []

        if self.score <= 0:
            spikes.append(self.spawn_level_0())
        elif self.score <= 10:
            spikes.append(self.spawn_level_1())
        elif self.score <= 20:
            spikes.append(self.spawn_level_2())
        elif self.score <= 30:
            spikes.append(self.spawn_level_3())
        elif self.score >= 40:
            spikes.append(self.spawn_level_4())

        size = 65
        [spikes.append(Spike(size, 1, 'TOP', i)) for i in range(1, 10)]
        [spikes.append(Spike(size, 1, 'BOTTOM', i)) for i in range(1, 10)]

        return spikes

    def spawn_level_0(self):
        return [
            Spike(50, 1, self.orientation),
            Spike(50, 1, self.orientation),
            Spike(50, 1, self.orientation)
        ]

    def spawn_level_1(self):
        return [
            Spike(50, 1, self.orientation),
            Spike(50, 1, self.orientation),
            Spike(50, 1, self.orientation),
            Spike(70, 1, self.orientation)
        ]

    def spawn_level_2(self):
        return [
            Spike(50, 1, self.orientation),
            Spike(50, 1, self.orientation),
            Spike(70, 2, self.orientation),
            Spike(80, 2, self.orientation)
        ]

    def spawn_level_3(self):
        return [
            Spike(70, 2, self.orientation),
            Spike(80, 2, self.orientation),
            Spike(80, 3, self.orientation),
            Spike(70, 3, self.orientation)
        ]

    def spawn_level_4(self):
        return [
            Spike(100, 1, self.orientation),
            Spike(80, 2, self.orientation),
            Spike(60, 3, self.orientation),
            Spike(70, 4, self.orientation),
            Spike(90, 5, self.orientation)
        ]