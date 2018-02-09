class Settings():
    ''' 储存《扫雷》的所有设置的信息 '''

    def __init__(self,x=15,y=10,m=10):
        ''' 初始化游戏的设置 '''
        # 设置背景色，以及提示信息的颜色
        self.bg_color = (230,230,230)
        self.ms_color = (230,0,0)
        
        # 设置方块的行和列
        self.block_xnum = int(x)
        self.block_ynum = int(y)

        # 设置雷的个数
        self.mine_number = int(m)

        # 根据方块的行和列设置窗口的大小
        self.screen_width = self.block_xnum*32
        self.screen_height = self.block_ynum*32+32

