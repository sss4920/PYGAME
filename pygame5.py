__author__ = 'sss4920@naver.com'
'''
오늘은 pygame에서 적을 만들어 볼겁니다..
'''

import pygame       #pygame을 임포트 합니다
import random       #random을 임포트 합니다.

WHITE = (255,255,255) # 흰색을 표현하는 값
pad_width = 1024 #게임판의 폭
pad_height = 512#게임판의 높이를 각각 전역변수에 저장
background_width = 1024

def drawObject(obj,x,y): #게임판에 그려지는 모든 객체들은 앞으로 이 함수로 통일한다
    global gamepad
    gamepad.blit(obj,(x,y))



def runGame(): #실제 게임이 구동되는 함수 밑에 initGame()함수에서 호출됨
    global gamepad, aircraft,clock,background1,background2
    global bat,fires
    
    x = pad_width *0.05
    y = pad_height * 0.8    #비행기의 최초위치를 게임판의 왼쪽 적당한 위치에 두도록 좌표설정 비행기가 아래위로 움직이기 때문에 비행기위 y좌표 변화를 y_change변수로 나타낼 것
    y_change = 0

    background1_x=0#배경이미지의 좌상단 모서리의 x좌표를 나타내고 최초값으로 0지정
    background2_x=background_width

    bat_x=pad_width
    bat_y = random.randrange(0,pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0,pad_height)
    random.shuffle(fires)
    fire = fires[0]
    
    crashed = False
    while not crashed:
        for event in pygame.event.get():#pygame.event.get()은 게임판에서 발생하는 다양한 이벤트를 리턴한다. 그 중 event타입이 마우스로 창을 닫는거면 crash의 값을 True로 설정하여 while을 빠져나오고
            if event.type == pygame.QUIT:
                crashed = True      #게임을 종료하기 위한 플래그입니다
            
            if event.type == pygame.KEYDOWN:#게이머가 키를 누르면
                if event.key == pygame.K_UP:#윗방향키 누르면
                    y_change -= 5 #5픽셀씩 위로
                elif event.key == pygame.K_DOWN:#아랫방향키 누르면
                    y_change += 5#5픽셀씩 아래로 Y축이 아래방향으로 되어있는듯
                
            if event.type == pygame.KEYUP:#키 누르다 때
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0#키를 놓으면 변화가 없도록 한다.
                    
        y+=y_change#키보드 입력에 따라 비행기의 Y좌표를 변경한다.
            
        gamepad.fill(WHITE) #아니면 게임판을 흰색으로 채우고

        background1_x -= 2
        background2_x -= 2

        bat_x-=7#박쥐를 우리 비행기쪽으로 7픽셀씩 날아오게 함 왼쪽끝까지가면 박쥐 위치 다시잡기
        if bat_x <= 0:
            bat_x = pad_width
            bat_y = random.randrange(0,pad_height)#우리의 적인 박쥐가 날아올 위치 정함 박쥐의 x좌표는 게임판의 맨 오른쪽끝,y는 게임판 높이범위중 무작위

        if fire == None:#fire가 None이면 30픽셀씩 다가오게 해서 이는 아무런 방해물없는 시간 지연책
            fire_x -= 30
        else:
            fire_x -= 15#만약 불덩이라면 15픽셀씩 날아오게함
            
        if fire_x <= 0:
            fire_x = pad_width#불덩이가 날아올 위치를 박쥐와 동일한 로직으로
            fire_y = random.randrange(0,pad_height)
            random.shuffle(fires)#불덩이나 시간 지연책이 나올수 있게 리스트 섞고
            fire = fires[0]#그 중 첫번째 요소 선택

        if background1_x == -background_width:
            background1_x = background_width
        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1, background1_x,0)
        drawObject(background2, background2_x,0)
        drawObject(bat,bat_x,bat_y)
        if fire != None:
            drawObject(fire,fire_x,fire_y)
        drawObject(aircraft,x,y)
            
        pygame.display.update()#게임판을 다시 그립니다.
        clock.tick(60)#그리고 FPS값을 60으로 설정하여 while문을 반복하도록 한다.
    pygame.quit()#초기화한 pygame을 종료한다.
    quit()

def initGame():#게임을 초기화하고 시작하는 함수
    global gamepad, aircraft, clock,background1,background2
    global bat,fires

    fires = []#장애물 리스트 만들기 fire는 불덩이 None은 시간지연책

    pygame.init()# pygame라이브러리를 초기화합니다. pygame을 활용하려면 최초에 항상 pygame.init()을 호출해야한다. 이제 우리 코드에서 pygame이 제공하는 다양한 기능을 사용할 준비가 되었다
    gamepad = pygame.display.set_mode((pad_width, pad_height))# 게임판의 크기를 1024*512로 설정
    pygame.display.set_caption('PyFlying')#게임판타이틀 설정
    aircraft = pygame.image.load('images/plane.png')
    background1 = pygame.image.load('images/background.png')#배경이미지 파일을 읽어 전역변수 background에 할
    background2 = background1.copy()
    bat = pygame.image.load('images/bat.png')
    fires.append(pygame.image.load('images/fireball.png'))
    fires.append(pygame.image.load('images/fireball2.png'))

    for i in range(5):
        fires.append(None)#시간지연책
    
    clock = pygame.time.Clock()#게임의 초당 프레임(FPS)설정을 위해 클락을 생성한다. 사람 눈에 자연스럽게 보이게 되는 FPS는 30이지만 60으로 할예정
    runGame()#게임판 초기화가 마무리 되었으니 실제 게임 구동을 위한 함수인 runGame()함수를 호출한다

initGame()
