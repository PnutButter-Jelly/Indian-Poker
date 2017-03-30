# 인디언 포커
# P찬솔 제작

from random import *
from os import system

card = []  # Card
U_c = 0  # User Card
C_c = 0  # Computer Card
U_b = 0  # User Betting
C_b = 0  # Computer Betting
Bet = 0  # Betting counter
U_m = 30  # User money
C_m = 30  # Computer money
Game = [U_m, C_m, U_b, C_b, Bet, U_c, C_c]

def School(Game):
    Game[4] += 2
    Game[2] = 1
    Game[3] = 1
    Game[0] -= 1
    Game[1] -= 1
    Flash()
    Status(Game)
    print("첫 베팅을 합니다.")
    return 0

def Flash():
    system('cls')
    return

def Status(Game):
    print("-------------------------------------")
    print("나의 칩     : ", Game[0])
    print("컴퓨터의 칩 : ", Game[1])
    print("나의 누적 베팅금액 : ", Game[2])
    print("컴퓨터의 누적 베팅금액 : ", Game[3])
    print("누적 베팅금액 : ", Game[4])
    print("-------------------------------------")
    return Game

def Newcard():
    global card
    card = []
    for x in range(0, 2):
        for y in range(1, 11):
            card += [y]
    shuffle(card)

def Dealer(Game):
    Game[5] = card[2 * turn - 1]
    Game[6] = card[2 * turn]
    print("상대의 카드는", Game[6], "입니다.")
    return Game

def Betting(Game):
    global a
    while 1:
        if Game[0] * Game[1] <= 0:
            Flash()
            Status(Game)
            print("배팅이 종료되었습니다.")
            return Game
        Flash()
        Status(Game)
        Dealer(Game)
        a = int(input("얼마를 베팅하시겠습니까? : "))

        if a == 30911:
            print("신의 축복을 받았습니다. 돈이 20 증가합니다.")
            Game[0] += 20
            c = input("<enter>")
            if c == "30911":
                print("정성이 가득하구나")
                print("신의 축복을 받았습니다. 돈이 40 증가합니다.")
                Game[0] += 40
                c = input("<enter>")
                if c == "30911":
                    print("정성이 아주 가득하구나")
                    print("신의 축복을 받았습니다. 돈이 60 증가합니다.")
                    Game[0] += 60
                    c = input("<enter>")
                    if c == "30911":
                        print("정성이 정말로 아주 많구나")
                        print("신의 축복을 받았습니다. 돈이 100 증가합니다.")
                        Game[0] += 100
                        c = input("<enter>")
                        if c == "30911":
                            print("썅년이 사실 아닌거 다알아")
                            print("신을 노하게 했습니다. 돈을 다시 다 뺏겼습니다.")
                            Game[0] -= 240
                            c = input("<enter>")


        elif a == 0:
            print("베팅을 포기하셨습니다.")
            print("당신의 카드는 ", Game[5], "입니다.")
            Game[1] += Game[4]
            Game[4] = 0
            if Game[5] == 10:
                print("카드가 10인채로 포기하셨으니 패널티가 부여됩니다.")
                print("상대에게 10개의 칩을 줍니다.")
                Game[0] -= 10
                Game[1] += 10
            else:
                pass
            input("(enter)")

            return Game

        elif a + Game[2] < Game[3]:
            print("컴퓨터가 베팅한 금액보다적게 베팅할 수 없습니다.")
            input("(enter)")
        elif a > Game[0]:
            print("당신의 소지금보다 베팅금이 더 많습니다.")
            input("(enter)")
        elif a + Game[2] > Game[1] + Game[3]:
            print("컴퓨터의 소지금보다 배팅금이 더 많습니다.")
            input("(enter)")
        elif a > 10 + b:
            print("배팅금은 10을 넘을 수 없습니다.")
            input("(enter)")
        else:
            Game[2] += a
            Game[4] += a
            Game[0] -= a
            break

    if Game[3] == Game[2]:
        Flash()
        Status(Game)
        print("배팅이 종료되었습니다.")
        return Game
    else:
        Combet(Game)

    if b == 0:
        print("컴퓨터가 배팅을 포기했습니다.")
        print("당신의 카드는 ", Game[5], "입니다.")
        if Game[6] == 10:
            print("컴퓨터가 카드가 10인채로 포기하셨으니 패널티가 부여됩니다.")
            print("당신에게 10개의 칩을 줍니다.")
            Game[1] -= 10
            Game[0] += 10
        else:
            pass
        Game[0] += Game[4]
        Game[4] = 0
        input("(enter)")
        return Game
    elif Game[3] == Game[2]:
        Flash()
        Status(Game)
        print("배팅이 종료되었습니다.")
        return Game
    else:
        Betting(Game)

def Comthink(card,Game):
    global Comthink_result
    Count = card[2 * turn - 1:19]
    lose = 0
    for x in Count:
        if x < Game[5]:
            lose += 1
    Comthink_1 = lose / len(Count)

    if Game[2] <= 2:
        Comthink_2 = 0
    elif 2 < Game[2] <= 4:
        Comthink_2 = 1
    elif 4 < Game[2] <= 6:
        Comthink_2 = 3
    elif 6 < Game[2] <= 7:
        Comthink_2 = 5
    elif 7 < Game[2] <= 9:
        Comthink_2 = 7
    elif 9 < Game[2]:
        Comthink_2 = 10
    else:
        print("error_think_2")

    if Game[4] <= 5:
        Comthink_3 = 0
    elif 5 < Game[4] <= 10:
        Comthink_3 = 1
    elif 10 < Game[4] <= 15:
        Comthink_3 = 3
    elif 15 < Game[4] <= 20:
        Comthink_3 = 5
    elif 20 < Game[4] <= 25:
        Comthink_3 = 10
    elif 25 < Game[4] <= 30:
        Comthink_3 = 5
    elif 30 < Game[4]:
        Comthink_3 = 0
    else:
        print("error_think_3")

    if Game[1] <= 5:
        Comthink_4 = 0
    elif 5 < Game[1] <= 10:
        Comthink_4 = 20
    elif 11 < Game[1] <= 15:
        Comthink_4 = 15
    elif 15 < Game[1] <= 20:
        Comthink_4 = 10
    elif 20 < Game[1] <= 25:
        Comthink_4 = 5
    elif 25 < Game[1] <= 30:
        Comthink_4 = 4
    elif 30 < Game[1]:
        Comthink_4 = 0
    else:
        print("error_think_4")

    Comthink_result = int((Comthink_2 + Comthink_3 + Comthink_4) * Comthink_1 + 5)

def Combet(Game):
    Comthink(card, Game)
    global b
    while(1):
        think = randint(0, 50)
        #print(Comthink_result, int((50 - Comthink_result) / 10 * 4),int((50 - Comthink_result) / 10 * 1),int((50 - Comthink_result) / 10 * 2),int((50 - Comthink_result) / 10 * 3))

        if think <= Comthink_result :
            b = 0
            Game[3] += 0
        elif Comthink_result < think <= int((50 - Comthink_result) / 10 * 4):
            b = a - b
            Game[3] += b
            Game[1] -= b
            Game[4] += b
        elif int((50 - Comthink_result) / 10 * 4) < think <= int((50 - Comthink_result) / 10 * 7):
            if Game[0] >= 3:
                if Game[1] >= a + 3:
                    b = Game[2] - Game[3]
                    Game[3] += b
                    Game[1] -= b
                    Game[4] += b
                elif Game[1] < a + 3:
                    b = Game[1]
                    Game[3] += b
                    Game[1] = 0
                    Game[4] += b
                else:
                    print("error1")
            elif Game[0] <  3:
                b = Game[0] + a
                Game[3] += b
                Game[1] -= b
                Game[4] += b
            else:
                print("error3")

        elif int((50 - Comthink_result) / 10 * 7) < think <= int((50 - Comthink_result) / 10 * 9):
            if Game[0] >= 5:
                if Game[1] >= a + 5:
                    b = a + 5
                    Game[3] += b
                    Game[1] -= b
                    Game[4] += b
                elif Game[1] < a + 5:
                    b = Game[1]
                    Game[3] += b
                    Game[1] = 0
                    Game[4] += b
                else:
                    print("error1")
            elif Game[0] <  5:
                b = Game[0] + a
                Game[3] += b
                Game[1] -= b
                Game[4] += b
            else:
                print("error3")

        else:
            if Game[0] >= 10:
                if Game[1] >= a + 10:
                    b = a + 10
                    Game[3] += b
                    Game[1] -= b
                    Game[4] += b
                elif Game[1] < a + 10:
                    b = Game[1]
                    Game[3] += b
                    Game[1] = 0
                    Game[4] += b
                else:
                    print("error1")
            elif Game[0] <  10:
                b = Game[0] + a
                Game[3] += b
                Game[1] -= b
                Game[4] += b
            else:
                print("error3")

        if Game[1] >= 0:
            if b >= 0:
                break
            else:
                pass
        else:
            pass

    if b == 0:
        pass
    else:
        print("-------------------------------------")
        print("컴퓨터가",b,"을 베팅했습니다.")
        input("(enter)")

    return Game

def Judge(Game):
    print("당신의 카드는 ",Game[5],"입니다.")
    if Game[5] > Game[6]:
        Game[0] += Game[4]
        Game[4] = 0
        print("이겼습니다.")
        input("(enter)")
        return Game
    elif Game[5] < Game[6]:
        Game[1] += Game[4]
        Game[4] = 0
        print("졌습니다.")
        input("(enter)")
        return Game
    else:
        print ("비겼습니다. 배팅금을 유지한채 계속합니다.")
        input("(enter)")
        return Game

print("인디언 포커")
input("룰알지 시작한다? (enter)")

while 1:
    Newcard()
    for turn in range(1, 11):
        a=0
        b=0
        School(Game)
        input("(enter)")
        Betting(Game)

        if Game[4] == 0:
            pass
        else:
            Judge(Game)

        if Game[0] <= 0:
            Flash()
            Status(Game)
            print("생각할 줄 모르는 컴퓨터에게 농락을 당한후 패배하셨습니다.")
            break

        elif Game[1] <= 0:
            Flash()
            Status(Game)
            print("승리하셨지만... 알아두셔야할건 상대는 생각할 줄 모르는 간단한 프로그램이란점 입니다.")
            break

        else:
            pass

        Game[2] = 0
        Game[3] = 0

    if Game[0] <= 0:
        break
    elif Game[1] <= 0:
        break

input("Press Enter to exit")
