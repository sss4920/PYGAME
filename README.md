# PYGAME
파이썬으로 게임만들기 도전!  
```cmd:
pip install pygame 
```

### 1회차. 게임창 만들기 사이즈 `'1024*512'`

### 2회차. 비행기 만들고 위 아래 키 누르면 움직이는 거 구현
좌표가 우리가 알고 있는 x,y좌표와 다른 것 같다. 설명이 부족해서 추론한 거지만 우리는 x좌표가 오른쪽방향을 향하고 y좌표가 위방향을 향하는 것으로
알고 있지만 여기서는 y좌표가 아래방향을 향하는 것 같다. 따라서 `위방향키를 누르면 y의 변화량을 줄여야되고 아래방향키를 누르면 y의 변화량을 늘려야하는 것 같다.`

### 3회차. 배경사진 넣기  
`오타 조심하자; 오타때문에 실행 안되는거 겨우찾음`

### 4회차. 무한으로 움직이는 배경사진 넣기 
`copy`함수를 쓰면 이미지도 복사되는 것이 놀라웠고 방식은 이렇다. 사진의 왼쪽 상단 점의 좌표를 기준으로 (0,0)을 넣고
원본사진의 복사본을 (1024,0)좌표에 해당하는 위치에 왼쪽 상단 점을 위치시켜 `blit`한 후에 `run`중 두개의 사진의 x좌표를 줄이다가 -1024가 먼저 되는
사진의 x좌표를 다시 1024로 돌려놓는 식으로 무한으로 연결된 배경 사진을 만든다.  
