import pygame.font

class Msgboard():
    ''' 显示各种信息的分数面板 '''

    def __init__(self, settings, screen, status, top):
        ''' 初始化属性 '''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.status = status
        self.top = top

        #显示信息时使用的字体
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
    
        self.msg_str = ' '
    def update_msg(self, text):
        self.msg_str = text
    

    def show_msg(self):
        # 将字符串渲染成图像
        self.msg_image = self.font.render(self.msg_str, True,
            self.settings.ms_color)
        
        # 将信息显示在屏幕右上角
        self.score_rect = self.msg_image.get_rect()
        self.score_rect.center = self.score_rect.center
        self.score_rect.top = self.top
        self.screen.blit(self.msg_image, self.score_rect)
    
    