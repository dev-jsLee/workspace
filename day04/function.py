

# 함수
# (선택)매개변수를 전달받아
# (필수)미리 정해진 동작을 수행하는 기능
# (선택)수행 결과에 따라 만들어진 값을 반환하는 기능
#       -> 반환하는 코드에 도달한 이후의 코드는
#       -> 실행되지 않는다.
# 매개변수x, 반환x
def func_xx():
    print("매개변수x, 반환x")

# 매개변수o, 반환x
def func_ox(var):
    print(var)

# 매개변수x, 반환o
def func_xo():
    return "홍길동"

# 매개변수o, 반환o
def func_oo(fname, lname):
    result = f"{fname} {lname}"
    return result
    print(result) # 실행되지 않음.

if __name__ == "__main__":
    var = func_oo("이", "준상")
    print(var)