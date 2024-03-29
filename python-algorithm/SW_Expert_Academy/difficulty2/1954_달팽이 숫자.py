import sys
sys.stdin = open("input.txt","r")
T = int(input())
for test_case in range(1,T+1):
    print(f"#{test_case} ",end="")
    N = int(input())
    board = [[0]*N for _ in range(N)]
    # 회전하는 방향은 항상 시계방향
    # 우,하,좌,상의 방향
    # 계속 움직이다 index가 벋어나면 방향에 따른 값을 추가한다.
    # 우: 행은 그대로 열에 +1 ++j
    # 하: 열은 그대로 행에 +1 ++i
    # 좌: 행은 그대로 열에 -1 --j
    # 상: 열은 그래도 행에 -1 --i
    # "벋어나면" 의 조건을 지정해주어하는데....
    # 방향별로 남은 이동거리를 미리 지정해준다.
    # N이 5일경우 5,5,5,5라고 주어지고
    # 한바퀴돌고 [i][j]의 인덱스라있으면 j가 0이면(0번째 열이면) -1
    # 그렇지 않을 경우에는 -2씩해둔다. 만약 값을 뺐는데 0이다! 그러면 종료
    vector = {0:N,1:N,2:N,3:N}
    # 0: 우, 1: 하, 2: 좌, 3: 상
    num = 0
    move_cnt = 100
    vec = 0
    i,j = 0,0
    while True :
        print("i:",i,"j:",j,"vec:",vec,"vec%4:",vec%4)
        
        vec = vec % 4
        # 오른쪽으로 이동
        if vec == 0:
            if j ==0 :
                vector[vec] -= 1
            else:
                vector[vec] -= 2
            if vector[vec] == 0:
                break
            else:
                for _ in range(vector[vec]+1):
                    num += 1
                    board[i][j] = num
                    j += 1
                    print("i:",i,"j:",j,"vec:",vec,"vec%4:",vec%4)
                    for list in board:
                        print(list)
                    print("--------------------------------------")
                vec += 1
                j -= 1
        # 아래쪽으로 이동
        elif vec == 1:
            # if j ==0 :
            #     vector[vec] -= 1
            # else:
            vector[vec] -= 2
            if vector[vec] == 0:
                break
            else:
                # print("vector[vec]+1",vector[vec]+1)
                for _ in range(vector[vec]+1):
                    i += 1
                    num += 1
                    board[i][j] = num
                vec += 1
        # 왼쪽으로 이동
        elif vec == 2:
            # if j ==0 :
            #     vector[vec] -= 1
            # else:
            vector[vec] -= 2
            if vector[vec] == 0:
                break
            else:
                print("!!!!!!!",vector[vec]+1,"!!!!!!")
                for _ in range(vector[vec]+1):
                    j -= 1
                    num += 1
                    # print("i:",i-1,"j:",j-1,"board[i][j]",board[i-1][j-1])
                    board[i][j] = num
                vec += 1
        #위쪽으로 이동
        elif vec == 3:
            if j ==0 :
                vector[vec] -= 1
            else:
                vector[vec] -= 2
            if vector[vec] == 0:
                break
            else:
                for _ in range(vector[vec]+1):
                    i -= 1
                    num += 1
                    board[i][j] = num

                    for list in board:
                        print(list)
                    print("--------------------------------------")
                vec += 1

        for list in board:
            print(list)
        print("--------------------------------------")
    