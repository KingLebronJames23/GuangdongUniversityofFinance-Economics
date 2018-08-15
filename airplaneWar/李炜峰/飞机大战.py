import pygame
import random
pygame.init()
pygame.mixer.init()
#导入字体
font=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",36)
font1=pygame.font.Font("C:\Windows\Fonts\SimHei.ttf",14)
#创建屏幕
screen=pygame.display.set_mode((400,700))
#判断屏幕号数
what_screen=1   #初始化为1号屏幕
#导入游戏开始背景图
bigin_back=pygame.image.load(r"images\9.png")
bigin_back=pygame.transform.scale(bigin_back,(400,700))
#导入开始音乐
bigin_music=pygame.mixer.Sound(r"sound\bigin_miuse.ogg")
#导入开始按钮
bigin_button=pygame.image.load(r"images\bigin_button.png")
bigin_button=pygame.transform.scale(bigin_button,(150,50))
#导入游戏背景
back=pygame.image.load(r"images\back.png")
back=pygame.transform.scale(back,(400,1400))
back_y=-700
#导入游戏音乐
back_music=pygame.mixer.Sound(r"sound\game_music.ogg")

#设置基本属性
score=0             #得分
life=100            #生命
gret=1              #等级
time=0              #击中敌机次数
wuji=-999999        #废弃子弹所在坐标

#创建我方飞机
hero=pygame.image.load("images\hero.gif")
h_rect=hero.get_rect()
h_width=h_rect.width
h_height=h_rect.height
hx=100              #初始横坐标
hy=700-h_height     #初始纵坐标

#创建我方升级版飞机
hero1=pygame.image.load("images\enemy2_n2.png")
h1_rect=hero1.get_rect()
h1_width=h1_rect.width
h1_height=h1_rect.height
h1x=100             #初始横坐标
h1y=700-h1_height   #初始纵坐标

#创建普通子弹
bullet=pygame.image.load(r"images\bullet.png")
bullet_x=[]
bullet_y=[]
s_num=0         #子弹数目计数器
#产生20颗子弹
for i in range(20):
    bullet_x.append(wuji)
    bullet_y.append(wuji)

#创建升级版子弹
bullet1=pygame.image.load(r"images\bullet1.png")
bullet1_x=[]
bullet1_y=[]
bullet1_time=1     #子弹可发射次数
#产生50颗子弹
for i in range(50):
    bullet1_x.append(wuji)
    bullet1_y.append(wuji)

#创建敌方飞机
enemy0=pygame.image.load(r"images\enemy0.png")
enemy0_down=pygame.image.load(r"images\enemy0_down3.png")
e0_over_music=pygame.mixer.Sound(r"sound\enemy3_down.wav")
e0_rect=enemy0.get_rect()
e0_width=e0_rect.width
e0_height=e0_rect.height
e0_x=[]
e0_y=[]
e0_num=30
#初始化飞机
def pain_e0():
    for i in range(e0_num):
        e0_x.append(random.randint(0,350))
        e0_y.append(-100*i)

#创建敌方升级版飞机
enemy1=pygame.image.load(r"images\enemy1.png")
enemy1_down=pygame.image.load(r"images\enemy1_down3.png")
e1_over_music=pygame.mixer.Sound(r"sound\enemy1_down.wav")
e1_rect=enemy1.get_rect()
e1_width=e1_rect.width
e1_height=e1_rect.height
e1_x=[]
e1_y=[]
e1_num=10
def pain_e1():
    for i in range(e1_num):
        e1_x.append(random.randint(0,350))
        e1_y.append(i*(-1000))

while True:
    if what_screen==1:          #1号屏幕
        #产生游戏开始背景图，按钮图，通告文字
        screen.blit(bigin_back, (0, 0))
        screen.blit(bigin_button,(125,550))
        screen.blit(font1.render("抵制不良游戏，拒绝盗版游戏。 注意自我保护，谨防受骗上当。" , True, (255, 255, 255)), (10, 630))
        screen.blit(font1.render("适度游戏益脑，沉迷游戏伤身。 合理安排时间，享受健康生活。", True, (255, 255, 255)), (10, 650))
        #关闭游戏背景音乐，打开开始音乐
        back_music.stop()
        bigin_music.play()
    if what_screen==2:          #2号屏幕
        # 打开游戏背景音乐，关闭开始音乐
        bigin_music.stop()
        back_music.play()
        #产生游戏背景，并使背景运动
        screen.blit(back,(0,back_y))
        back_y+=1
        if back_y==0:
            back_y=-700
        #判断击中敌机数目
        if time>=20:#大于20，等级加1，升级版飞机可发射1次子弹，重置为0
            gret+=1
            bullet1_time=1
            time=0
        #判断升级版子弹是否可以发射
        if bullet1_time==1:
            #我方飞机变为升级版飞机
            hero = pygame.image.load("images\enemy2_n2.png")
        #画子弹
        for i in range(20):
            screen.blit(bullet, (bullet_x[i]-10,bullet_y[i]))
            bullet_y[i]-=2
        for i in range(50):
            screen.blit(bullet1, (bullet1_x[i] - 10, bullet1_y[i]))
            bullet1_y[i]-=2
        #画我方飞机
        screen.blit(hero, (hx - h_width / 2, hy))
        #画敌方飞机
        pain_e0()
        pain_e1()
        #敌方飞机运动
        for i in range(e0_num):
            screen.blit(enemy0, (e0_x[i],e0_y[i]))
            e0_y[i]+= 2
        #判断等级
        if gret>5:
            #大于5级，产生升级版敌方飞机
            for i in range(e1_num):
                screen.blit(enemy1, (e1_x[i],e1_y[i]))
                e1_y[i]+=3
        #判断子弹是否击中两种敌机
        for i in range(20):
            for j in range(e0_num):
                if bullet_y[i] <= e0_y[j] + e0_height and e0_x[j] <= bullet_x[i] <= e0_x[j] + e0_width:
                    score+=1        #分数加1
                    time+=1         #击中次数加1
                    e0_over_music.play()    #产生击中音乐
                    screen.blit(enemy0_down, (e0_x[j], e0_y[j]))        #画出被击中图片
                    #敌机重新创建
                    e0_x[j] =random.randint(0,350)
                    e0_y[j] =random.randint(-5000,-1000)
                    #子弹进入废弃状态
                    bullet_x[i]=wuji
                    bullet_y[i]=wuji
        for i in range(20):
            for j in range(e1_num):
                if bullet_y[i] <= e1_y[j] + e1_height and e1_x[j] <= bullet_x[i] <= e1_x[j] + e0_width:
                    score+=2
                    time+=1
                    e1_over_music.play()
                    screen.blit(enemy1_down, (e1_x[j], e1_y[j]))
                    e1_x[j] =random.randint(0,350)
                    e1_y[j] =random.randint(-5000,-1000)
                    bullet_x[i]=wuji
                    bullet_y[i]=wuji

        # 判断升级版子弹是否击中两种敌机
        for i in range(50):
            for j in range(e0_num):
                if bullet1_y[i] <= e0_y[j] + e0_height and e0_x[j] <= bullet1_x[i] <= e0_x[j] + e0_width:
                    score+=1
                    e0_over_music.play()
                    screen.blit(enemy0_down, (e0_x[j], e0_y[j]))
                    e0_x[j] =random.randint(0,350)
                    e0_y[j] =random.randint(-5000,-1000)
                    bullet1_x[i]=wuji
                    bullet1_y[i]=wuji
        for i in range(50):
            for j in range(e1_num):
                if bullet1_y[i] <= e1_y[j] + e1_height and e1_x[j] <= bullet1_x[i] <= e1_x[j] + e0_width:
                    score+=2
                    e1_over_music.play()
                    screen.blit(enemy1_down, (e1_x[j], e1_y[j]))
                    e1_x[j] =random.randint(0,350)
                    e1_y[j] =random.randint(-5000,-1000)
                    bullet1_x[i]=wuji
                    bullet1_y[i]=wuji

        #处理飞机，子弹出界问题
        for i in range(e0_num):
            if e0_y[i]>=700:
                e0_y[i]=random.randint(-5000,-1000)
                score-=1
                life-=2
        for i in range(e1_num):
            if e1_y[i]>=700:
                e1_y[i]=random.randint(-5000,-1000)
                score-=2
                life-=3
        for i in range(20):
            if bullet_y[i]==0:
                bullet_y[i]=wuji
        for i in range(50):
            if bullet1_y[i]==0:
                bullet1_y[i]=wuji

        #判断生命
        if life<=0:#生命小于0，统一为0，屏幕变为1号屏幕
            life=0
            what_screen=1
        #限制子弹数量
        if bullet_y[3]==wuji:#当第3发子弹废弃时，子弹可以允许重新产生
                s_num=0
        #屏幕产生得分，生命
        screen.blit(font.render("得分：" + str(score), True, (255, 255, 255)), (10, 10))
        screen.blit(font.render("生命：" + str(life), True, (255, 255, 255)), (10, 45))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            #获取鼠标位置
            a,b=pygame.mouse.get_pos()
            #判断屏幕1时，鼠标是否点击开始按钮
            if what_screen==1 and 125<=a<=275 and 550<=b<=600:
                #清空上一局敌方飞机
                e0_x.clear()
                e0_y.clear()
                e1_x.clear()
                e1_y.clear()
                #重新画敌机
                pain_e0()
                pain_e1()
                #屏幕变为2号，生命，分数刷新
                what_screen=2
                life=100
                score=0
                bullet1_time=1
            #判断屏幕2时，发射子弹
            if what_screen==2 and s_num<20:
                bullet_x[s_num],a=event.pos
                bullet_y[s_num] = hy - h_height / 2
                s_num+=1
        hx, a = pygame.mouse.get_pos()
        if event.type==pygame.KEYDOWN:
            #当升级版子弹允许发射时，点击“m”，发射
            if chr(event.key)=="m" and bullet1_time==1 and what_screen==2:
                bullet1_time=0
                hero = pygame.image.load("images\hero.gif")
                for i in range(50):
                    bullet1_x[i]=i*20
                    bullet1_y[i] =hy-h_height/2
    pygame.display.update()