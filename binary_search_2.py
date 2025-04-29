def binary_search_2(list, target, low=None, high=None):
    
    if low is None:
        low = 0
    
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1  # 값 서칭 불가
        

    while low <= high:
        midpoint = (low + high) // 2

        if target < list[midpoint]:
            high = midpoint - 1
        elif target > list[midpoint]:
            low = midpoint + 1
        else:
            return midpoint  # 찾으면 인덱스 반환

    return -1  # 못 찾으면 -1

if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    a = binary_search_2(list, 9)
    
    print(a)

