from dino_runner.components.obstacules.cactus import Cactus
from dino_runner.components.obstacules.bird import Bird
from dino_runner.components.obstacules.enemy_robot import EnemyRobot
from dino_runner.components.obstacules.enemy_sky_robot import EnemySkyRobot
from dino_runner.utils.constants import SHIELD_TYPE,DEFAULT_TYPE
import random, pygame


class ObstacleMager ():

    def __init__(self) :
        self.has_obstacle = False
        self.obstacle = None
        

    def update(self,game):
        if not self.has_obstacle:
            self.create_obstacle()
        if self.obstacle.rect.x > 0:
            self.has_obstacle = True
        else:
            self.has_obstacle = False
        self.obstacle.update(game)
        if game.player.rect.colliderect(self.obstacle.rect):
            if game.player.type == SHIELD_TYPE:
                game.player.type = DEFAULT_TYPE
                self.has_obstacle = False
            else:
                pygame.time.delay(300)
                game.playing = False

    def create_obstacle(self):
        Obstacle_list = [Cactus(), Bird(), EnemyRobot(),EnemySkyRobot()]
        self.obstacle = random.choice(Obstacle_list)


    def draw(self,screen):
        if self.has_obstacle:
            
            self.obstacle.draw(screen)