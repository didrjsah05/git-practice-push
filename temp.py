def binary_search(list, target, low=None, high=None):
    
    if low is None:
        low = 0
    
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1  # 값 서칭 불가

    midpoint = (low + high) // 2

    if target < list[midpoint]:
        return binary_search(list, target, low, midpoint - 1)
    
    elif target > list[midpoint]:
        return binary_search(list, target, midpoint + 1, high)
    
    else:  
        return midpoint

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    a = binary_search(list, 5)
    
    print(a)

    

    # 만약에 타겟 값이 서칭한 값과 같다면, return midpoint
    # 만약에 타겟 값이 서칭한 값보다 작다면 다시 함수 불러오기
    # return binary_search (list, target, low, midpoint -1)
    # 만약에 타겟 값이 서칭한 값보다 크다면 다시 불러오기
    # return