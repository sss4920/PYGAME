__author__ = 'sss4920@naver.com'
'''
오늘은 pygame에서 배경을 만들어 볼겁니다.
'''

import pygame       #pygame을 임포트 합니다

WHITE = (255,255,255) # 흰색을 표현하는 값
pad_width = 1024 #게임판의 폭
pad_height = 512#게임판의 높이를 각각 전역변수에 저장


def airplane(x,y):#우리가 조정할 비행기를 게임판 위 (x,y)위치에 그립니다.
    global gamepad, aircraft
    gamepad.blit(aircraft,(x,y))



def runGame(): #실제 게임이 구동되는 함수 밑에 initGame()함수에서 호출됨
    global gamepad, aircraft,clock
    x = pad_width *0.05
    y = pad_height * 0.8    #비행기의 최초위치를 게임판의 왼쪽 적당한 위치에 두도록 좌표설정 비행기가 아래위로 움직이기 때문에 비행기위 y좌표 변화를 y_change변수로 나타낼 것
    y_change = 0

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
        airplane(x,y)
        pygame.display.update()#게임판을 다시 그립니다.
        clock.tick(60)#그리고 FPS값을 60으로 설정하여 while문을 반복하도록 한다.
    pygame.quit()#초기화한 pygame을 종료한다.
    quit()

def initGame():#게임을 초기화하고 시작하는 함수
    global gamepad, aircraft, clock

    pygame.init()# pygame라이브러리를 초기화합니다. pygame을 활용하려면 최초에 항상 pygame.init()을 호출해야한다. 이제 우리 코드에서 pygame이 제공하는 다양한 기능을 사용할 준비가 되었다
    gamepad = pygame.display.set_mode((pad_width, pad_height))# 게임판의 크기를 1024*512로 설정
    pygame.display.set_caption('PyFlying')#게임판타이틀 설정
    aircraft = pygame.image.load('images/plane.png')
    clock = pygame.time.Clock()#게임의 초당 프레임(FPS)설정을 위해 클락을 생성한다. 사람 눈에 자연스럽게 보이게 되는 FPS는 30이지만 60으로 할예정
    runGame()#게임판 초기화가 마무리 되었으니 실제 게임 구동을 위한 함수인 runGame()함수를 호출한다

initGame()
