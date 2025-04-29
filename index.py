import random

def game():
    """
    숫자 맞히기 게임
    """
    answer = random.randint(1, 10)

    while True:
        guess = int(input("숫자를 입력하세요."))

        if answer > guess:
           print("up")

        elif answer < guess:
            print("down")

        else:
            print("정답")

            break

game()


