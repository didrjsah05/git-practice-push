# import random

# def game():
#     """
#     숫자 맞히기
#     """
#     answer = random.randint(1, 10)

#     while True:
#         guess = int(input("숫자를 입력하세요."))

#         if answer > guess:
#            print("up")

#         elif answer < guess:
#             print("down")

#         else:
#             print("정답")

#             break

# game()

# 일반적으로 찾는 방식

def find(list, target): #리스트와 값
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1 # -1 은 아닐테니까

# if __name__=="__main__": # __name__  : __main 이 들어감 만약 변수 이름이 main 파일 내에서 만들었을 때만 동작하도록 하는 장치

#     list = [1,2,3,4,5]

#     a = find(list, 3)

# def binary_search(list, target, low= None, High = None):

#     if low is None:
#         low = 0

#     if high is None:
#         high = len(list) - 1

#     if high < low:
#         return -1 # 값 서칭 불가
    

#     midpoint = (low + high) // 2

    # 만약에 타겟 값이 서칭한 값과 같다면, return midpoint
    # 만약에 타겟 값이 서칭한 값보다 작다면 다시 함수 불러오기
    # return binary_search (list, target, low, midpoint -1)
    # 만약에 타겟 값이 서칭한 값보다 크다면 다시 불러오기
    # return