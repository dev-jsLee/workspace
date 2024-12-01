# 클래스와 메서드
# 
class Student():
    # name = ""
    def __init__(self, input_name, age=0, gender=None) -> None:
        # 이름, 나이, 성별
        self.name = input_name
        self.age = age
        self.gender = gender
        self.print_infos()
        # return 0 # 되돌려줄 값(주소값)이 정해져 있기 때문에
        # 초기화메서드(__init__)는 return을 반드시 None으로 해주어야 한다.
    
    def print_infos(self):
        print(self.name, self.age, self.gender)

if __name__ == "__main__":
    # 객체화
    # 클래스라는 개념을 실체화한(구체화한)
    # 대상을 만드는 것이다.
    hong = Student("honggildong", gender="남")
    kim = Student("kimC", 30, "여")

    


    # print(hong.name)
    # print(kim.name)

    # print(hong)
    # print(kim)