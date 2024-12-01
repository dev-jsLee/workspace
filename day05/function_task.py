# 함수
# 외부에서 매개변수에 담을 값을 전달받아
# 매개변수로 처리할 로직을 작성해놓은 
# 추상적인 기능 블록을 의미한다.
def add_nums(num1, num2):
    return num1 + num2

print(add_nums(num1=3, num2=5))

# 두 개의 숫자와 연산자를 문자열로 입력받아
# 문자열 연산자에 따라 결과값을 다르게 return하는 함수 만들기
def calculator(num1, num2, oper):
    # oper -> "+", "-", "*", "/"
    answer = 0
    # oper의 값이 "+"이면
    if oper == "+":
        # answer에 num1과 num2를 더한 값을 저장한다.
        answer = num1 + num2
    # elif? 동시에 일어나진 않네?
    # oper의 값이 "-"이면
    elif oper == "-":
        # answer에 num1에서 num2를 뺀 값을 저장한다.
        answer = num1 - num2
    
    # 위의 과정을 거쳐서 저장된 answer의 값을
    # 외부로 돌려준다.
    return answer

print(calculator(3, 5, "+") == 8)
print(calculator(5, 3, "-") == 2)
print(calculator(3, 5, "*") == 15)
print(calculator(10, 2, "/") == 5)
