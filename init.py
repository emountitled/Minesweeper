import random
from block import Block
from pic_swicher import picture_switcher
import sys
import time

global start_time

def set_mines(blocks, settings):
    ''' 初始化mine的位置 '''    
    # 根据mine_number，最开始的几个block设只为mine
    for i in range(0, settings.mine_number):
        x = i / settings.block_xnum
        y = i % settings.block_ynum
        blocks[i].xch_pic('mine')
    # 重制mine的位置，进行随机分布
    swap_time = len(blocks)
    for i in range(0, len(blocks)):
        num = random.randint(0,len(blocks)-1)
        t = blocks[i].img
        blocks[i].img = blocks[num].img
        blocks[num].img = t




def inArea(x, y ,settings):
    ''' 定界函数，判断坐标(x,y)是否合法 '''
    if 0<=x<settings.block_ynum and 0<=y<settings.block_xnum:
        return True
    else:
        return False 



def cal_num(blocks, settings):     
    ''' 根据埋的雷计算出每个方块的提示信息 '''
    for i in range(0,len(blocks)):
        num = 0
        # 将一维的 i 转化为二维坐标x, y
        x = i // settings.block_xnum
        y = i % settings.block_xnum
        for ii in range(x-1, x+2):
            for iii in range(y-1, y+2):
                if inArea(ii,iii,settings):
                    if blocks[ii*settings.block_xnum+iii].img == picture_switcher.get('mine'):
                        num += 1    
        if blocks[i].img != picture_switcher.get('mine'):
            blocks[i].xch_pic(num)

def open(x,y,settings):
    if inArea(x,y,settings):
        blocks[x*settings.block_xnum+y].revealed = True
    for ii in range(x-1, x+2):
        for iii in range(y-1, y+2):                    
            if inArea(ii,iii,settings):
                return open(ii,iii,settings)
    
        

    

def auto_span(blocks, settings):
    ''' 若该方块周围没有雷，则展开周围的所有方块 '''
    for i in range(0, len(blocks)):
        if blocks[i].revealed==True and blocks[i].flagged==False and blocks[i].img==picture_switcher.get(0):
            # 将一维的 i 转化为二维坐标x, y
            x = i // settings.block_xnum
            y = i % settings.block_xnum
            for ii in range(x-1, x+2):
                for iii in range(y-1, y+2):                    
                    if inArea(ii,iii,settings):
                        blocks[ii*settings.block_xnum+iii].revealed = True

def bomb(blocks, mb):
    ''' 判断是否踩到了雷 '''
    for i in range(0, len(blocks)):
        if blocks[i].revealed==True and blocks[i].img==picture_switcher.get('mine'):
            mb.update_msg("Game Over")
            return False
           
            
            
    
            
            


def flagged_num(blocks,settings, mb):
    ''' 记录被标记过的方块总数 '''
    num = 0
    total = settings.mine_number
    bomb(blocks,mb)
    for i in range(0, len(blocks)):
        if blocks[i].flagged==True:
            num += 1
    
    if num == settings.mine_number:
        mb.update_msg("Win")
        return False
        
    else:
        mb.update_msg(str(total-num))
        return True
        

def show_time(start_time, mb):
    
    
    time_now = time.time()
    mb.update_msg(str(int(time_now-start_time)) + "S")
            
        
        
    

