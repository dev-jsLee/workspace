

# 함수를 만들어보자.
# 입력되는 값 중, True/False인 어떤 매개변수의 값에 따라
# 결과 값이 다르게 나오는 함수를 만들어보자.
# +추가설명
# 함수명 is_add
# 매개변수: num1, num2, is_add: bool
# 반환: is_add가 True이면 num1과 num2의 합을 반환
# is_add가 False이면 num1과 num2의 차를 반환
def is_add(num1, num2, is_add: bool=True) -> int:
    pass
    # 1안
    # result = 0
    # if is_add==True:
    #     result = num1 + num2
    # else:
    #     result = num1 - num2
    # return result

    # 2안
    # result = num1 - num2
    # if is_add==True:
    #     result = num1 + num2
    # return result

    # 3안
    # result = num1
    # if is_add==True:
    #     result += num1
    # else:
    #     result -= num1

    # 4안
    # result = num1 (num2 if is_add==True else -num2)
    
    # 5안
    result = num1 + num2 * (1 if is_add==True else -1)

    # 6안
    (num1 + num2) if is_add else (num1 - num2)
    return result


if __name__ == "__main__":
    print(is_add(10, 5,))

