import pygame
import random
from pic_swicher import picture_switcher

''' 定义Block类 '''
class Block():
    
    def __init__(self,screen, x, y, pic):
        ''' 初始化方块并设置其初始位置 '''
        # self.init = random.randint(0,1)
        self.screen = screen

        # 加载方块图像并获取其外接矩形
        # 保存方块的真实值
        self.img = picture_switcher.get(pic)
        self.image = pygame.image.load(picture_switcher.get('block'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.revealed = False
        self.flagged = False
        

        # 将方块放在屏幕的左上角
        self.rect.x = x
        self.rect.y = y
        self.l_flag = False
        self.r_flag = False
    
    ''' 改变方块的图片 '''
    def xch_pic(self, pic):
        self.pic = pic
        self.img = picture_switcher.get(pic)
    
   
    
    def blitme(self):
    
        # l_clicked 用于判断是否鼠标左击
        l_clicked = self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()==(1,0,0)
        r_clicked = self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()==(0,0,1)
        
        if self.revealed:
            self.image = pygame.image.load(self.img)

        
                
        
        if l_clicked:
            if self.flagged==False:
                if self.revealed==False:
                    self.image = pygame.image.load(self.img)
                    self.revealed=True
                if  self.revealed==True:
                    self.image = pygame.image.load(self.img)
                    self.revealed=True
        
        if r_clicked:
            if self.revealed==False:
                if self.flagged==False:
                    self.image = pygame.image.load(picture_switcher.get('flag'))
                    
                if self.flagged==True:
                    self.image = pygame.image.load(picture_switcher.get('flag'))
                self.flagged = True
        

        
        
        
            

        self.screen.blit(self.image,self.rect)
