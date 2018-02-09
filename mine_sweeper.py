''' 设置游戏界面 '''
import sys
import pygame
import time
import tkinter.messagebox

from settings import Settings
from block import Block
from init import set_mines, cal_num, auto_span, bomb, flagged_num, show_time
from game_status import GameStatus
from msgboard import Msgboard
from timeboard import Timeboard


def run_game(settings):
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ms_settings = settings
    status = GameStatus(ms_settings)
    
    start_time = time.time()
    

    screen = pygame.display.set_mode((ms_settings.screen_width,ms_settings.screen_height))
    pygame.display.set_caption("Mine Sweeper")
    mb = Msgboard(ms_settings, screen, status, 0)
    mb1 = Msgboard(ms_settings, screen, status, 30)
    timer = Timeboard(ms_settings, screen,status, 60)

    # 设置背景色
    bg_color = ms_settings.bg_color

    # 创建一个方块阵
    blocks = []

    y = 0    
    for j in range(0, ms_settings.block_ynum):
        x = 0
        for i in range(0, ms_settings.block_xnum):
            block = Block(screen,x,y, 0)
            blocks.append(block)
            x += 32
        y += 32 
    
    set_mines(blocks, ms_settings)
    cal_num(blocks, ms_settings)
    
    
    
    # print(blocks[0].revealed)
    
    
    # 开始游戏的主循环
    while True:
        
        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
        # 每次循环都重绘屏幕
        screen.fill(ms_settings.bg_color)
        auto_span(blocks, ms_settings)

        if bomb(blocks, mb1) == False:
            info = 'Game Over'
            break
        if flagged_num(blocks,ms_settings, mb) == False:
            game_time = time.time()-start_time
            info = 'You Win!\nTime:' + str(int(game_time)) + 'S'
            break
        show_time(start_time, timer)
        
        
        for i in blocks:
            i.blitme()
        
        
        mb.show_msg()
        mb1.show_msg()
        timer.show_msg()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
    
    

    
    tkinter.messagebox.askokcancel('Info',info)

