''' 创建开始游戏引导界面 '''

from tkinter import *
from settings import Settings
from mine_sweeper import run_game

root = Tk()
root.title('Welcome')
root.resizable(0,0)

# 设置Frame
frame_1 = Frame(root,width = 5,height = 5)
frame_2 = Frame(root,width = 5,height = 5)
frame_3 = Frame(root,width = 5,height = 5)
frame_4 = Frame(root,width = 5,height = 5)


#组件Label
label_1 = Label(frame_1,text = 'Column')
label_2 = Label(frame_2,text = 'Row')
label_3 = Label(frame_3,text = 'Mine')

 
#组件Text
text_1 = Text(frame_1,height = 1,width = 20,font = ('宋体',12))
text_2 = Text(frame_2,height = 1,width = 20,font = ('宋体',12))
text_3 = Text(frame_3,height=1,width = 20,font = ('宋体',12))

#组件Button
button = Button(frame_4,text = 'Start')


# 根据提交的信息开始游戏
def start(Event):
    column = text_1.get(1.0,END)
    row = text_2.get(1.0,END)
    mine = text_3.get(1.0,END)
    settings = Settings(column,row,mine)    
    run_game(settings)
    

#布局frame
frame_1.grid(row = 0,column = 0)
frame_2.grid(row = 1,column = 0,padx = 10)
frame_3.grid(row = 2,column = 0,padx = 10)
frame_4.grid(row = 3,column = 0,pady = 10)

#布局组件
label_1.grid(row = 0,column = 0,padx = 15,sticky=W)
label_2.grid(row = 3,column = 0,padx = 15,sticky=W)
label_3.grid(row = 3,column = 0,padx = 15,sticky=W)

#布局Button
button.grid(row = 3,column = 1,padx = 10,pady = 10,sticky = E)
#布局文本
text_1.grid(row = 1,column = 0,padx = 10)
text_2.grid(row = 5,column = 0,padx = 10)
text_3.grid(row = 5,column = 0,padx = 10)


# 给start键绑定游戏开始事件
button.bind('<Button-1>', start)


root.mainloop()
