#主程序
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, 
			ai_settings.screen_height))
	pygame.display.set_caption("外星人降临-By Hung-Yi")

	#创建一艘飞船
	ship = Ship(ai_settings, screen)


	#开始游戏主循环
	while True:
		gf.check_events(ship)
		ship.update()

		gf.update_screen(ai_settings, screen, ship)

run_game()